from Photoswipe import Photoswipe
from Terminal import Terminal

from rorn.Lock import SingleLock as Lock
from rorn.ResponseWriter import ResponseWriter

import sys

term = Terminal('cd /personal-projects', 'ls -lar --sort=relevance')
termLock = Lock()
allTags = set()

# @get('personal-projects', statics = ['projects'])
@get('personal-projects', statics = ['projects', 'bootstrap'] + Photoswipe.getStatics())
def projects(handler, tags = None):
	handler.title('Personal Projects', 'personal-projects')
	print(Photoswipe.getRootElement())

	# Generate the list of level -> school symlinks. This is drawn between the regular list and the individual subpages
	with ResponseWriter() as w:
		print("<br>")
		print("<div class=\"prompt\">/bin/project-filters --list --clickable</div>")
		print("<div class=\"stdout project-tags\">")
		for tag in sorted(allTags):
			sys.stdout.write("<span class=\"label label-default\">%s</span>" % tag)
		print()
		print("</div>")

		print("<div class=\"tag-filter\">")
		print("<div class=\"prompt\">/bin/project-filters --set <div class=\"tag-list\"></div></div>")
		print("<div class=\"stdout\">\nProjects filtered to only those with the requested tags. <button id=\"tag-filter-clear\">Remove filter</button>\n</div>")
		print("</div>")
		term.setInterstitial(w.done())

	# Output everything
	# This is super gross, but it's still happening -- storing the filter data on 'term' for the length of the print, which means it needs a lock since 'term' is global
	with termLock as l:
		term.tags = tags.split(' ') if tags else []
		try:
			print(term)
		finally:
			del term.tags

def subpage(project, name, tagline, mtime, screenshotSpec, tags, links = {}):
	allTags.update(tags)

	def fn(real_handler):
		@term.subpage(project, mtime)
		def fn2():
			print("<div class=\"name\">%s</div>" % name)
			print("<div class=\"tagline\">%s</div>" % tagline)
			print("<div class=\"project-filters\">")
			for tag in tags:
				print("<span class=\"label label-default\">%s</span>" % tag)
			print("</div>")
			if links:
				print("<div class=\"project-links\">")
				if 'repo' in links:
					repoHost, repoName = links['repo'] if isinstance(links['repo'], tuple) else ('github', links['repo'])
					if repoHost == 'github':
						print(f"<a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/{repoName}\"><i class=\"fa fa-lg fa-github\"></i>&nbsp;Github repository</a>")
					elif repoHost == 'gitlab':
						print(f"<a class=\"gitlab-link\" target=\"_blank\" href=\"https://gitlab.com/mrozekma/{repoName}\"><i class=\"fa fa-lg fa-gitlab\"></i>&nbsp;Gitlab repository</a> (private, but available on request)")
					else:
						raise ValueError(f"Unrecognized host: {repoHost}")
				if 'production' in links:
					print(f"<a class=\"prod-link\" target=\"_blank\" href=\"{links['production']}\"><i class=\"fa fa-lg fa-columns\"></i>&nbsp;Live website</a>")
				if 'docs' in links:
					print(f"<a class=\"doc-link\" target=\"_blank\" href=\"{links['docs']}\"><i class=\"fa fa-lg fa-book\"></i>&nbsp;Documentation</a>")
				print("</div>")
			pswp = Photoswipe.fromSpec(screenshotSpec)
			print(pswp)
			print("<div class=\"description\">")
			real_handler(pswp)
			print("</div>")
		return fn2
	return fn

@subpage('sprint', 'Sprint', 'scrum tracking tool', 1308373920, 'static/images/projects/sprint/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket'], {'repo': 'sprint'})
def sprint(_):
	print("The <em>Sprint tool</em>, as it came to be known when I forgot to come up with a real name, is a web-based <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Scrum_(software_development)\">Scrum</a> tracking tool. I wrote it largely in 2011-2012 in my free time for use at <a target=\"_blank\" href=\"/work-history#microsemi\">Microsemi</a>. Its predecessor was an Excel spreadsheet filled with formulas and custom cell formatting that tended to slowly degenerate as it was copied from sprint to sprint until the metrics it reported bore little resemblance to the actual hours entered into the cells. While the Sprint tool was originally written just for internal use at my company, former coworkers have carried it with them to at least three other companies that I know of. This was relatively painless, once a few <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b0ac62a97c28b871c4853686bda6426060eb7a90\">poorly-conceived</a> <a target=\"_blank\" href=\"https://github.com/mrozekma/Sprint/commit/b6b1af214e77de7b6680d565aeddfebce00c1385\">hardcoded values</a> were fixed.<br><br>")
	print("The Sprint tool is also noteworthy as my first Python webapp, as my previous web work was in PHP. It contained a custom web framework on top of Python's built-in <a target=\"_blank\" href=\"https://docs.python.org/2/library/basehttpserver.html\">HTTP server</a>; this framework has since been pulled out into its <a target=\"_blank\" href=\"https://github.com/mrozekma/rorn\">own project</a> so I could use it on <a href=\"#spades\">other webapps</a>, including <a target=\"_blank\" href=\"https://github.com/mrozekma/cv\">this very site</a>.")

