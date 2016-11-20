from Terminal import Terminal

from rorn.ResponseWriter import ResponseWriter

from bleach import clean
from collections import OrderedDict
from datetime import datetime
import sys

term = Terminal('cd /education', 'ls -lart by-school/')
symlinks = OrderedDict()

@get('education', statics = 'education')
def projects(handler):
	handler.title('Education', 'education')

	# Generate the list of level -> school symlinks. This is drawn between the regular list and the individual subpages
	w = ResponseWriter()
	try:
		print "<br>"
		print "<div class=\"prompt\">ls -lrt by-level/</div>"
		print "<div class=\"stdout\">"
		print "total %dk" % ((len(symlinks)) * 4)
		for school, (level, mtime) in symlinks.iteritems():
			ln = "../by-school/%s" % school
			print "<div class=\"file_entry\">lrwxr-xr-x   1 mrozekma mrozekma  %2d %s <a class=\"symlink\" href=\"#%s\">%s</a> -> <a href=\"#%s\">%s</a></div>" % (len(ln), Terminal.renderMTime(datetime.utcfromtimestamp(mtime)), school, level, school, ln)
		print "</div>"
	finally:
		term.setInterstitial(w.done())

	# Output everything
	print term

def subpage(school, level, mtime, url, logo, degree, timeframe):
	symlinks[school] = (level, mtime)
	def fn(real_handler):
		@term.subpage(school, mtime, catName = "by-school/%s" % school)
		def fn2():
			print "<div class=\"school\">"
			if url is not None:
				sys.stdout.write("<a target=\"_blank\" href=\"%s\">" % url)
			sys.stdout.write("<img class=\"logo\" src=\"/static/images/education/%s\">" % logo)
			if url is not None:
				sys.stdout.write("</a>")
			print
			print "<div class=\"degree\">%s</div>" % ('<br>'.join(degree) if isinstance(degree, tuple) else degree)
			print "<div class=\"timeframe\">%s</div>" % timeframe
			print "<br>"
			real_handler()
			print "</div>"
		return fn2
	return fn

@subpage('purdue', "master's", 1431882000, 'https://purdue.edu/', 'purdue.png', 'Master of Science in Computer Science', '2011 - 2015')
def purdue():
	print "Continuing education while employed at <a href=\"/work_history#microsemi\">Microsemi</a><br>"
	print "Cumulative GPA: <em>3.67</em><br>"
	print "Courses:"
	print "<ul>"
	courses = [
		# ID   Semester Name
		( 502, 201120,  'Compiling and Programming Systems'),
		( 536, 201210,  'Data Communication and Computer Networks'),
		( 555, 201220,  'Cryptography'),
		( 503, 201310,  'Operating Systems'),
		( 580, 201320,  'Algorithm Design, Analysis, and Implementation'),
		( 526, 201410,  'Information Security'),
		( 525, 201420,  'Parallel Computing'),
		( 626, 201420,  'Advanced Information Assurance'),
		( 505, 201510,  'Distributed Systems'),
		( 565, 201520,  'Programming Languages'),
	]
	# Sort courses by ID
	courses.sort(key = lambda (id, semester, name): id)
	for id, semester, name in courses:
		print "<li><a target=\"_blank\" href=\"https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=%d&subj_code_in=CS&crse_numb_in=%d00\"><em>CS%d</em> %s</a></li>" % (semester, id, id, clean(name))
	print "</ul>"

@subpage('rose-hulman', "bachelor's", 1245085200, 'https://rose-hulman.edu/', 'rose-hulman.png', 'Bachelor of Science in Computer Science and Software Engineering', '2005 - 2009')
def rose():
	print "Cum Laude<br>"
	print "Cumulative GPA: <em>3.48</em>&nbsp;&nbsp;&nbsp;&nbsp;Upperclass GPA: <em>3.70</em>"
	pass #TODO

@subpage('perry', "high_school", 1118854800, 'http://www.perry-lake.k12.oh.us/', 'perry.png', 'High School', '2005 - 2009')
def perry():
	print "Graduate with Honors<br>"
	print "Class rank: 3<br>"
	print "National AP Scholar with Distinction"
