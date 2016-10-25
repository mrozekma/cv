from Terminal import Terminal

term = Terminal('cd /work_history', 'ls -lart')

@get('work_history', statics = 'work')
def work(handler):
	handler.title('Work History', 'work_history')
	print term

@term.subpage('README.1ST', 1477280113)
def background():
	print "<br>"
	print "My work history is slightly confusing because of a series of company splits and acquisitions. The short version is that I've worked at the same place since my <a href=\"#arxan\">2008 internship</a>, despite the regular name changes."
	print "<ul>"
	print "<li><b>??? 2008</b> Arxan splits into Arxan Defense Systems and Arxan Technologies</li>" # //NO Figure out month
	print "<li><b>Sep 2010</b> Arxan Defense Systems is acquired by Microsemi<a class=\"cite\" href=\"http://investor.microsemi.com/2010-09-15-Microsemi-Corporation-Acquires-Arxan-Defense-Systems-Inc\"></a></li>"
	print "<li><b>May 2016</b> The security division of Microsemi is acquired by Mercury Systems<a class=\"cite\" href=\"https://www.mrcy.com/presscenter/pressreleases/pressrelease.aspx?id=16578\"></a></li>"
	print "</ul>"

@term.subpage('mercury', 1477280113)
def mercury():
	print "<div class=\"job\">"
	print "<img class=\"logo\" style=\"width: 300px\" src=\"/static/images/mercury.png\">"
	print "<div class=\"title\">Software Development Engineer</div>"
	print "<div class=\"timeframe\">2016 - Present</div>"
	print "</div>"
