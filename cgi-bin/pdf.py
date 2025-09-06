# Dependencies: texlive-xetex texlive-luatex texlive-fonts-extra

from dataclasses import dataclass
import io
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
import urllib

import jinja2

GITHUB_URL = 'https://github.com/mrozekma/cv/blob/master/cgi-bin/pdf.py'

root_dir = Path(__file__).parents[1]
tex_dir = root_dir / 'tex'
is_cgi = 'QUERY_STRING' in os.environ

if is_cgi:
	def excepthook(typ, value, tb):
		print("Content-type: text/plain")
		print()
		print("There was an exception trying to generate the PDF. If you're thinking about hiring me, let's agree to pretend this never happened.")
		print()
		print(f"{typ.__name__}: {value}")
		print()
		summary = traceback.StackSummary.extract(traceback.walk_tb(tb))
		for line in summary.format():
			print(line)
		for frame in summary:
			if frame.filename == __file__:
				print(f"See the failing line in Github at {GITHUB_URL}#L{frame.lineno}")
				break
	sys.excepthook = excepthook

@dataclass
class Entry:
	name: str
	section: str
	selected: bool

	def __post_init__(self):
		self.name = Entry.make_form_name(self.name)
		self.section = Entry.make_form_name(self.section)

	@staticmethod
	def make_form_name(name: str):
		name = name.lower()
		name = re.sub(r'[^a-z0-9]+', '-', name)
		name = re.sub(r'^-+', '', name)
		name = re.sub(r'-+$', '', name)
		return name

entries: list[Entry] = []
section = None
for line in (tex_dir / 'sections.txt').read_text().splitlines():
	if line == '':
		continue
	elif line.endswith(':'):
		section = line[:-1]
	elif line.startswith('  * ') or line.startswith('  - '):
		assert section is not None
		entries.append(Entry(line[4:], section, line[2] == '*'))
	else:
		raise RuntimeError("Malformed sections list")
del section

def setAllEntries(selection: bool):
	for entry in entries:
		entry.selected = selection

if is_cgi:
	qs = urllib.parse.parse_qs(os.environ['QUERY_STRING'])
	if qs:
		for entry in entries:
			entry.selected = qs.get(entry.name, ['off'])[-1] == 'on'
	args = None
elif 'TEST' in os.environ:
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', type = Path, metavar = 'FILENAME')
	parser.add_argument('--tmpdir', type = Path, metavar = 'DIR')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-a', '--all', dest = 'selections', action = 'append_const', const = 'all')
	group.add_argument('-n', '--none', dest = 'selections', action = 'append_const', const = 'none')
	for entry in entries:
		parser.add_argument(f"--{entry.name}", dest = 'selections', action = 'append_const', const = ( entry, True ))
		parser.add_argument(f"--no-{entry.name}", dest = 'selections', action = 'append_const', const = ( entry, False ))
	args = parser.parse_args()

	for selection in args.selections or []:
		match selection:
			case 'all':
				setAllEntries(True)
			case 'none':
				setAllEntries(False)
			case (entry, value):
				entry.selected = value
else:
	raise RuntimeError("Unrecognized request type")

dest: Path = (args.tmpdir if args else None) or Path(tempfile.mkdtemp(prefix = 'cv-tmp'))
dest = dest.resolve()
dest.mkdir(parents = True, exist_ok = True)
try:
	tex_in = tex_dir / 'resume.tex'
	tex_out = dest / 'resume.tex'

	jinja_env = jinja2.Environment(
		loader = jinja2.FileSystemLoader(tex_dir),
		undefined = jinja2.StrictUndefined,
		trim_blocks = True,
		line_statement_prefix = r'\jinja',
		comment_start_string = '%',
		comment_end_string = '\n',
	)

	def debug():
		rtn = io.StringIO()
		rtn.write(
			'\\cvsection{entries}\n'
			'\\begin{cvparagraph}\n'
			'\\begin{itemize}[leftmargin=2ex, nosep, noitemsep]\n'
		)
		for section in sorted({ entry.section for entry in entries }):
			rtn.write(f"\\item {section}\n")
			rtn.write("\\begin{itemize}[leftmargin=2ex, nosep, noitemsep]\n")
			for entry in entries:
				if entry.section == section:
					rtn.write(f"\\item {entry.name}: {'yes' if entry.selected else 'no'}\n")
			rtn.write("\\end{itemize}\n")
		rtn.write(
			'\\end{itemize}\n'
			'\\end{cvparagraph}\n'
		)
		return rtn.getvalue()

	vars = {
		'debug': debug,
		'any_selections': False,
		'min': min,
		'max': max,
	}

	for section in { entry.section for entry in entries }:
		vars[section.replace('-', '_')] = False
	for entry in entries:
		vars[entry.name.replace('-', '_')] = entry.selected
		if entry.selected:
			vars[entry.section.replace('-', '_')] = True
			vars['any_selections'] = True

	template: jinja2.Template = jinja_env.get_template('resume.tex')
	tex = template.render(vars)
	tex_out.write_text(tex)

	with open(dest / 'output', 'w') as f:
		subprocess.run(['xelatex', '-halt-on-error', '-output-directory', str(dest), str(tex_out)], cwd = tex_dir, stdout = f, stderr = subprocess.STDOUT)
	pdf = dest / 'resume.pdf'
	pdf_bytes = pdf.read_bytes()

	# We intentionally put off sending the headers for as long as possible in case of exceptions. At this point we should be safe
	if is_cgi:
		print("Content-type: application/pdf")
		print('Content-Disposition: inline; filename="michael_mrozek_resume.pdf"')
		print()
		sys.stdout.flush()
		sys.stdout.buffer.write(pdf_bytes)
	elif args.output:
		args.output.write_bytes(pdf_bytes)
	else:
		for entry in entries:
			print(entry.name, entry.section, entry.selected)
		print()
		print(f"Generated {len(pdf_bytes)} bytes")

except Exception:
	print((dest / 'output').read_text(), file = sys.stderr)
	raise RuntimeError("Failed to generate PDF")
finally:
	if args is None or args.tmpdir is None:
		shutil.rmtree(dest)
