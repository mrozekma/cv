from collections import OrderedDict
from datetime import datetime

from Terminal import Terminal

@get('', statics = 'cv')
def cv(handler):
	term = Terminal('ls -lar --sort=relevance')
	#        url                  path                 typeBits    mtime       description
	term.add('work_history',      'work_history',      'drx',      1477259577, "The places I've worked and the things I did while I was there")
	term.add('personal_projects', 'personal_projects', 'drx',      1477259577, "Things nobody paid me to do. Much more interesting, on the whole")
	term.add('education',         'education',         'drx',      1431910800, "How did I learn how to do all these things?")
	term.add('publications',      'publications',      'drx',      1196560800, "That time my thoughts were permanently recorded and shared with others")
	term.add('hobbies',           'hobbies',           'drx',      1477259577, "Occasionally I'm not at my computer")
	term.addSeparator()
	term.add('make-pdf-resume',   'make-pdf-resume',   'xs',       1477259577, "This page isn't particularly printer-friendly")
	print term
