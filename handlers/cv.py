from Terminal import Terminal

@get('')
def cv(handler):
	intro = """
Hello!

All the parts of my resume and portfolio are accessible through this CLI (I suggest starting with [[help]]).
If the command-line interface doesn't amuse you, you can [[startx|disable it]].
"""

	term = Terminal(handler)
	term.printText(intro, "term.prompt();")

	print term
