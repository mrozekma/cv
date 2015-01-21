from Terminal import Terminal

@get('')
def cv(handler):
	str = """
This is a *test*!

  * List element
  * *Second* *element*
  * [This is a long link to **Google**](http://www.google.com/)

Last line"""

	term = Terminal(handler)
	term.printText(str, "term.prompt(function() {console.log('yay');});")

	print term
