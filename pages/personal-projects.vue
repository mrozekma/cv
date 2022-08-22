<template>
	<cv-terminal :prompts="['cd /personal-projects', 'ls -la --sort=relevance']">
		<br>
		<div class="prompt">/bin/project-filters --list --clickable</div>
		<div class="stdout project-tags">
			<span v-for="tag in allTags" class="label label-default" :class="{selected: selectedTags.includes(tag)}" @click="toggleTag(tag)">{{ tag }}</span>
		</div>
		<div class="tag-filter" v-if="selectedTags.length > 0">
			<div class="prompt">/bin/project-filters --set {{ selectedTags.join(' ') }}</div>
			<div class="stdout"><!-- stdout is preformatted, so the whitespace here is important -->
Projects filtered to only those with the requested tags. <button @click="selectedTags = []">Remove filter</button></div>
		</div>

		<cv-project
			project="serial-bridge"
			name="Serial Bridge"
			tagline="Serial port multiplexer"
			:mtime="1569550860"
			:tags="['vue', 'typescript', 'websocket', 'api']"
			:links="{repo: 'serial-bridge', docs: 'https://serial-bridge.readthedocs.io/en/latest/'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="device-expanded">
					A list of connected devices, with the first device expanded to show more information.
				</cv-project-screenshot>
				<cv-project-screenshot name="real-device-list">
					A list of devices from a real deploy, but with some device information anonymized.
				</cv-project-screenshot>
				<cv-project-screenshot name="setup">
					The setup tab on the homepage, which lets the user specify some preferences.
				</cv-project-screenshot>
				<cv-project-screenshot name="device-output">
					A device view. Each terminal represents a single port on the device. The colorful output in the middle terminal was produced by the Python Rich library.
				</cv-project-screenshot>
				<cv-project-screenshot name="device-commands-menu">
					The commands menu, used to quickly write to a port on a device.
				</cv-project-screenshot>
				<cv-project-screenshot name="device-ports">
					A list of ports on a particular device.
				</cv-project-screenshot>
				<cv-project-screenshot name="find-ports">
					A wizard for identifying which ports on a system corresponds to a particular device.
				</cv-project-screenshot>
				<cv-project-screenshot name="ports">
					All ports on the host system.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Serial Bridge</em> was written for use at <nuxt-link to="/work-history#mercury">Mercury</nuxt-link>. Its primary function is to make COM ports accessible remotely, so devices connected to a host machine can be accessed without needing to remote desktop into the host machine. Serial Bridge also allows multiple people to connect to the same device at once, which is normally impossible with a COM port. In addition to making the ports available over TCP, a web interface provides access via a browser.
		</cv-project>

		<cv-project
			project="chalk"
			name="Chalk"
			tagline="Coding interviews"
			:mtime="1589693700"
			:tags="['vue', 'typescript', 'websocket', 'api', 'firebase', 'monaco']"
			:links="{repo: 'chalk', production: 'https://chalk.run/'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="home">
					The list of upcoming interviews, as a calendar and a list.
				</cv-project-screenshot>
				<cv-project-screenshot name="interview">
					Details about a single interview, including the position, schedule, potential questions to ask, and the applicant's resume.
				</cv-project-screenshot>
				<cv-project-screenshot name="questions">
					A library of questions to ask. This is from a live instance, so the names have been blurred.
				</cv-project-screenshot>
				<cv-project-screenshot name="question">
					Details of a single question from the question library.
				</cv-project-screenshot>
				<cv-project-screenshot name="help">
					Information on how to create and conduct an interview.
				</cv-project-screenshot>
				<cv-project-screenshot name="board">
					The view during the interview itself, from the perspective of the interviewer.
				</cv-project-screenshot>
				<cv-project-screenshot name="board-candidate">
					The view during the interview itself, from the perspective of the applicant.
				</cv-project-screenshot>
				<cv-project-screenshot name="conducting-interview">
					An animation of both sides of a (very short) interview.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Chalk</em> came about during the COVID-19 pandemic, when <nuxt-link to="/work-history#mercury">we</nuxt-link> were suddenly unable to interview candidates in person. We use Skype for Business for an audio connection, but were unable to find a suitable shared code editor for the coding portion of the interview &mdash; existing sites are either expensive or very unreliable. Chalk's main feature is the collaborative code editor, which keeps all viewers synchronized. While I wish I could take credit, this is a combination of several third-party technologies: <a target="_blank" href="https://firebase.google.com/">Firebase</a> for the realtime database, <a target="_blank" href="https://microsoft.github.io/monaco-editor/">Monaco</a> (the editor that powers <a target="_blank" href="https://code.visualstudio.com/">Visual Studio Code</a>) for the code editor, and <a target="_blank" href="https://firepad.io/">Firepad</a> to connect them. Other features include a question library to make it easy to standardize questions across multiple interviews, file storage to enable quick access to things like the candidate's resume, and a compiler (courtesy of <a target="_blank" href="https://godbolt.org/">Compiler Explorer</a>) to check for errors.
		</cv-project>

		<cv-project
			project="point-vote"
			name="Point Vote"
			tagline="Planning poker"
			:mtime="1653709560"
			:tags="['vue', 'typescript', 'websocket']"
			:links="{repo: 'point-vote'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="point-vote">
					An animation of pretty much all the features available in Point Vote.
				</cv-project-screenshot>
				<cv-project-screenshot name="home">
					The homepage, where users can create or join a voting session.
				</cv-project-screenshot>
				<cv-project-screenshot name="session">
					A voting session, between votes.
				</cv-project-screenshot>
				<cv-project-screenshot name="voting">
					A voting session, mid-vote.
				</cv-project-screenshot>
				<cv-project-screenshot name="voted">
					A voting session, after all votes are cast.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Point Vote</em> was thrown together in a week (as demonstrated by the complete lack of style) when the Jira addon we were using for <a target="_blank" href="https://en.wikipedia.org/wiki/Planning_poker">planning poker</a> skyrocketed in price. It might make more sense for Point Vote to be a Jira addon as well, but from past experience those are a pretty big hassle to test and keep updated, and I would like eventually to break the dependency on Jira and let the tool operate independently.
		</cv-project>

		<cv-project
			project="ninja"
			name="Ninja"
			tagline="Non-linear data analysis tool"
			:mtime="1565645910"
			:tags="['vue', 'typescript', 'canvas']"
			:links="{repo: 'ninja', production: 'https://ninja.mrozekma.com/', docs: 'https://github.com/mrozekma/ninja/wiki'}"
		>
			<cv-project-screenshots ref="ninja-screenshots">
				<cv-project-screenshot name="routing">
					A very simple script that adds a given number to itself and prints the result.
				</cv-project-screenshot>
				<cv-project-screenshot name="home">
					A blank script, with most of the tools visible.
				</cv-project-screenshot>
				<cv-project-screenshot name="settings">
					The settings dialog.
				</cv-project-screenshot>
				<cv-project-screenshot name="properties">
					A single tool added to the script, with its properties visible.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Ninja</em> came about when a coworker was using <a target="_blank" href="https://gchq.github.io/CyberChef/">CyberChef</a> and complained about some of its limitations:

			<ul>
			<li><b>Linear data flow</b> &mdash; Each operation has one input and one output. For example, when encrypting data with AES, the input is the plaintext, which means the key (and any other setting) must be a constant. It's often desirable to have multiple parameters of a single operation configurable by data coming from other operations.</li>
			<li><b>Type confusion</b> &mdash; Because many of the operations work with raw data, there's constantly a need to specify if the data is encoded in hex or just provided as raw bytes. Many operations can only handle one form and will provide unexpected results if given the other form.</li>
			<li><b>PKCS#7 padding</b> &mdash; The padding mode used by the miscellaneous crypto operations cannot be changed, and will pad data that's already block-aligned. The authors have indicated this is intentional and unlikely to change, but is often not what we want.</li>
			</ul>

			Ninja takes the great idea of connectable data-transforming widgets and lays them out in two dimensions, allowing inputs and outputs to be connected freely. Unfortunately once I got the app itself working, I lost interest in making the many tools that are necessary for full functionality, although I would like to come back to it at some point.<br><br>

			For a simple script to experiment with (depicted in <a href="#" @click="$refs['ninja-screenshots'].show('routing')">one of the screenshots</a> above), click <a target="_blank" href="https://ninja.mrozekma.com/#eyJ2ZXJzaW9uIjoxLCJ0b29scyI6W3sidHlwZSI6IkNhbGMiLCJuYW1lIjoiQ2FsYyBhK2IiLCJsb2MiOnsieCI6MTU4LCJ5IjoxNDV9LCJpbnB1dHMiOnsiZXhwciI6IiRhKyRiIn0sImNvbm5lY3Rpb25zIjp7ImEiOlsiQ29uc3QgKDIpIiwib3V0Il0sImIiOlsiQ29uc3QgKDIpIiwib3V0Il19fSx7InR5cGUiOiJUZW1wbGF0ZSIsIm5hbWUiOiJUZW1wbGF0ZSIsImxvYyI6eyJ4IjozNywieSI6MjcyfSwiaW5wdXRzIjp7ImV4cHIiOiJUaGUgc3VtIG9mICRhIGFuZCAkYiBpcyAkc3VtIn0sImNvbm5lY3Rpb25zIjp7ImEiOlsiQ29uc3QgKDIpIiwib3V0Il0sImIiOlsiQ29uc3QgKDIpIiwib3V0Il0sInN1bSI6WyJDYWxjIGErYiIsIm91dCJdfX0seyJ0eXBlIjoiQ2FsYyIsIm5hbWUiOiJDb25zdCAoMikiLCJsb2MiOnsieCI6MTAsInkiOjEwfSwiaW5wdXRzIjp7ImV4cHIiOiIyIn0sImNvbm5lY3Rpb25zIjp7fX1dLCJ2aWV3cG9ydCI6eyJ4IjotMSwieSI6MCwic2NhbGUiOjF9LCJsb2NrQXV0b0xheW91dCI6ZmFsc2UsIndhdGNoZXMiOltbIkNhbGMgYStiIiwiZXhwciJdLFsiQ2FsYyBhK2IiLCJvdXQiXSxbIlRlbXBsYXRlIiwib3V0Il0sWyJDb25zdCAoMikiLCJvdXQiXV19">here</a>. For a more complicated script, see this demonstration video:<br><br>

			<iframe width="860" height="480" src="https://www.youtube.com/embed/pAvc2g23dwk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</cv-project>

		<cv-project
			project="sprint"
			name="Sprint"
			tagline="Scrum tracking tool"
			:mtime="1308373920"
			:tags="['python', 'javascript', 'html', 'css', 'jquery', 'websocket']"
			:links="{repo: 'sprint'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="home">
					The sprint tool homepage, containing a list of every project and sprint, starting with the current one. Note that while these screenshots are from a real deploy, the names of users, projects, sprints, and tasks have all been anonymized.
				</cv-project-screenshot>
				<cv-project-screenshot name="backlog">
					By far the most used page, the backlog is the list of every task on a given sprint. Each task includes the person assigned to work on it, the status (not started, in progress, blocked, etc.), the sprint goal the task is contributing to, and how much time the assignee estimates before it will be completed.
				</cv-project-screenshot>
				<cv-project-screenshot name="backlog-filtered">
					The backlog supports many filtering options via a search box, but the filters most commonly used during sprint meetings are given buttons along the top: the task assignee and the task status. In this case we're showing all non-started tasks with at least 16 estimated hours.
				</cv-project-screenshot>
				<cv-project-screenshot name="metrics">
					There are quite a few graphs available to track sprint progress, although only two are visible here: the day-to-day total estimated hours remaining versus the number of hours the team is scheduled to work on the project, and the current hours each team member has scheduled versus their remaining availability. This sprint is not going well &mdash; three people have more work than they can complete even if they finish tasks at the scheduled rate, and as a team the remaining hours is about to exceed the total hours available, and projections show nearly 500 hours of uncompleted work at the end of the sprint if progress stays at the same rate.
				</cv-project-screenshot>
				<cv-project-screenshot name="metrics-past">
					The previous metrics screenshot was from a sprint that got off to a bad start; this is the metrics for a more typical sprint that is already complete. The hours drop to 0 on the last day because all incomplete tasks are automatically deferred.
				</cv-project-screenshot>
				<cv-project-screenshot name="history">
					A complete list of task changes during the sprint. Hours are generally the most interesting thing and are graphed at the top, but all changes are listed.
				</cv-project-screenshot>
				<cv-project-screenshot name="task-history">
					All the changes made to a particular task. Again hours get a dedicated graph since that's generally what people want to see.
				</cv-project-screenshot>
				<cv-project-screenshot name="calendar">
					A calendar view of when all sprints begin and end.
				</cv-project-screenshot>
				<cv-project-screenshot name="error">
					A sample error page, included because I'm quite proud of the syntax highlighted code. I had to hack in a test error because the actual Sprint code is free of all bugs.
				</cv-project-screenshot>
			</cv-project-screenshots>

			The <em>Sprint tool</em>, as it came to be known when I forgot to come up with a real name, is a web-based <a target="_blank" href="https://en.wikipedia.org/wiki/Scrum_(software_development)">Scrum</a> tracking tool. I wrote it largely in 2011-2012 in my free time for use at <nuxt-link to="/work-history#microsemi">Microsemi</nuxt-link>. Its predecessor was an Excel spreadsheet filled with formulas and custom cell formatting that tended to slowly degenerate as it was copied from sprint to sprint until the metrics it reported bore little resemblance to the actual hours entered into the cells. While the Sprint tool was originally written just for internal use at my company, former coworkers have carried it with them to at least three other companies that I know of. This was relatively painless, once a few <a target="_blank" href="https://github.com/mrozekma/Sprint/commit/b0ac62a97c28b871c4853686bda6426060eb7a90">poorly-conceived</a> <a target="_blank" href="https://github.com/mrozekma/Sprint/commit/b6b1af214e77de7b6680d565aeddfebce00c1385">hardcoded values</a> were fixed.<br><br>

			The Sprint tool is also noteworthy as my first Python webapp, as my previous web work was in PHP. It contained a custom web framework on top of Python's built-in <a target="_blank" href="https://docs.python.org/2/library/basehttpserver.html">HTTP server</a>; this framework has since been pulled out into its <a target="_blank" href="https://github.com/mrozekma/rorn">own project</a> so I could use it on <nuxt-link to="#spades">other webapps</nuxt-link>, including the first draft of <a target="_blank" href="https://github.com/mrozekma/cv/tree/python">this very site</a>.
		</cv-project>

		<cv-project
			project="noisebot"
			name="Noisebot"
			tagline="Chat bot"
			:mtime="1277020414"
			:tags="['java', 'irc', 'slack', 'api']"
			:links="{repo: 'noisebot'}"
		>
			<!-- IRC: Choose, Help, Poll, Weather, Wikipedia, Wolfram, Youtube -->
			<!-- Slack: EmojiRace, LaTeXMath, Wikipedia, Youtube -->
			<cv-project-screenshots>
				<cv-project-screenshot name="slack-poll">
					Taking a poll in Slack.
				</cv-project-screenshot>
				<cv-project-screenshot name="irc-poll">
					Showing the current weather for everyone in the room, and taking a poll in IRC.
				</cv-project-screenshot>
				<cv-project-screenshot name="irc-url-info">
					Resolving information about Youtube and Twitter URLs. Many other sites are also handled, including Imgur, Reddit, TVTropes, and Twitch.
				</cv-project-screenshot>
				<cv-project-screenshot name="slack-update">
					What it looks like when new commits are pushed to Github. The synchronization and reload/restart is entirely automatic.
				</cv-project-screenshot>
				<cv-project-screenshot name="irc-update">
					The IRC version of a bot update.
				</cv-project-screenshot>
				<cv-project-screenshot name="slack-emojirace">
					Slack supports message editing, which Noisebot abuses for entertainment purposes.
				</cv-project-screenshot>
				<cv-project-screenshot name="slack-latexmath">
					A module to render a LaTeX-formatted equation.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Noisebot</em> originated as a fairly simple collection of Python scripts to provide useful functions in the IRC channel populated by the Linux Users Group I belonged to in <nuxt-link to="/education#rose-hulman">undergrad</nuxt-link>. It was later rewritten in Java and expanded to support Slack. Unlike other chat bots, Noisebot was designed from the ground up to be <a target="_blank" href="https://github.com/mrozekma/noisebot#developer-documentation">easily updatable by anyone</a>. When a new commit is pushed to the repository, it is automatically validated and then deployed to Github. Running bots are alerted to the change and synchronize automatically, reloading affected modules without restarting. This ease of updating makes Noisebot the only project on this page with a non-trivial number of <a target="_blank" href="https://github.com/mrozekma/NoiseBot/graphs/contributors">contributors</a>.<br><br>

			If you're interested in watching me code at 4x speed, I have a video of the development of the <a target="_blank" href="https://github.com/mrozekma/NoiseBot/blob/master/src/modules/EmojiRace.java">EmojiRace module</a>:<br><br>

			<iframe width="860" height="480" src="https://www.youtube.com/embed/l98orlySZZA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
		</cv-project>

		<cv-project
			project="spades"
			name="Spades"
			tagline="Web-based cards interface"
			:mtime="1446781016"
			:tags="['python', 'javascript', 'html', 'css', 'jquery', 'websocket', 'api']"
			:links="{repo: 'spades'}"
		>
			<cv-project-screenshots ref="spades-screenshots">
				<cv-project-screenshot name="game-full-round">
					A high-speed animation of what game setup and the first round looks like. While this is a real game, here each play takes one second; the actual round took over a month to play out.
				</cv-project-screenshot>
				<cv-project-screenshot name="game-with-irc">
					The early portion of a round (just after the lead in the second trick). The corresponding IRC log that led to this point is superimposed.
				</cv-project-screenshot>
				<cv-project-screenshot name="game-score-history">
					The score history of a completed game. The green line indicates the goal score, while the red and blue lines track each team's score round-to-round. The boxes flagging some of the scores indicate particularly impactful events.
				</cv-project-screenshot>
				<cv-project-screenshot name="game-round-history">
					The history of a single round, including the score change for each team, the point spread between teams, how close the leading team is to winning, which cards each player played, which ones were winners (the green background), a heatmap of suits in each hand, the breakdown of each trick, and a chart of the resulting bid versus score.
				</cv-project-screenshot>
				<cv-project-screenshot name="player">
					A player's history, including their win rate, how often they bid particular amounts and how often they make each bid, how often they win with each partner, and (not depicted here) how often they lead and win with each card in the deck.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Spades</em> takes some explanation. Several years ago a friend of mine implemented an IRC bot to let users play the card game <a target="_blank" href="https://en.wikipedia.org/wiki/Spades">Spades</a>. (He implemented it in AWK, so the <a class="github-link" target="_blank" href="https://github.com/Andy753421/rhawk/blob/master/spades.awk"><font-awesome-icon :icon="githubIcon"/>&nbsp;code</a> is worth looking at).

			You can see a short snippet of what the IRC interface looks like in <a href="#" @click="$refs['spades-screenshots'].show('game-with-irc')">one of the screenshots</a> above; naturally it is somewhat inefficient.

			This project is a web-based interface to show current and historical games. It communicates with the game server and with client browsers using websockets, and shows each play as it happens. The complete history of the current game and all previous games is available. The most technically challenging part of the project was actually <a class="github-link" target="_blank" href="https://github.com/mrozekma/spades/blob/master/EventThread.py#L30-L66"><font-awesome-icon :icon="githubIcon"/>&nbsp;parsing the game server's events</a>, which are the same messages sent to IRC clients and not intended for programmatic use, and <a class="github-link" target="_blank" href="https://github.com/mrozekma/spades/blob/master/GameConstructor.py"><font-awesome-icon :icon="githubIcon"/>&nbsp;reconstructing the game</a> from this one-way information.<br><br>

			<!-- While the screenshots above cover the highlights, the <a target="_blank" href="http://spades.mrozekma.com/">live site</a> is publicly accessible and will show the state of the current game. -->
		</cv-project>

		<cv-project
			project="got"
			name="Got"
			tagline="Git repository manager"
			:mtime="1532316900"
			:tags="['python', 'git', 'bitbucket', 'api']"
			:links="{repo: 'got', docs: 'http://got.readthedocs.io/'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="got">
					An example of requesting a repository's path. The first time the repository isn't cloned yet, so got clones it before returning the new path. The second time, the clone already exists, so got just reports the path.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Got</em> was written for use at <nuxt-link to="/work-history#mercury">Mercury</nuxt-link>. Before my office was acquired by Mercury, all code was stored in a centralized subversion repository, and it was common for projects to depend on each other via relative paths. For example, if <code>products/foo</code> depends on code from <code>libraries/bar</code>, it would simply point at <code>../../libraries/bar</code>.

			After the migration to git, <code>products/foo</code> and <code>libraries/bar</code> would now be stored in separate repositories in Bitbucket. This means that when a user builds <code>products/foo</code>:

			<ol>
				<li>The user might not have <code>libraries/bar</code> cloned.</li>
				<li><code>libraries/bar</code> might be cloned anywhere on disk, not at a fixed location relative to <code>products/foo</code>.</li>
			</ol>

			Got solves this problem by essentially combining <a target="_blank" href="https://en.wikipedia.org/wiki/Pkg-config">pkg-config</a> with <a target="_blank" href="https://code.google.com/archive/p/git-repo/">git-repo</a> to create a tool that not only provides the locations of repositories on request, but will download those repositories from a remote host if they're not already on disk. This means build systems can simply run <code>got repo_name</code> to get the path to the specified repository, regardless of if it's already been cloned.
		</cv-project>

		<cv-project
			project="lynchelper"
			name="Lync Helper"
			tagline="Lync utility pack"
			:mtime="1532316900"
			:tags="['c#', 'lync', 'api']"
			:links="{repo: {host: 'gitlab', name: 'lynchelper'}}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="codeshare">
					Sharing a code snippet. The code snippet is syntax-highlighted, in a monospace font, and suppresses Lync features like emoji expansion.
				</cv-project-screenshot>
				<cv-project-screenshot name="installer">
					A simple GUI for installing Lync Helper. All actions that require admin access are grouped in a single program in case users need to go through IT to run a program with admin permissions.
				</cv-project-screenshot>
				<cv-project-screenshot name="logging-settings">
					Configuration for the logging system. This lets the user customize where log files are stored, and how they are formatted.
				</cv-project-screenshot>
				<cv-project-screenshot name="logging-tray">
					The system tray icon used to control the logging system.
				</cv-project-screenshot>
			</cv-project-screenshots>

			If you live in the happy world of Slack and RocketChat, you may be unfamiliar with Lync, otherwise known as Skype for Business. <em>Lync Helper</em> is a tool to work around some of Lync's more annoying limitations. It has two main modules:

			<ul>
				<li><em>Code Share</em>, a tool for sending code snippets to other users. Sharing code with coworkers is common, but Lync has a fairly short message limit and automatically converts common strings to emoji. For example, code containing <code>std::string</code> will be rendered by Lync as <code>std:<img src="/images/projects/lynchelper/worried-emoji.png" style="width: 14px">tring</code>. Code Share suppresses this emoji rendering, formats the code in monospace, and syntax highlights it for ease of readability.</li>
				<li><em>Logging</em>, a tool to log all conversations to text files on disk. Lync only supports logging to an Exchange database, and does so piecemeal, leading to lots of duplicated snippets that are difficult to search.</li>
			</ul>
		</cv-project>

		<cv-project
			project="gir"
			name="Gir"
			tagline="Git interactive rebase editor"
			:mtime="1432780392"
			:tags="['python', 'curses', 'git']"
			:links="{repo: 'gir'}"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="all-choices">
					Gir highlights each commit based on the chosen command; here each of the first six commits has a different command to show all possible row colors.
				</cv-project-screenshot>
				<cv-project-screenshot name="all-pick">
					By default (in most circumstances) every commit will start with the "pick" command, so this is what gir will look like when first started.
				</cv-project-screenshot>
				<cv-project-screenshot name="help">
					Gir is entirely keyboard-driven; pressing <kbd>F1</kbd> shows a list of the available hotkeys.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Gir</em> is either immediately understandable or completely incomprehensible, depending on your familiarity with Git. Gir is a curses interface for editing git's interactive rebase todo list. Git normally opens this list in the user's default text editor, where each commit is given a line. Gir splits the window in half, drawing a formatted version of the todo list in the upper half with color-coding for the different commands, and showing the current commit's diff in the bottom half so you can remember what it was. Once each commit is marked appropriately, pressing <kbd>Enter</kbd> will submit the todo list to git just as if it were edited in a text editor.
		</cv-project>

		<cv-project
			project="woop"
			name="Woop"
			tagline="Keyboard-driven web browser"
			:mtime="1402217739"
			:tags="['python', 'gtk', 'webkit']"
		>
			<cv-project-screenshots>
				<cv-project-screenshot name="google">
					Woop opened to Google's homepage.
				</cv-project-screenshot>
				<cv-project-screenshot name="tabopen">
					Woop in command mode &mdash; a <em>tabopen</em> command is being typed along the bottom of the screen.
				</cv-project-screenshot>
				<cv-project-screenshot name="refresh">
					Woop in command mode, tab-completing a command.
				</cv-project-screenshot>
			</cv-project-screenshots>

			<em>Woop</em> seemed like an excellent idea, until I discovered it had already been <a target="_blank" href="http://www.vimperator.org/">done</a>. <a target="_blank" href="http://vimium.github.io/">Kind</a> <a target="_blank" href="https://github.com/k2nr/ViChrome">of</a> <a target="_blank" href="https://github.com/jinzhu/vrome">a</a> <a target="_blank" href="https://www.uzbl.org/">lot</a>.

			Woop was a webkit-based web browser with a vim-like modal interface. Since the keyboard generally sits unused in a web browser unless interacting with a form, it's possible to bind useful functionality directly to letter keys without needing modifiers like <kbd>Ctrl</kbd> or <kbd>Alt</kbd>. For example, just pressing <kbd>t</kbd> can open a new tab. Much like vim itself, this interface is extremely efficient once the user gets acclimated.<br><br>I got the basic functionality working before discovering that the concept had already been implemented, so the project was never completed.
		</cv-project>
	</cv-terminal>
