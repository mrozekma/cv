#!/usr/bin/env python3
# Dependencies: texlive-xetex texlive-luatex texlive-fonts-extra

import cgi
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import traceback

GITHUB_URL = 'https://github.com/mrozekma/cv/blob/master/cgi-bin/pdf.py'

def exceptHook(typ, value, tb):
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
sys.excepthook = exceptHook

form = cgi.FieldStorage()
entries = {name for name in form if form[name].value == 'on'}

# The Python version of this code used to do more sanity checking on the arguments, but it's not worth
# reproducing the section/entry structure here for that -- the frontend enforces sane values, so this can
# only produce weird output if the user passes a weird combination of arguments directly. Instead, just
# make sure the tag names are properly formatted
tagPattern = re.compile('[a-z0-9-]+')
if any(tagPattern.match(entry) is None for entry in entries):
	raise ValueError("Bad tag name")

rootDir = Path(__file__).parent.parent
texDir = rootDir / 'tex'
dest = Path(tempfile.mkdtemp(prefix = 'cv-tmp'))
try:
	texIn = texDir / 'resume.tex'
	texOut = dest / 'resume.tex'
	tex = texIn.read_text()
	tex = tex.replace(r'%%% TAGS %%%', '\n'.join(fr"\usetag{{{entry}}}" for entry in entries))
	texOut.write_text(tex)

	with open(dest / 'output', 'w') as f:
		subprocess.run(['xelatex', '-halt-on-error', '-output-directory', str(dest), str(texOut)], cwd = texDir, stdout = f, stderr = subprocess.STDOUT)
	pdf = Path(dest) / 'resume.pdf'
	pdfBytes = pdf.read_bytes()

	# We intentionally put off sending the headers for as long as possible in case of exceptions. At this point we should be safe
	print("Content-type: application/pdf")
	print('Content-Disposition: inline; filename="michael_mrozek_resume.pdf"')
	print()
	sys.stdout.flush()
	sys.stdout.buffer.write(pdfBytes)
except Exception:
	print((dest / 'output').read_text(), file = sys.stderr)
	raise RuntimeError("Failed to generate PDF")
finally:
	shutil.rmtree(dest)
