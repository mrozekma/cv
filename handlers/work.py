from Terminal import Terminal

import markdown
import sys

term = Terminal('cd /work_history', 'ls -lart **/*')

@get('work_history', statics = 'work')
def work(handler):
	handler.title('Work History', 'work_history')
	print(term)

@term.subpage('README.1ST', 1477280113)
def background():
	print("<br>")
	print("My work history is slightly confusing because of a series of company splits and acquisitions. The short version is that I've worked at the same place since my <a href=\"#arxan\">2008 internship</a>, despite the regular name changes:")
	print("<ul>")
	print("<li><div class=\"timeframe\">Oct 2008</div> Arxan splits into Arxan Defense Systems and Arxan Technologies</li>")
	print("<li><div class=\"timeframe\">Sep 2010</div> Arxan Defense Systems is <a target=\"_blank\" href=\"http://investor.microsemi.com/2010-09-15-Microsemi-Corporation-Acquires-Arxan-Defense-Systems-Inc\">acquired</a> by Microsemi</li>")
	print("<li><div class=\"timeframe\">May 2016</div> The security division of Microsemi is <a target=\"_blank\" href=\"https://www.mrcy.com/presscenter/pressreleases/pressrelease.aspx?id=16578\">acquired</a> by Mercury Systems</li>")
	print("</ul>")
	print("The jobs predating this all took place during undergraduate or high school (and are stored in the <code>pre-graduation</code> directory).")

def subpage(path, mtime, url, logo, title, timeframe):
	def fn(real_handler):
		@term.subpage(path, mtime)
		def fn2():
			print("<div class=\"job\">")
			if url is not None:
				sys.stdout.write("<a target=\"_blank\" href=\"%s\">" % url)
			sys.stdout.write("<img class=\"logo\" src=\"/static/images/work/%s\">" % logo)
			if url is not None:
				sys.stdout.write("</a>")
			print()
			print("<div class=\"title\">%s</div>" % (', '.join(title) if isinstance(title, tuple) else title))
			print("<div class=\"timeframe\">%s</div>" % timeframe)
			print("<br>")
			print(markdown.markdown(real_handler(), extensions = []))
			print("</div>")
		return fn2
	return fn

@subpage('mercury', 1532302550, 'https://www.mrcy.com/', 'mercury.png', 'Software Development Engineer', '2016 - Present')
def mercury():
	return '''
* Designed and rolled out an automated build and test system for a number of projects.
* Handled the office migration to Atlassian tools, including moving all projects from Subversion to Bitbucket.
    - Implemented a [tool](/personal_projects#got) to manage cross-repository dependencies in Bitbucket, and an [addon](https://marketplace.atlassian.com/apps/1218193/project-fields) to track additional project information within Bitbucket.
* Fully automated a recurring task needed by a customer, so it can now be done on demand in about 90 minutes
* Fixed and redesigned large portions of an embedded system of interconnected Microblaze cores used by many customers
'''

@subpage('microsemi', 1462881600, 'http://www.microsemi.com/', 'microsemi.png', 'Software Developer', '2010 - 2016')
def microsemi():
	return '''
* Implemented and improved miscellaneous whitebox cryptography algorithms, including RSA, AES, and elliptic curve DSA.
* Developed an OpenSSL engine wrapping our whitebox cryptography implementations so they could be used transparently by any application that uses OpenSSL.
* Implemented the security model and key management policy for an Android password manager.
* Designed and implemented multiple higher level protocols wrapping existing whitebox cryptography to satisfy customer needs.
* <span title="A security assessment performed without the customer's help, mimicking the situation a real attacker would be in.">Red-</span> and <span title="A security assessment performed with the customer's help, including access to background information, design documents, and possibly even source code.">blue-teamed</span> several devices, finding a number of vulnerabilities. Wrote large portions of the final reports detailing the vulnerabilities, their severity, and potential mitigations and fixes.
'''

@subpage('arxan_defense_systems', 1289390400, None, 'arxan_defense_systems.png', 'Software Security Analyst', '2009 - 2010')
def ads():
	return '''
* Implemented many features in [CodeSEAL](http://www.microsemi.com/products/information-assurance/softwareanti-tamper/codeseal), a product that analyzes executables and modifies them to protect against reverse engineering or modification.
* Developed [WhiteboxRSA](http://www.microsemi.com/products/information-assurance/cryptography/whiteboxcrypto), an RSA implementation that hides the key to frustrate recovery even when the implementation is fully under the attacker's control.
'''

@subpage('pre-graduation/arxan', 1245672000, None, 'arxan.png', 'Intern', '2008 - 2009')
def arxan():
	return '''
* Engineering intern on a team that developed *TransformIT*, a white box cryptography solution.
* Subsequently accepted an opportunity to continue work remotely during the school year before transitioning to full-time employment after graduation.
'''

@subpage('pre-graduation/ventures', 1212148800, 'http://www.rhventures.org/', 'ventures.png', 'Team Lead', '2007 - 2008')
def ventures():
	return '''
* Head of a team of students that specified, designed, developed and launched the web portal for a promising online startup company.
* Handled maintenance of development servers and software.
* Maintained source code repository and bug tracking system.
* Reviewed code produced by other team members.
'''

@subpage('pre-graduation/rose-hulman', 1244635200, 'http://www.rose-hulman.edu/', 'rose-hulman.png', ('Teaching Assistant', 'CSSE Newsletter Editor'), '2005 - 2008')
def roseHulman():
	return '''
* Assisted students in many introductory programming classes with fundamental object-oriented techniques, UML, project planning, and completing team-based goals.
* Responsible for all phases of the CSSE newsletter production, from writing to publishing.
'''

@subpage('pre-graduation/perry_schools', 1180612800, 'http://www.perry-lake.k12.oh.us/', 'perry.png', ('Website Designer', 'Technician', 'Database Administrator'), '2001 - 2007')
def perry():
	return '''
* Project coordinator that designed and implemented a completely new look and feel for the school district's 5000+ page website, including a custom CMS and DB design.
* Converted all existing webpages to a new format and implemented a new, more efficient interface.
* Designed, implemented, and maintained the school's first online course registration system.
'''

@subpage('pre-graduation/perritech', 1117540800, None, 'perritech.png', ('President', 'Technician'), '2001 - 2005')
def perritech():
	return '''
* Recruited in 2001 as a computer technician, responsible for the 2000+ computer network.
* Subcontracted to various local businesses for programming, website design, networking and system administration.
* Promoted to President in 2005, managing four directors and a number of technicians.
* Spearheaded a presentation at the Ohio State SchoolNet Convention illustrating the benefits of a student-run technology company fully executed within a school district. Subsequently invited to Seoul, Korea for the 6th Global Forum to make a detailed presentation on how to duplicate our success throughout many school districts.
'''
