from Terminal import Text, Prompt

@get('')
def cv(handler):
	str = """
This is a *test*!

  * List element
  * *Second* *element*
  * [This is a long link to **Google**](http://www.google.com/)

Last line"""

	text = Text(handler, str)
	prompt = Prompt(handler)
	text.setAfter("term.hideCursor(); $('#%s').css('display', 'inline');" % prompt.id)

	print text
	print "<br><br>"
	print prompt
