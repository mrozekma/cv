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
	with ResponseWriter() as w:
		print("<br>")
		print("<div class=\"prompt\">ls -lrt by-level/</div>")
		print("<div class=\"stdout\">")
		print(f"total {len(symlinks) * 4}k")
		for school, (level, mtime) in symlinks.items():
			ln = "../by-school/%s" % school
			mtime = Terminal.renderMTime(datetime.utcfromtimestamp(mtime))
			print(f"<div class=\"file_entry\">lrwxr-xr-x   1 mrozekma mrozekma  {len(ln):2d} {mtime} <a class=\"symlink\" href=\"#{school}\">{level}</a> -> <a href=\"#{school}\">{ln}</a></div>")
		print("</div>")
		term.setInterstitial(w.done())

	# Output everything
	print(term)

def subpage(school, level, mtime, url, logo, degree, timeframe):
	symlinks[school] = (level, mtime)
	def fn(real_handler):
		@term.subpage(school, mtime, catName = f"by-school/{school}")
		def fn2():
			print("<div class=\"school\">")
			if url is not None:
				sys.stdout.write(f"<a target=\"_blank\" href=\"{url}\">")
			sys.stdout.write(f"<img class=\"logo\" src=\"/static/images/education/{logo}\">")
			if url is not None:
				sys.stdout.write("</a>")
			print()
			print("<div class=\"degree\">%s</div>" % ('<br>'.join(degree) if isinstance(degree, tuple) else degree))
			print(f"<div class=\"timeframe\">{timeframe}</div>")
			print("<br>")
			real_handler()
			print("</div>")
		return fn2
	return fn

@subpage('purdue', "master's", 1431882000, 'https://purdue.edu/', 'purdue.png', 'Master of Science in Computer Science', '2011 - 2015')
def purdue():
	print("Continuing education while employed at <a href=\"/work-history#microsemi\">Microsemi</a><br>")
	print("Cumulative GPA: <em>3.67</em><br>")
	print("Courses:")
	print("<ul>")
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
	courses.sort(key = lambda id_semester_name: id_semester_name[0])
	for id, semester, name in courses:
		print(f"<li><a target=\"_blank\" href=\"https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in={semester}&subj_code_in=CS&crse_numb_in={id}00\"><em>CS{id}</em> {clean(name)}</a></li>")
	print("</ul>")

@subpage('rose-hulman', "bachelor's", 1245085200, 'https://rose-hulman.edu/', 'rose-hulman.png', 'Bachelor of Science in Computer Science and Software Engineering', '2005 - 2009')
def rose():
	print("Cum Laude<br>")
	print("Cumulative GPA: <em>3.48</em>&nbsp;&nbsp;&nbsp;&nbsp;Upperclass GPA: <em>3.70</em>")
	pass #TODO

@subpage('perry', "high_school", 1118854800, 'http://www.perry-lake.k12.oh.us/', 'perry.png', 'High School', '2005 - 2009')
def perry():
	print("Graduate with Honors<br>")
	print("Class rank: 3<br>")
	print("National AP Scholar with Distinction")