@subpage('noisebot', 'Noisebot', 'chat bot', 1277020414, 'static/images/projects/noisebot/spec', ['java', 'irc', 'slack', 'api'], {'repo': 'noisebot'})
def noisebot(_):
	# IRC: Choose, Help, Poll, Weather, Wikipedia, Wolfram, Youtube
	# Slack: EmojiRace, LaTeXMath, Wikipedia, Youtube
	print("<em>Noisebot</em> originated as a fairly simple collection of Python scripts to provide useful functions for use in the IRC channel populated by the Linux Users Group I belonged to in <a target=\"_blank\" href=\"/education#rose-hulman\">undergrad</a>. It was later rewritten in Java and expanded to support Slack. Unlike other chat bots, Noisebot was designed from the ground up to be <a target=\"_blank\" href=\"https://github.com/mrozekma/noisebot#developer-documentation\">easily updatable by anyone</a>. When a new commit is pushed to the repository, it is automatically validated and then deployed to Github. Running bots are alerted to the change and synchronize automatically, reloading affected modules without restarting. This ease of updating makes Noisebot the only project on this page with a non-trivial number of <a target=\"_blank\" href=\"https://github.com/mrozekma/NoiseBot/graphs/contributors\">contributors</a>.<br><br>")
	print("If you're interested in watching me code at 4x speed, I have a video of the development of the <a href=\"https://github.com/mrozekma/NoiseBot/blob/master/src/modules/EmojiRace.java\">EmojiRace module</a>:<br><br>")
	print("<iframe width=\"854\" height=\"480\" src=\"https://www.youtube.com/embed/l98orlySZZA\" frameborder=\"0\" allowfullscreen></iframe>")

@subpage('spades', 'Spades', 'web-based cards interface', 1446781016, 'static/images/projects/spades/spec', ['python', 'javascript', 'html', 'css', 'jquery', 'websocket', 'api'], {'repo': 'spades', 'production': 'http://spades.mrozekma.com/'})
def spades(pswp):
	idx = pswp.getIndexByPath('game-with-irc')
	print("<em>Spades</em> takes some explanation. Several years ago a friend of mine implemented an IRC bot to let users play the card game <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Spades\">Spades</a>. (He implemented it in AWK, so the <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/Andy753421/rhawk/blob/master/spades.awk\"><i class=\"fa fa-github\"></i>&nbsp;code</a> is worth looking at).")
	print("You can see a short snippet of what the IRC interface looks like in <a class=\"screenshot-link\" data-pswp=\"%s\" data-index=\"%d\" href=\"#\">one of the screenshots</a> above; naturally it is somewhat inefficient." % (pswp.id, idx))
	print("This project is a web-based interface to show current and historical games. It communicates with the game server and with client browsers using websockets, and shows each play as it happens. The complete history of the current game and all previous games is available. The most technically challenging part of the project was actually <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/spades/blob/master/EventThread.py#L30-L66\"><i class=\"fa fa-github\"></i>&nbsp;parsing the game server's events</a>, which are the same messages sent to IRC clients and not intended for programmatic use, and <a class=\"github-link\" target=\"_blank\" href=\"https://github.com/mrozekma/spades/blob/master/GameConstructor.py\"><i class=\"fa fa-github\"></i>&nbsp;reconstructing the game</a> from this one-way information.<br><br>")
	print("While the screenshots above cover the highlights, the <a target=\"_blank\" href=\"http://spades.mrozekma.com/\">live site</a> is publicly accessible and will show the state of the current game.")

