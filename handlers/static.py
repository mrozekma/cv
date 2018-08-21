
from os.path import isfile, realpath
import sys

from bleach import clean

@get('static/(?P<filename>.+)')
def static(handler, filename, v = None):
	handler.wrappers = False
	handler.log = False

	types = {
		'css': 'text/css',
		'js': 'text/javascript',
		'pdf': 'application/pdf',
		'png': 'image/png',
		'svg': 'image/svg+xml'
	}

	if not isfile("static/" + filename):
		return handler.error("Invalid static argument", f"Static resource <b>{clean(filename)}</b> does not exist")
	if not realpath("static/" + filename).startswith(realpath("static")):
		return handler.error("Invalid static argument", f"Static resource <b>{clean(filename)}</b> is not allowed")

	ext = filename[filename.rfind('.')+1:]
	if ext in types:
		handler.contentType = types[ext]

	with open("static/" + filename, 'rb') as f:
		sys.stdout.write(f.read())
