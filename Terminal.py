from json import dumps as toJS

from rorn.ResponseWriter import ResponseWriter

def include():
	print "<script src=\"/static/third-party/keypress.js\"></script>"
	print "<script src=\"/static/terminal.js\"></script>"
	print "<link rel=\"stylesheet/less\" type=\"text/css\" href=\"/static/terminal.less\">"

class Terminal:
	def __init__(self, handler):
		self.handler = handler
		id = handler.localData['terminal_id'] = handler.localData.get('terminal_id', 0) + 1
		self.id = "term%d" % id

		self.handler.jsOnReady("var %s = new Terminal(%s);" % (self.id, toJS(self.id)))

	def printText(self, text, after = None):
		after = ("function(term) {%s}" % after) if after else 'undefined'
		self.handler.jsOnReady("%s.print(%s, %s);" % (self.id, toJS(text), after))

	def prompt(self, after):
		# 'after' can either be a function name or an anonymous function
		if not after.startswith('function('):
			after = "function(term, command) {%s}" % after
		self.handler.jsOnReady("%s.prompt(%s);" % (self.id, after))

	def write(self):
		print "<div id=\"%s\" class=\"terminal\"></div>" % self.id

	def __str__(self):
		w = ResponseWriter()
		self.write()
		return w.done()