@subpage('got', 'Got', 'git repository manager', 1532316900, 'static/images/projects/got/spec', ['python', 'git', 'bitbucket', 'api'], {'repo': 'got', 'docs': 'http://got.readthedocs.io/'})
def got(_):
	print("<em>Got</em> was written for use at <a target=\"_blank\" href=\"/work-history#mercury\">Mercury</a>. Before my office was acquired by Mercury, all code was stored in a centralized subversion repository, and it was common for projects to depend on each other via relative paths. For example, if <code>products/foo</code> depends on code from <code>libraries/bar</code>, it would simply point at <code>../../libraries/bar</code>.")
	print("After the migration to git, <code>products/foo</code> and <code>libraries/bar</code> would now be stored in separate repositories in Bitbucket. This means that when a user builds <code>products/foo</code>:")
	print("<ol><li>The user might not have <code>libraries/bar</code> cloned.</li><li><code>libraries/bar</code> might be cloned anywhere on disk, not at a fixed location relative to <code>products/foo</code>.</li></ol>")
	print("Got solves this problem by essentially combining <a target=\"_blank\" href=\"https://en.wikipedia.org/wiki/Pkg-config\">pkg-config</a> with <a target=\"_blank\" href=\"https://code.google.com/archive/p/git-repo/\">git-repo</a> to create a tool that not only provides the locations of repositories on request, but will download those repositories from a remote host if they're not already on disk. This means build systems can simply run <code>got repo_name</code> to get the path to the specified repository, regardless of if it's already been cloned or not.")

@subpage('lynchelper', 'Lync Helper', 'lync utility pack', 1532316900, 'static/images/projects/lynchelper/spec', ['c#', 'lync', 'api'], {'repo': ('gitlab', 'lynchelper')})
def lynchelper(_):
	print("If you live in the happy world of Slack and RocketChat, you may be unfamiliar with Lync, otherwise known as Skype for Business. <em>Lync Helper</em> is a tool to work around some of Lync's more annoying limitations. It has two main modules:")
	print("<ul>")
	print("<li><em>Code Share</em>, a tool for sending code snippets to other users. Sharing code with coworkers is common, but Lync has a fairly short message limit and automatically converts common strings to emoji. For example, code containing <code>std::string</code> will be rendered by Lync as <code>std:<img src=\"/static/images/projects/lynchelper/worried-emoji.png\" style=\"width: 14px\">tring</code>. Code Share suppresses this emoji rendering, formats the code in monospace, and syntax highlights it for ease of readability.</li>")
	print("<li><em>Logging</em>, a tool to log all conversations to text files on disk. Lync only supports logging to an Exchange database, and does so piecemeal, leading to lots of duplicated snippets that are difficult to search.</li>")
	print("</ul>")

@subpage('gir', 'Gir', 'git interactive rebase editor', 1432780392, 'static/images/projects/gir/spec', ['python', 'curses', 'git'], {'repo': 'gir'})
def gir(_):
	print("<em>Gir</em> is either immediately understandable or completely incomprehensible, depending on your familiarity with Git. Gir is a curses interface for editing git's interactive rebase todo list. Git normally opens this list in the user's default text editor, where each commit is given a line. Gir splits the window in half, drawing a formatted version of the todo list in the upper half with color-coding for the different commands, and showing the current commit's diff in the bottom half so you can remember what it was. Once each commit is marked appropriately, pressing <kbd>Enter</kbd> will submit the todo list to git just as if it were edited in a text editor.")

@subpage('woop', 'Woop', 'keyboard-driven web browser', 1402217739, 'static/images/projects/woop/spec', ['python', 'gtk', 'webkit'])
def woop(_):
	print("<em>Woop</em> seemed like an excellent idea, until I discovered it had already been <a target=\"_blank\" href=\"http://www.vimperator.org/\">done</a>.")
	phrase = ('Kind', 'of', 'a', 'lot')
	urls = ('http://vimium.github.io/', 'https://github.com/k2nr/ViChrome', 'https://github.com/jinzhu/vrome', 'https://www.uzbl.org/')
	print(' '.join("<a target=\"_blank\" href=\"%s\">%s</a>" % (url, word) for word, url in zip(phrase, urls)) + '.')
	print("Woop was a webkit-based web browser with a vim-like modal interface. Since the keyboard generally sits unused in a web browser unless interacting with a form, it's possible to bind useful functionality directly to letter keys without needing modifiers like <kbd>Ctrl</kbd> or <kbd>Alt</kbd>. For example, just pressing <kbd>t</kbd> can open a new tab. Much like vim itself, this interface is extremely efficient once the user gets acclimated.<br><br>I got the basic functionality working before discovering that the concept had already been implemented, so the project was never completed.")
