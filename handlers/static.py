from __future__ import with_statement
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
		'png': 'image/png',
		'svg': 'image/svg+xml'
	}

	if not isfile("static/" + filename):
		return handler.error("Invalid static argument", "Static resource <b>%s</b> does not exist" % clean(filename))
	if not realpath("static/" + filename).startswith(realpath("static")):
		return handler.error("Invalid static argument", "Static resource <b>%s</b> is not allowed" % clean(filename))

	ext = filename[filename.rfind('.')+1:]
	if ext in types:
		handler.contentType = types[ext]

	with open("static/" + filename) as f:
		sys.stdout.write(f.read())