</template>

<script lang="ts">
	import Vue from 'vue';

	import { iterChildren } from '~/scripts/vue-hierarchy';

	import _ from 'lodash';
	import { faGithub, IconDefinition } from '@fortawesome/free-brands-svg-icons';

	import CvTerminal from '~/components/terminal.vue';
	import CvProject from '~/components/project.vue';
	import CvProjectScreenshots from '~/components/project-screenshots.vue';
	import CvProjectScreenshot from '~/components/project-screenshot.vue';
	const component = Vue.extend({
		name: "personal-projects",
		components: { CvTerminal, CvProject, CvProjectScreenshots, CvProjectScreenshot },
		head() {
			return {
				title: 'Personal Projects',
			};
		},
		computed: {
			githubIcon(): IconDefinition {
				return faGithub;
			},
		},
		data() {
			return {
				allTags: [] as string[],
				selectedTags: [] as string[],
			};
		},
		methods: {
			toggleTag(tag: string) {
				const idx = this.selectedTags.indexOf(tag);
				if(idx == -1) {
					this.selectedTags.push(tag);
				} else {
					this.selectedTags.splice(idx, 1);
				}
			},
		},
		mounted() {
			this.allTags = _.uniq(_.flatten(Array.from(iterChildren(this, CvProject)).map(project => project.tags))).sort();
		},
	});
	export default component;
	export type PersonalProjectsComp = InstanceType<typeof component>;
</script>

<style lang="less" scoped>
	.stdout.project-tags {
		margin: 20px;
		.label {
			cursor: pointer;

			&.selected {
				background-color: #c00;
			}
		}
	}
</style>
