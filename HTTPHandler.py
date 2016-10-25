from os.path import isfile
import sys

from Log import console
from wrappers import header, footer

from rorn.HTTPHandler import HTTPHandler as ParentHandler
from rorn.ResponseWriter import ResponseWriter

def ensureList(l):
	return l if isinstance(l, list) else [l]

class HTTPHandler(ParentHandler):
	def __init__(self, request, address, server):
		self.wrappers = True
		self.wrapperData = {'jsOnReady': []}
		self.localData = {}
		ParentHandler.__init__(self, request, address, server)

	def log_message(self, fmt, *args):
		console('rorn', "%s - %s", self.address_string(), fmt % args)

	def preprocessQuery(self, query):
		if 'raw' in query:
			self.wrappers = False
			del query['raw']
		return query

	def invokeHandler(self, handler, query):
		handler['fn'](handler = self, **query)

	def requestDone(self):
		if self.wrappers:
			types = ['less', 'css', 'js']
			includes = {type: [] for type in types}
			handler = getattr(self, 'handler', None)
			if handler and 'statics' in handler:
				for key in ensureList(handler['statics']):
					for type in types:
						if isfile("static/%s.%s" % (key, type)):
							includes[type].append("/static/%s.%s" % (key, type))

			writer = ResponseWriter()
			header(self, includes)
			sys.stdout.write(self.response)
			footer(self)
			self.response = writer.done()

	def title(self, title, path = None):
		if title is None:
			self.pagePath = ''
			self.pageTitle = 'Michael Mrozek'
			self.pageSubtitle = ''
		else:
			self.pagePath = path or title
			self.pageSubtitle = title
			self.pageTitle = self.pageSubtitle + " - Michael Mrozek"

	def jsOnReady(self, js):
		self.wrapperData['jsOnReady'].append(js)

from handlers import *
