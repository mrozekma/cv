const pkg = require('./package');

module.exports = {
	// mode: 'universal',
	mode: 'spa',

	/*
	** Headers of the page
	*/
	head: {
		title: 'Michael Mrozek',
		meta: [
			{ charset: 'utf-8' },
			{ name: 'viewport', content: 'width=device-width, initial-scale=1' },
			// { hid: 'description', name: 'description', content: pkg.description }
		],
		link: [
			{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
		]
	},

	/*
	** Customize the progress-bar color
	*/
	loading: { color: '#000' },

	/*
	** Global CSS
	*/
	css: [
		'@fortawesome/fontawesome-svg-core/styles.css',
	],

	/*
	** Plugins to load before mounting the App
	*/
	plugins: [
		'~/plugins/fontawesome.js',
	],

	/*
	** Nuxt.js modules
	*/
	modules: [
	],

	router: {
		// Scrolling is contained to the terminal element, not the whole page, so this handles scrolling that element
		//TODO Figure out how to restore the terminal scroll position (savedPosition will always be (0, 0))
		scrollBehavior: function(to, from, savedPosition) {
			const process = function() {
				if(to.hash) {
					document.getElementById(to.hash.substring(1)).scrollIntoView();
				} else {
					document.getElementById('terminal').scrollTo(0, 0);
				}
			};

			if(from.name == to.name) {
				process();
			} else {
				// Need to wait until after the transition to invoke process(). The transition's afterEnter hook looks for this variable on the Vue instance
				this.app.afterRouteFn = process;
			}
			return false;
		},
	},

	transition: {
		enterActiveClass: 'animated quick fadeInUp',
		leaveActiveClass: 'animated quick fadeOut',
		afterEnter: function(el) {
			if(this.$root.afterRouteFn) {
				this.$root.afterRouteFn();
				delete this.$root.afterRouteFn;
			}
		},
	},

	/*
	** Build configuration
	*/
	build: {
		/*
		** You can extend webpack config here
		*/
		extend(config, ctx) {
			config.resolveLoader.modules.push(`${config.resolve.alias['~']}/scripts`);
		},
	},
};
