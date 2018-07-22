from datetime import datetime
import sys

def console(source, fmt, *args):
	str = fmt
	if args:
		str %= args
	when = datetime.now().replace(microsecond = 0)
	sys.__stdout__.write(f"[{when}] [{source}] {str}\n")
