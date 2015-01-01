from datetime import datetime
import sys

def console(source, fmt, *args):
	str = fmt
	if args:
		str %= args
	sys.__stdout__.write("[%s] [%s] %s\n" % (datetime.now().replace(microsecond = 0), source, str))
