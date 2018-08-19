from bleach import clean
from functools import lru_cache
import re
import shutil
import subprocess
import sys
import tempfile
from textwrap import dedent

from rorn.utils import basePath

sections = [
	'Technical Skills', [
		'Languages',
		'Tools and Frameworks',
	],
	'Experience', [
		'Mercury',
		'Microsemi',
		'Arxan Defense Systems',
		'-Arxan',
		'-Rose-Hulman',
		'-Ventures',
		'-Perry Schools',
		'-Perritech',
	],
	'Education', [
		'Masters',
		'Bachelors',
		'-High School',
	],
	'Projects', [
		'Sprint',
		'Noisebot',
		'Spades',
		'Got',
		'Lync Helper',
		'Gir',
		'-Woop',
	],
	'Publications', [
		'-Subverting the Fundamentals Sequence',
	],
	# Hobbies?
]

@lru_cache(maxsize = None)
def textToName(text):
	# Foo Bar Baz -> foo-bar-baz
	ret = text.lower()
	if ret.startswith('-'):
		ret = ret[1:]
	ret = re.sub('[^a-z0-9]+', '-', ret)
	ret = re.sub('-+$', '', ret)
	return ret

leafNames = {textToName(name) for l in sections for name in l if isinstance(l, list)}
leafDefaults = {textToName(name) for l in sections for name in l if isinstance(l, list) and not name.startswith('-')}
leafParents = {textToName(name): textToName(parent) for (parent, l) in zip(sections, sections[1:]) for name in l if isinstance(l, list)}

@get('make-pdf-resume', statics = 'pdf')
def pdfMenu(handler):
	handler.title('PDF', 'make-pdf-resume')

	print(dedent("""
	<div class="terminal">
	<div class="prompt">/make-pdf-resume --help</div>
	<div class="stdout"><br>
	This tool generates a PDF containing a more traditional resume. Which sections to include and omit can be customized as desired, but the default values are sane and have been chosen to fit within a single page.<br><br>
	<small>Thanks to Byungjin Park for the use of the <a href="https://github.com/posquit0/Awesome-CV">Awesome CV</a> document class.</small>
	</div>
	<br>
	<div class="prompt">export NCURSES=1</div>
	<div class="prompt">/make-pdf-resume</div>
	<div class="pdf-generator">
	<div class="title"><input type="checkbox">&nbsp;PDF Generator</div>
	"""))

	def chkList(l):
		for text in l:
			if isinstance(text, list):
				print("<ul>")
				chkList(text)
				print("</ul>")
			else:
				checked = True
				if text.startswith('-'):
					checked = False
					text = text[1:]
				name = textToName(text)
				print(f"""</li><li><input type="checkbox" id="chk-{name}" name="{name}"{' checked' if checked else ''}>&nbsp;<label for="chk-{name}">{clean(text)}</label></input>""")

	print(dedent("""
	<form action="resume.pdf">
	<input type="hidden" name="background" value="on"/>
	<ul><li><input type="checkbox" checked disabled>&nbsp;Background
	"""))
	chkList(sections)
	print(dedent("""
	</li></ul>
	<div class="buttons">
	<button id="go-button" type="submit">Go</button>
	<button id="cancel-button">Cancel</button>
	</div>
	<div class="clear"></div>
	</div>
	</div>
	</form>
	"""))

@get('resume.pdf')
def pdfRender(handler, **kw):
	# Pull the selected sections out of 'kw'. If none are selected, use the defaults flagged in the master sections list
	# Thanks to PEP486 for guaranteeing that kw's keys are in the order they were passed in the query
	selections = set(kw.keys()) if kw else leafDefaults

	# Only include leaf sections; filter out parent/invalid sections
	selections &= leafNames

	# Now include parents that have at least one child in the set
	selections |= {leafParents[name] for name in selections}

	dest = tempfile.mkdtemp(prefix = 'cv-tmp')
	try:
		subprocess.run(['xelatex', '-halt-on-error', '-output-directory', dest, '-jobname', 'resume', r'\input{prolog}'] + [fr"\usetag{{{selection}}}" for selection in selections] + [r'\input{resume}'], cwd = f"{basePath()}/tex")
		with open(f"{dest}/resume.pdf", 'rb') as f:
			sys.stdout.write(f.read())
		handler.contentType = 'application/pdf'
		handler.wrappers = False
	except FileNotFoundError:
		raise RuntimeError("Failed to generate PDF")
	finally:
		shutil.rmtree(dest)
