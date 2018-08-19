from textwrap import dedent

from rorn import code

from Terminal import Terminal

@get('', statics = 'cv')
def cv(handler):
	term = Terminal('ls -lar --sort=relevance')
	#        url                  path                 typeBits    mtime       description
	term.add('work_history',      'work_history',      'drx',      1477259577, "The places I've worked and the things I did while I was there")
	term.add('personal_projects', 'personal_projects', 'drx',      1477259577, "Things nobody paid me to do. Much more interesting, on the whole")
	term.add('education',         'education',         'drx',      1431910800, "Where I learned to do the above things")
	term.add('publications',      'publications',      'drx',      1196560800, "Journal articles. Well, article")
	term.add('hobbies',           'hobbies',           'drx',      1477259577, "Occasionally I'm not at my computer")
	term.addSeparator()
	term.add('make-pdf-resume',   'make-pdf-resume',   'xs',       1477259577, "This page isn't particularly printer-friendly")
	print(term)

@get('code.css')
def codeCSS(handler):
        handler.wrappers = False
        handler.contentType = 'text/css'
        code.showCodeCSS()

		# Override a few things
        print(dedent("""
        .code_default { border-spacing: 0; }
        .code_default.light { color: #000; }
        .selected_line { background-color: #aa0000aa; }
        """))
