from Terminal import Terminal

import sys

term = Terminal('cd /work_history', 'ls -lart **/*')

@get('work_history', statics = 'work')
def work(handler):
	handler.title('Work History', 'work_history')
	print term

@term.subpage('README.1ST', 1477280113)
def background():
	print "<br>"
	print "My work history is slightly confusing because of a series of company splits and acquisitions. The short version is that I've worked at the same place since my <a href=\"#arxan\">2008 internship</a>, despite the regular name changes:"
	print "<ul>"
	print "<li><div class=\"timeframe\">??? 2008</div> Arxan splits into Arxan Defense Systems and Arxan Technologies</li>" # //NO Figure out month
	print "<li><div class=\"timeframe\">Sep 2010</div> Arxan Defense Systems is acquired by Microsemi<a class=\"cite\" href=\"http://investor.microsemi.com/2010-09-15-Microsemi-Corporation-Acquires-Arxan-Defense-Systems-Inc\"></a></li>"
	print "<li><div class=\"timeframe\">May 2016</div> The security division of Microsemi is acquired by Mercury Systems<a class=\"cite\" href=\"https://www.mrcy.com/presscenter/pressreleases/pressrelease.aspx?id=16578\"></a></li>"
	print "</ul>"
	print "The jobs predating this all took place during undergraduate or high school (and are stored in the <code>pre-graduation</code> folder)."

class jobTemplate:
	def __init__(self, url, logo, title, timeframe):
		self.url = url
		self.logo = logo
		self.title = title
		self.timeframe = timeframe

	def __enter__(self):
		print "<div class=\"job\">"
		if self.url is not None:
			sys.stdout.write("<a target=\"_blank\" href=\"%s\">" % self.url)
		sys.stdout.write("<img class=\"logo\" src=\"/static/images/%s\">" % self.logo)
		if self.url is not None:
			sys.stdout.write("</a>")
		print
		print "<div class=\"title\">%s</div>" % ('<br>'.join(self.title) if isinstance(self.title, tuple) else self.title)
		print "<div class=\"timeframe\">%s</div>" % self.timeframe

	def __exit__(self, excType, excValue, traceback):
		print "</div>"

@term.subpage('mercury', 1477280113)
def mercury():
	with jobTemplate('https://www.mrcy.com/', 'mercury.png', 'Software Development Engineer', '2016 - Present'):
		pass #TODO

@term.subpage('microsemi', 1462881600)
def microsemi():
	with jobTemplate('http://www.microsemi.com/', 'microsemi.png', 'Software Developer', '2010 - 2016'):
		pass #TODO

@term.subpage('arxan_defense_systems', 1289390400)
def ads():
	with jobTemplate(None, 'arxan_defense_systems.png', 'Software Security Analyst', '2009 - 2010'):
		pass #TODO

@term.subpage('pre-graduation/arxan', 1245672000)
def arxan():
	with jobTemplate(None, 'arxan.png', 'Intern', '2008 - 2009'):
		pass #TODO

@term.subpage('pre-graduation/ventures', 1212148800)
def ventures():
	with jobTemplate('http://www.rhventures.org/', 'ventures.png', 'Team Lead', '2007 - 2008'):
		pass #TODO

@term.subpage('pre-graduation/rose-hulman', 1244635200)
def ventures():
	with jobTemplate('http://www.rose-hulman.edu/', 'rose-hulman.png', ('Teaching Assistant', 'CSSE Newsletter Editor'), '2005 - 2008'):
		pass #TODO

@term.subpage('pre-graduation/perry_schools', 1180612800)
def perry():
	with jobTemplate('http://www.perry-lake.k12.oh.us/', 'perry.png', ('Website Designer', 'Technician', 'Database Administrator'), '2001 - 2007'):
		pass #TODO

@term.subpage('pre-graduation/perritech', 1117540800)
def perry():
	with jobTemplate(None, 'perritech.png', ('President', 'Technician'), '2001 - 2005'):
		pass #TODO
