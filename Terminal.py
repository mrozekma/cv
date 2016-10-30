from bleach import clean
from datetime import datetime
import re

from rorn.ResponseWriter import ResponseWriter

separator = object()

class Terminal:
	def __init__(self, *prompt):
		self.prompt = prompt
		self.files = []
		self.subpages = []
		self.interstitial = None

	def add(self, url, path, typeBits, mtime, description = None):
		if not isinstance(mtime, datetime):
			mtime = datetime.utcfromtimestamp(mtime)
		self += {'url': url, 'path': path, 'typeBits': typeBits, 'mtime': mtime, 'description': description}

	def addSeparator(self):
		self.files.append(separator)

	def setInterstitial(self, interstitial):
		self.interstitial = interstitial

	def __iadd__(self, file):
		if set(file.keys()) != {'url', 'path', 'typeBits', 'mtime', 'description'}:
			raise ValueError("Bad 'file' struct")
		self.files.append(file)
		return self

	@staticmethod
	def renderMTime(mtime):
		rtn = mtime.strftime('%b')
		rtn += " %s" % re.sub('^0', ' ', mtime.strftime('%d'))
		if mtime.year == datetime.now().year:
			rtn += " %s" % mtime.strftime('%H:%M')
		else:
			rtn += "  %s" % mtime.strftime('%Y')
		return rtn

	def __str__(self):
		w = ResponseWriter()
		print "<div class=\"terminal\">"
		for prompt in self.prompt:
			print "<div class=\"prompt\">%s</div>" % prompt
		print "<div class=\"stdout\">"
		print "total %dk" % ((len(self.files) + 2) * 4)
		latestMTime = max(file['mtime'] for file in self.files if not (file is separator)) if self.files else datetime.utcfromtimestamp(0)
		print "<div class=\"file_entry\">drwxr-xr-x   2 mrozekma mrozekma  4.0K %s <a href=\"#\">.</a></div>" % (Terminal.renderMTime(latestMTime))
		print "<div class=\"file_entry\">drwxr-xr-x   2 mrozekma mrozekma  4.0K %s <a href=\"..\">..</a></div>" % (Terminal.renderMTime(latestMTime))
		for file in self.files:
			if file is separator:
				print "<div class=\"separator\"></div>"
				continue
			path = clean(file['path'])
			permBits = 'rws' if 's' in file['typeBits'] else 'rwx'
			permBits += ''.join(c if c in file['typeBits'] else '-' for c in 'rwx')
			permBits += permBits[-3:]
			if 'd' in file['typeBits']:
				print "<div class=\"file_entry\">d%s   2 mrozekma mrozekma  4.0K %s <a href=\"%s\">%s</a>" % (permBits, Terminal.renderMTime(file['mtime']), file['url'], path),
			else:
				# Not sure if I'm willing to put in the effort to show real file size here
				print "<div class=\"file_entry\">-%s   1 mrozekma mrozekma     0 %s <a href=\"%s\">%s</a>" % (permBits, Terminal.renderMTime(file['mtime']), file['url'], path),
			if file['description'] is not None:
				print "%s<div class=\"description\">%s</div>" % (' ' * max(0, 20 - len(path)), clean(file['description'])),
			print "</div>"
		print "</div>"
		if self.interstitial:
			print self.interstitial
		for subpage in self.subpages:
			print "<div class=\"subpage\">"
			subpage()
			print "</div>"
		print "<div class=\"end\"></div>"
		print "</div>"
		return w.done()

	def subpage(self, path, mtime, description = None, catName = None):
		def fn(real_handler):
			safe_path = clean(path)
			self.add("#%s" % safe_path, path, 'r', mtime, description)
			def wrapper_handler():
				print "<a name=\"%s\"></a>" % safe_path
				print "<div class=\"prompt\"><a href=\"#%s\">cat %s</a></div>" % (safe_path, catName or safe_path)
				print "<div class=\"stdout\">"
				try:
					return real_handler()
				finally:
					print "</div>"
			self.subpages.append(wrapper_handler)
			return wrapper_handler
		return fn
