@get('resume')
def resume(handler, raw = False):
	handler.wrappers = not raw

	print "<div class=\"resume\">"
	print "<div class=\"personal-info\">"
	print "<div class=\"name\">Michael A. Mrozek</div>"
	print "<div class=\"pair\">"
	print "<div class=\"address\">680 Matthew Street, West Lafayette, Indiana 47906</div>"
	print "<div class=\"phone\">(440) 332-3537</div>"
	print "</div>"
	print "<div class=\"pair\">"
	print "<div class=\"email\">work@mrozekma.com</div>"
	print "<div class=\"web\">http://resume.michaelmrozek.com/</div>"
	print "</div>"
	print "</div>"

	print "<div class=\"section\">"
	print "<div class=\"title\">Areas of Expertise</div>"
	print "With a proven track record of success both academically and professionally, my diverse skills and experience enable me to contribute in many key areas:<br><br>"
	print
	print "<table>"
	print "<tr><td>Languages</td><td>Extensive experience in C++, Python, and Java. Familiar with many other languages, including PHP, HTML, CSS, Javascript/jQuery, and more.</td></tr>"
	print "<tr><td>Operating Systems</td><td>Adept with Linux and modern versions of Windows.</td></tr>"
	print "<tr><td>Database Systems</td><td>Well-versed in SQL, and familiar with many database systems, including MySQL, PostgreSQL, and SQLite.</td></tr>"
	print "<tr><td>Certifications</td><td>Certified in <b>Comptia A+</b> hardware repair as well as a former CCNA</td></tr>"
	print "</table>"

	print "</div>"
	print "</div>"
