<template>
  <cv-terminal :prompts="['cd /personal-projects', 'ls -lar --sort=relevance']">
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
      project="sprint"
      name="Sprint"
      tagline="scrum tracking tool"
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
          There are quite a few graphs available to track sprint progress, although only two are visible here: the day-to-day total estimated hours remaining versus the number of hours the team is scheduled to work on the project, and the current hours each team member has scheduled versus their remaining availability. This sprint is not going well -- three people have more work than they can complete even if they finish tasks at the scheduled rate, and as a team the remaining hours is about to exceed the total hours available, and projections show nearly 500 hours of uncompleted work at the end of the sprint if progress stays at the same rate.
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

      The Sprint tool is also noteworthy as my first Python webapp, as my previous web work was in PHP. It contained a custom web framework on top of Python's built-in <a target="_blank" href="https://docs.python.org/2/library/basehttpserver.html">HTTP server</a>; this framework has since been pulled out into its <a target="_blank" href="https://github.com/mrozekma/rorn">own project</a> so I could use it on <nuxt-link to="#spades">other webapps</nuxt-link>, including <a target="_blank" href="https://github.com/mrozekma/cv">this very site</a>.
    </cv-project>

    <cv-project
      project="noisebot"
      name="Noisebot"
      tagline="chat bot"
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

      <em>Noisebot</em> originated as a fairly simple collection of Python scripts to provide useful functions for use in the IRC channel populated by the Linux Users Group I belonged to in <nuxt-link to="/education#rose-hulman">undergrad</nuxt-link>. It was later rewritten in Java and expanded to support Slack. Unlike other chat bots, Noisebot was designed from the ground up to be <a target="_blank" href="https://github.com/mrozekma/noisebot#developer-documentation">easily updatable by anyone</a>. When a new commit is pushed to the repository, it is automatically validated and then deployed to Github. Running bots are alerted to the change and synchronize automatically, reloading affected modules without restarting. This ease of updating makes Noisebot the only project on this page with a non-trivial number of <a target="_blank" href="https://github.com/mrozekma/NoiseBot/graphs/contributors">contributors</a>.<br><br>

      If you're interested in watching me code at 4x speed, I have a video of the development of the <a target="_blank" href="https://github.com/mrozekma/NoiseBot/blob/master/src/modules/EmojiRace.java">EmojiRace module</a>:<br><br>

      <iframe width="854" height="480" src="https://www.youtube.com/embed/l98orlySZZA" frameborder="0" allowfullscreen></iframe>
    </cv-project>

    <cv-project
      project="spades"
      name="Spades"
      tagline="web-based cards interface"
      :mtime="1446781016"
      :tags="['python', 'javascript', 'html', 'css', 'jquery', 'websocket', 'api']"
      :links="{repo: 'spades', production: 'http://spades.mrozekma.com/'}"
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

      While the screenshots above cover the highlights, the <a target="_blank" href="http://spades.mrozekma.com/">live site</a> is publicly accessible and will show the state of the current game.
    </cv-project>

    <cv-project
      project="got"
      name="Got"
      tagline="git repository manager"
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
      tagline="lync utility pack"
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
      tagline="git interactive rebase editor"
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
      tagline="keyboard-driven web browser"
      :mtime="1402217739"
      :tags="['python', 'gtk', 'webkit']"
    >
      <cv-project-screenshots>
        <cv-project-screenshot name="google">
          Woop opened to Google's homepage.
        </cv-project-screenshot>
        <cv-project-screenshot name="tabopen">
          Woop in command mode -- a <em>tabopen</em> command is being typed along the bottom of the screen.
        </cv-project-screenshot>
        <cv-project-screenshot name="refresh">
          Woop in command mode, tab-completing a command.
        </cv-project-screenshot>
      </cv-project-screenshots>

      <em>Woop</em> seemed like an excellent idea, until I discovered it had already been <a target="_blank" href="http://www.vimperator.org/">done</a>. <a target="_blank" href="http://vimium.github.io/">Kind</a> <a target="_blank" href="https://github.com/k2nr/ViChrome">of</a> <a target="_blank" href="https://github.com/jinzhu/vrome">a</a> <a target="_blank" href="https://www.uzbl.org/">lot</a>.

      Woop was a webkit-based web browser with a vim-like modal interface. Since the keyboard generally sits unused in a web browser unless interacting with a form, it's possible to bind useful functionality directly to letter keys without needing modifiers like <kbd>Ctrl</kbd> or <kbd>Alt</kbd>. For example, just pressing <kbd>t</kbd> can open a new tab. Much like vim itself, this interface is extremely efficient once the user gets acclimated.<br><br>I got the basic functionality working before discovering that the concept had already been implemented, so the project was never completed.
    </cv-project>

    <!-- From http://photoswipe.com/documentation/getting-started.html -->
    <!-- Root element of PhotoSwipe. Must have class pswp. -->
    <div class="pswp" tabindex="-1" role="dialog" aria-hidden="true">

      <!-- Background of PhotoSwipe.
           It's a separate element as animating opacity is faster than rgba(). -->
      <div class="pswp__bg"></div>

      <!-- Slides wrapper with overflow:hidden. -->
      <div class="pswp__scroll-wrap">

        <!-- Container that holds slides.
            PhotoSwipe keeps only 3 of them in the DOM to save memory.
            Don't modify these 3 pswp__item elements, data is added later on. -->
        <div class="pswp__container">
          <div class="pswp__item"></div>
          <div class="pswp__item"></div>
          <div class="pswp__item"></div>
        </div>

        <!-- Default (PhotoSwipeUI_Default) interface on top of sliding area. Can be changed. -->
        <div class="pswp__ui pswp__ui--hidden">

          <div class="pswp__top-bar">

            <!--  Controls are self-explanatory. Order can be changed. -->

            <div class="pswp__counter"></div>

            <button class="pswp__button pswp__button--close" title="Close (Esc)"></button>

            <button class="pswp__button pswp__button--share" title="Share"></button>

            <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button>

            <button class="pswp__button pswp__button--zoom" title="Zoom in/out"></button>

            <!-- Preloader demo http://codepen.io/dimsemenov/pen/yyBWoR -->
            <!-- element will get class pswp__preloader--active when preloader is running -->
            <div class="pswp__preloader">
              <div class="pswp__preloader__icn">
                <div class="pswp__preloader__cut">
                  <div class="pswp__preloader__donut"></div>
                </div>
              </div>
            </div>
          </div>

          <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
            <div class="pswp__share-tooltip"></div>
          </div>

          <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
          </button>

          <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
          </button>

          <div class="pswp__caption">
            <div class="pswp__caption__center"></div>
          </div>

        </div>

      </div>

    </div>
  </cv-terminal>
