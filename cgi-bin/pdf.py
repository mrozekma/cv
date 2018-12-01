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
dest = tempfile.mkdtemp(prefix = 'cv-tmp')
try:
	subprocess.run(['xelatex', '-halt-on-error', '-output-directory', dest, '-jobname', 'resume', r'\input{prolog}'] + [fr"\usetag{{{entry}}}" for entry in entries] + [r'\input{resume}'], cwd = rootDir / 'tex', stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)
	print("Content-type: application/pdf\n")
	sys.stdout.flush()
	pdf = Path(dest) / 'resume.pdf'
	sys.stdout.buffer.write(pdf.read_bytes())
except FileNotFoundError:
	raise RuntimeError("Failed to generate PDF")
finally:
	shutil.rmtree(dest)
