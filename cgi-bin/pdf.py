#!/usr/bin/env python3
# Dependencies: texlive-xetex texlive-luatex texlive-fonts-extra

import cgitb
cgitb.enable()

import cgi
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

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

	with open(dest / 'stdout', 'w') as f:
		subprocess.run(['xelatex', '-halt-on-error', '-output-directory', str(dest), str(texOut)], cwd = texDir, stdout = f, stderr = subprocess.STDOUT)
	print("Content-type: application/pdf\n")
	sys.stdout.flush()
	pdf = Path(dest) / 'resume.pdf'
	sys.stdout.buffer.write(pdf.read_bytes())
except Exception:
	print((dest / 'stdout').read_text(), file = sys.stderr)
	raise RuntimeError("Failed to generate PDF")
finally:
	shutil.rmtree(dest)
