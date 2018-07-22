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
		latestMTime = max(file['mtime'] for file in self.files if not (file is separator)) if self.files else datetime.utcfromtimestamp(0)

		def printEntry(isDir, permBits, mTime, url, name, description):
			# Not sure if I'm willing to put in the effort to show real file size here
			dirBit, numLinks, sizeStr = ('d', 2, '4.0K') if isDir else ('-', 1, '   0')
			mTimeStr = Terminal.renderMTime(mTime)
			print(f"<div class=\"file_entry\"><div class=\"metadata\">{dirBit}{permBits}   {numLinks} mrozekma mrozekma  {sizeStr} {mTimeStr} </div><a href=\"{url}\">{name}</a>", end = '')
			if description is not None:
				if (len(path) < 20):
					print(' ' * (20 - len(path)), end = '')
					print(f"<div class=\"description\">{clean(description)}</div>", end = '')
			print("</div>")

		w = ResponseWriter()
		try:
			print("<div class=\"terminal\">")
			print("<div class=\"prompt mobile\">export LAYOUT=mobile</div>")
			for prompt in self.prompt:
				print("<div class=\"prompt\">%s</div>" % prompt)
			print("<div class=\"stdout\">")
			print(f"total {(len(self.files) + 2) * 4}k")
			printEntry(True, 'rwxr-xr-x', latestMTime, '#', '.', None)
			printEntry(True, 'rwxr-xr-x', latestMTime, '..', '..', None)
			for file in self.files:
				if file is separator:
					print("<div class=\"separator\"></div>")
					continue
				path = clean(file['path'])
				permBits = 'rws' if 's' in file['typeBits'] else 'rwx'
				permBits += ''.join(c if c in file['typeBits'] else '-' for c in 'rwx')
				permBits += permBits[-3:]
				printEntry('d' in file['typeBits'], permBits, file['mtime'], file['url'], path, file['description'])
			print("</div>")
			if self.interstitial:
				print(self.interstitial)
			for subpage in self.subpages:
				print("<div class=\"subpage\">")
				subpage()
				print("</div>")
			print("<div class=\"end\"></div>")
			print("</div>")
		finally:
			rtn = w.done()
		return rtn

	def subpage(self, path, mtime, description = None, catName = None):
		def fn(real_handler):
			safePath = clean(path)
			self.add(f"#{safePath}", path, 'r', mtime, description)
			def wrapper_handler():
				print(f"<a name=\"{safePath}\"></a>")
				print(f"<div class=\"prompt\"><a href=\"#{safePath}\">cat {catName or safePath}</a></div>")
				print("<div class=\"stdout\">")
				try:
					return real_handler()
				finally:
					print("</div>")
			self.subpages.append(wrapper_handler)
			return wrapper_handler
		return fn