</template>

<script>
  import { iterChildren } from '~/scripts/vue-hierarchy.js';

  const _ = require('lodash');
  import { faGithub } from '@fortawesome/free-brands-svg-icons';

  import CvTerminal from '~/components/cv-terminal.vue';
  import CvProject from '~/components/cv-project.vue';
  import CvProjectScreenshots from '~/components/cv-project-screenshots.vue';
  import CvProjectScreenshot from '~/components/cv-project-screenshot.vue';
  export default {
    name: "personal-projects",
    components: {
      CvTerminal,
      CvProject,
      CvProjectScreenshots,
      CvProjectScreenshot,
    },
    head: function() {
      return {
        title: 'Work History',
      };
    },
    computed: {
      githubIcon: function() {
        return faGithub;
      },
    },
    data: function() {
      return {
        allTags: null,
        selectedTags: [],
      };
    },
    methods: {
      toggleTag: function(tag) {
        const idx = this.selectedTags.indexOf(tag);
        if(idx == -1) {
          this.selectedTags.push(tag);
        } else {
          this.selectedTags.splice(idx, 1);
        }
      },
    },
    mounted: function() {
      this.allTags = _.uniq(_.flatten(Array.from(iterChildren(this, 'cv-project')).map(project => project.tags))).sort();
    },
  }
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
