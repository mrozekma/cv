from Photoswipe import Photoswipe
from Terminal import Terminal

from rorn.Lock import SingleLock as Lock
from rorn.ResponseWriter import ResponseWriter

import sys

term = Terminal('cd /personal_projects', 'ls -lar --sort=relevance')
termLock = Lock()
allTags = set()

# @get('personal_projects', statics = ['projects'])
@get('personal_projects', statics = ['projects', 'bootstrap'] + Photoswipe.getStatics())
def projects(handler, tags = None):
	handler.title('Personal Projects', 'personal_projects')
	print Photoswipe.getRootElement()

	# Generate the list of level -> school symlinks. This is drawn between the regular list and the individual subpages
	w = ResponseWriter()
	try:
		print "<br>"
		print "<div class=\"prompt\">~/bin/show-project-filters --all --clickable</div>"
		print "<div class=\"stdout project-tags\">"
		for tag in sorted(allTags):
			sys.stdout.write("<span class=\"label label-default\">%s</span>" % tag)
		print
		print "</div>"
	finally:
		term.setInterstitial(w.done())

	# Output everything
	# This is super gross, but it's still happening -- storing the filter data on 'term' for the length of the print, which means it needs a lock since 'term' is global
	with termLock as l:
		term.tags = tags.split(' ') if tags else []
		try:
			print term
		finally:
			del term.tags

def subpage(project, name, tagline, mtime, screenshotSpec, tags, repo = None):
	allTags.update(tags)

	def fn(real_handler):
		@term.subpage(project, mtime)
		def fn2():
			print "<div class=\"name\">%s</div>" % name
			print "<div class=\"tagline\">%s</div>" % tagline
			print "<div class=\"project-filters\">"
			for tag in tags:
				print "<span class=\"label label-default\">%s</span>" % tag
			print "</div>"
			if repo:
				print "<a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/%s\"><i class=\"fa fa-lg fa-github\"></i>&nbsp;Github repository</a>" % repo
			print Photoswipe.fromSpec(screenshotSpec)
			print "<div class=\"description\">"
			real_handler()
			print "</div>"
		return fn2
	return fn

@subpage('sprint', 'Sprint', 'scrum tracking tool', 1308373920, 'static/images/projects/sprint/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket'], 'sprint')
def sprint():
	print "The <em>Sprint tool</em>, as it came to be known when I forgot to come up with a real name, is a web-based <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Scrum_(software_development)\">Scrum</a> tracking tool. I wrote it largely in 2011-2012 in my free time for use at <a target=\"_blank\" href=\"/work_history#microsemi\">Microsemi</a>. Its predecessor was an Excel spreadsheet filled with formulas and custom cell formatting that tended to slowly degenerate as it was copied from sprint to sprint until the metrics it reported bore little resemblance to the actual hours entered into the cells. While the Sprint tool was originally written just for internal use at my company, former coworkers have carried it with them to at least three other companies that I know of. This was relatively painless, once a few <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b0ac62a97c28b871c4853686bda6426060eb7a90\">poorly-conceived</a> <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b6b1af214e77de7b6680d565aeddfebce00c1385\">hardcoded-values</a> were fixed.<br><br>"
	print "The Sprint tool is also noteworthy as my first Python webapp, as my previous web work was in PHP. It contained a custom web framework on top of Python's built-in <a target=\"_blank\" href=\"https://docs.python.org/2/library/basehttpserver.html\">HTTP server</a>; this framework has since been pulled out into its <a href=\"#rorn\">own project</a> so I could use it on <a href=\"#spades\">other webapps</a>, including <a target=\"_blank\" href=\"https://github.com/mrozekma/cv\">this very site</a>."

@subpage('noisebot', 'Noisebot', 'chat bot', 1277020414, 'static/images/projects/noisebot/spec', ['java', 'irc', 'slack'], 'noisebot')
def noisebot():
	# IRC: Choose, Help, Poll, Weather, Wikipedia, Wolfram, Youtube
	# Slack: EmojiRace, LaTeXMath, Wikipedia, Youtube
	print "<em>Noisebot</em> originated as a fairly simple collection of Python scripts to provide useful functions for use in the IRC channel populated by the Linux Users Group I belonged to in <a target=\"_blank\" href=\"/education#rose-hulman\">undergrad</a>. It was later rewritten in Java and expanded to support Slack. Unlike other chat bots, Noisebot was designed from the ground up to be <a target=\"_blank\" href=\"https://github.com/mrozekma/noisebot#developer-documentation\">easily updatable by anyone</a>. When a new commit is pushed to the repository, it is automatically validated and then deployed to Github. Running bots are alerted to the change and synchronize automatically, reloading affected modules without restarting. This ease of updating makes Noisebot the only project on this page with a non-trivial number of <a target=\"_blank\" href=\"https://github.com/mrozekma/NoiseBot/graphs/contributors\">contributors</a>."

# https://www.youtube.com/watch?v=l98orlySZZA

@subpage('spades', 'Spades', 'web-based cards interface', 1446781016, 'static/images/projects/spades/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket'], 'spades')
def spades():
	pass

'''
sprint
noisebot
spades
rorn
gir
helm
taut?
arxantv
pytypecheck
woop (browser)
cv
pytypecheck

test_dispatcher
launchpad
'''
