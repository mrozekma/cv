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
		#TODO Clicking these should toggle showing only projects with those tags
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

def subpage(project, name, tagline, mtime, screenshotSpec, tags, repo = None, production = None):
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
			print "<div class=\"project-links\">"
			if repo:
				print "<a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/%s\"><i class=\"fa fa-lg fa-github\"></i>&nbsp;Github repository</a>" % repo
			if production:
				print "<a class=\"prod-link\" target=\"_blank\" href=\"%s\"><i class=\"fa fa-lg fa-columns\"></i>&nbsp;Live website</a>" % production
			print "</div>"
			pswp = Photoswipe.fromSpec(screenshotSpec)
			print pswp
			print "<div class=\"description\">"
			real_handler(pswp)
			print "</div>"
		return fn2
	return fn

@subpage('sprint', 'Sprint', 'scrum tracking tool', 1308373920, 'static/images/projects/sprint/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket'], 'sprint')
def sprint(_):
	print "The <em>Sprint tool</em>, as it came to be known when I forgot to come up with a real name, is a web-based <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Scrum_(software_development)\">Scrum</a> tracking tool. I wrote it largely in 2011-2012 in my free time for use at <a target=\"_blank\" href=\"/work_history#microsemi\">Microsemi</a>. Its predecessor was an Excel spreadsheet filled with formulas and custom cell formatting that tended to slowly degenerate as it was copied from sprint to sprint until the metrics it reported bore little resemblance to the actual hours entered into the cells. While the Sprint tool was originally written just for internal use at my company, former coworkers have carried it with them to at least three other companies that I know of. This was relatively painless, once a few <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b0ac62a97c28b871c4853686bda6426060eb7a90\">poorly-conceived</a> <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b6b1af214e77de7b6680d565aeddfebce00c1385\">hardcoded-values</a> were fixed.<br><br>"
	print "The Sprint tool is also noteworthy as my first Python webapp, as my previous web work was in PHP. It contained a custom web framework on top of Python's built-in <a target=\"_blank\" href=\"https://docs.python.org/2/library/basehttpserver.html\">HTTP server</a>; this framework has since been pulled out into its <a href=\"#rorn\">own project</a> so I could use it on <a href=\"#spades\">other webapps</a>, including <a target=\"_blank\" href=\"https://github.com/mrozekma/cv\">this very site</a>."

@subpage('noisebot', 'Noisebot', 'chat bot', 1277020414, 'static/images/projects/noisebot/spec', ['java', 'irc', 'slack'], 'noisebot')
def noisebot(_):
	# IRC: Choose, Help, Poll, Weather, Wikipedia, Wolfram, Youtube
	# Slack: EmojiRace, LaTeXMath, Wikipedia, Youtube
	print "<em>Noisebot</em> originated as a fairly simple collection of Python scripts to provide useful functions for use in the IRC channel populated by the Linux Users Group I belonged to in <a target=\"_blank\" href=\"/education#rose-hulman\">undergrad</a>. It was later rewritten in Java and expanded to support Slack. Unlike other chat bots, Noisebot was designed from the ground up to be <a target=\"_blank\" href=\"https://github.com/mrozekma/noisebot#developer-documentation\">easily updatable by anyone</a>. When a new commit is pushed to the repository, it is automatically validated and then deployed to Github. Running bots are alerted to the change and synchronize automatically, reloading affected modules without restarting. This ease of updating makes Noisebot the only project on this page with a non-trivial number of <a target=\"_blank\" href=\"https://github.com/mrozekma/NoiseBot/graphs/contributors\">contributors</a>.<br><br>"
	print "If you're interested in watching me code at 4x speed, I have a video of the development of the <a href=\"https://github.com/mrozekma/NoiseBot/blob/master/src/modules/EmojiRace.java\">EmojiRace module</a>:<br><br>"
	print "<iframe width=\"854\" height=\"480\" src=\"https://www.youtube.com/embed/l98orlySZZA\" frameborder=\"0\" allowfullscreen></iframe>"

