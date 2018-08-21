from Terminal import Terminal

import markdown
import sys

term = Terminal('cd /publications', 'ls -lart **/*')

@get('publications', statics = 'publications')
def publications(handler):
	handler.title('Publications', 'publications')
	print(term)

@term.subpage('SupportingCS1.pdf', 1173268800, 'Subverting the fundamentals sequence')
def supportingCS1():
	print("<br><a href=\"/static/papers/SupportingCS1.pdf\" target=\"_blank\"><img class=\"pdf\" src=\"/static/papers/SupportingCS1.png\"></a><br><br>")
	print("A paper about a pilot program I assisted with while a teaching assistant. The class used individual subversion repositories to manage student assignments: new assignments were committed by the professor, the work was committed by the students, and the grades were committed by me.<br><br>")
	print("Submitted to the Special Interest Group on Computer Science Education (SIGCSE) and presented at the Annual Technical Symposium.")
