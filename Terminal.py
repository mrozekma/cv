from json import dumps as toJS

from rorn.ResponseWriter import ResponseWriter

def include():
	print "<script src=\"/static/terminal.js\"></script>"
	print "<link rel=\"stylesheet/less\" type=\"text/css\" href=\"/static/terminal.less\">"

termid = 1
class Text:
	def __init__(self, handler, text):
		global termid
		self.handler = handler
		self.text = text
		self.id = "term%d" % termid
		self.after = None
		termid += 1

	def setAfter(self, after):
		self.after = after

	def write(self):
		after = ("function(term) {%s}" % self.after) if self.after else 'undefined'
		self.handler.jsOnReady("var term = new Terminal(%s); term.show(); setTimeout(function() {term.print(%s, %s);}, 2000);" % (toJS(self.id), toJS(self.text), after))
		print "<div id=\"%s\" class=\"terminal text\"><div class=\"terminal cursor blink\"></div></div>" % self.id

	def __str__(self):
		w = ResponseWriter()
		self.write()
		return w.done()

promptid = 1
class Prompt:
	def __init__(self, handler):
		global promptid
		self.handler = handler
		self.id = "prompt%d" % promptid
		promptid += 1

	def write(self):
		print "<div id=\"%s\" class=\"terminal prompt\">$ <div class=\"terminal cursor blink\"></div>" % self.id

	def __str__(self):
		w = ResponseWriter()
		self.write()
		return w.done()
