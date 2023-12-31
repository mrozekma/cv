# Dependencies: texlive-xetex texlive-luatex texlive-fonts-extra

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
import yaml

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

sections: dict[str, str] = {} # entry -> section containing the entry
entries: dict[str, bool] = {} # entry -> is selected

def make_form_name(entry: str):
	entry = entry.lower()
	entry = re.sub(r'[^a-z0-9]+', '-', entry)
	entry = re.sub(r'^-+', '', entry)
	entry = re.sub(r'-+$', '', entry)
	return entry

section = None
for line in (tex_dir / 'sections.txt').read_text().splitlines():
	if line == '':
		continue
	elif line.endswith(':'):
		section = make_form_name(line[:-1])
	elif line.startswith('  * ') or line.startswith('  - '):
		entry = make_form_name(line[4:])
		entries[entry] = (line[2] == '*')
		sections[entry] = section
	else:
		raise RuntimeError("Malformed sections list")
del section

if is_cgi:
	qs = urllib.parse.parse_qsl(os.environ['QUERY_STRING'])
	for name, value in qs:
		if name in entries and value == 'on':
			entries[name] = True
	args = None
elif 'TEST' in os.environ:
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', type = Path, metavar = 'FILENAME')
	parser.add_argument('--tmpdir', type = Path, metavar = 'DIR')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-a', '--all', dest = 'selections', action = 'append_const', const = ( None, True ))
	group.add_argument('-n', '--none', dest = 'selections', action = 'append_const', const = ( None, False ))
	for entry in entries:
		parser.add_argument(f"--{entry}", dest = 'selections', action = 'append_const', const = ( entry, True ))
		parser.add_argument(f"--no-{entry}", dest = 'selections', action = 'append_const', const = ( entry, False ))
	args = parser.parse_args()

	for selection, selected in args.selections or []:
		if selection is None:
			entries = { k: selected for k in entries }
		else:
			entries[selection] = selected
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
		line_statement_prefix = '\jinja',
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
		for section in sorted({ v for k, v in sections.items() }):
			rtn.write(f"\\item {section}\n")
			rtn.write("\\begin{itemize}[leftmargin=2ex, nosep, noitemsep]\n")
			for entry, selected in entries.items():
				if sections[entry] == section:
					rtn.write(f"\\item {entry}: {'yes' if selected else 'no'}\n")
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

	for section in sections.values():
		vars[section.replace('-', '_')] = False
	for entry, selected in entries.items():
		vars[entry.replace('-', '_')] = selected
		if selected:
			vars[sections[entry].replace('-', '_')] = True
			vars['any_selections'] = True

	template: jinja2.Template = jinja_env.get_template('resume.tex')
	tex = template.render(vars)
		# entry_selected = lambda entry: entry in selected_entries,
		# section_selected = lambda section: section in selected_sections,
		# *{ entry: }
		# debug_entries = debug_entries,
		# any_selections = len(selected_entries) > 0,
	# )
	# tex = tex_in.read_text()
	# print('\n'.join(fr"\useentry{{{entry}}}" for entry in selected_entries), file = sys.stderr)
	# tex = tex.replace(r'%%% entries %%%', '\n'.join(fr"\useentry{{{entry}}}" for entry in selected_entries))
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
		print(f"Generated {len(pdf_bytes)} bytes")

except Exception:
	print((dest / 'output').read_text(), file = sys.stderr)
	raise RuntimeError("Failed to generate PDF")
finally:
	if args is None or args.tmpdir is None:
		shutil.rmtree(dest)