@subpage('spades', 'Spades', 'web-based cards interface', 1446781016, 'static/images/projects/spades/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket'], 'spades', 'http://spades.mrozekma.com/')
def spades(pswp):
	idx = pswp.getIndexByPath('game-with-irc')
	print "<em>Spades</em> takes some explanation. Several years ago a friend of mine implemented an IRC bot to let users play the card game <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Spades\">Spades</a>. (He implemented it in AWK, so the <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/Andy753421/rhawk/blob/master/spades.awk\"><i class=\"fa fa-github\"></i>&nbsp;code</a> is worth looking at)."
	print "You can see a short snippet of what the IRC interface looks like in <a class=\"screenshot-link\" data-pswp=\"%s\" data-index=\"%d\" href=\"#\">one of the screenshots</a> above; naturally it is somewhat inefficient." % (pswp.id, idx)
	print "This project is a web-based interface to show current and historical games. It communicates with the game server and with client browsers using websockets, and shows each play as it happens. The complete history of the current game and all previous games is available. The most technically challenging part of the project was actually <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/spades/blob/master/EventThread.py#L30-L66\"><i class=\"fa fa-github\"></i>&nbsp;parsing the game server's events</a>, which are the same messages sent to IRC clients and not intended for programmatic use, and <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/spades/blob/master/GameConstructor.py\"><i class=\"fa fa-github\"></i>&nbsp;reconstructing the game</a> from this one-way information.<br><br>"
	print "While the screenshots above cover the highlights, the <a target=\"_blank\" href=\"http://spades.mrozekma.com/\">live site</a> is publicly accessible and will show the state of the current game."

@subpage('gir', 'Gir', 'git interactive rebase editor', 1432780392, 'static/images/projects/gir/spec', ['python', 'curses', 'git'], 'gir')
def gir(_):
	print "<em>Gir</em> is either immediately understandable or completely incomprehensible, depending on your familiarity with Git. Gir is a curses interface for editing git's interactive rebase todo list. Git normally opens this list in the user's default text editor, where each commit is given a line. Gir splits the window in half, drawing a formatted version of the todo list in the upper half with color-coding for the different commands, and showing the current commit's diff in the bottom half so you can remember what it was. Once each commit is marked appropriately, pressing <kbd>Enter</kbd> will submit the todo list to git just as if it were edited in a text editor."

@subpage('woop', 'Woop', 'keyboard-driven web browser', 1402217739, 'static/images/projects/woop/spec', ['python', 'gtk', 'webkit'])
def woop(_):
	print "<em>Woop</em> seemed like an excellent idea, until I discovered it had already been <a target=\"_blank\" href=\"http://www.vimperator.org/\">done</a>."
	phrase = ('Kind', 'of', 'a', 'lot')
	urls = ('http://vimium.github.io/', 'https://github.com/k2nr/ViChrome', 'https://github.com/jinzhu/vrome', 'https://www.uzbl.org/')
	print ' '.join("<a target=\"_blank\" href=\"%s\">%s</a>" % (url, word) for word, url in zip(phrase, urls)) + '.'
	print "Woop was a webkit-based web browser with a vim-like modal interface. Since the keyboard generally sits unused in a web browser unless interacting with a form, it's possible to bind useful functionality directly to letter keys without needing modifiers like <kbd>Ctrl</kbd> or <kbd>Alt</kbd>. For example, just pressing <kbd>t</kbd> can open a new tab. Much like vim itself, this interface is extremely efficient once the user gets acclimated.<br><br>I got the basic functionality working before discovering that the concept had already been implemented, so the project was never completed."
'''
[x] sprint
[x] noisebot
[x] spades
rorn
[x] gir
helm
taut?
arxantv
pytypecheck
[x] woop (browser)
cv

test_dispatcher
launchpad
'''
