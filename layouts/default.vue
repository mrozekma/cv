<template>
	<!-- <link href="/fontawesome/css/all.css" rel="stylesheet" /> -->
	<div id="default">
		<div class="titlebar" @click="$router.push('/')">
			<div class="title">{{ title }}</div>
		</div>
		<div id="terminal">
			<!--<div id="reveal"></div>-->
			<nuxt/>
		</div>
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
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';

	import '../node_modules/photoswipe/dist/photoswipe.css';
	import '../node_modules/photoswipe/dist/default-skin/default-skin.css';

	export default Vue.extend({
		head() {
			return {
				titleTemplate: '%s - Michael Mrozek',
			};
		},
		computed: {
			title() {
				return (this.$route.name == 'index') ? '' : this.$route.name;
			}
		},
	});
</script>

<style lang="less">
	@import '../node_modules/animate.css/animate.css';
	@import '../node_modules/bootstrap-less/bootstrap/variables';
	@import '../node_modules/bootstrap-less/bootstrap/mixins/labels';
	@import '../node_modules/bootstrap-less/bootstrap/labels';

	.label {
		cursor: default;
		font-weight: normal;
		margin-right: 4px;
	}

	/*
	#reveal {
		height: ~"calc(100% - 22px - 4px - 60px)";
		width: ~"calc(100% - 50px)";
		background-color: #000;
		position: absolute;
		animation-duration: 5s;
		animation-name: slideOutDown;
		animation-fill-mode: forwards;
	}
	*/

	.animated.quick {
		-webkit-animation-duration: 250ms;
		animation-duration: 250ms;
	}

	* {
		box-sizing: border-box;
	}

	html {
		height: ~"calc(100% - 32px)";
	}

	body, #__nuxt, #__layout, #default, .full {
		height: 100%;
	}

	body {
		margin: 10px;
		background-color: #eee;
		color: #fff;
		border: 3px solid #888;
	}

	a {
		text-decoration: none;
		color: #66f; // #00f is a bit hard to read on the black terminal background
		&:hover {
			text-decoration: underline;
		}
	}

	// All civilized people agree that the proper way to emphasize text is with bold, not italics
	em {
		font-weight: bold;
		font-style: normal;
	}

	// Mostly copied from Stack Exchange's stylesheet, but fiddled a little bit
	kbd {
		display: inline-block;
		margin: 0 .1em;
		padding: .1em .6em;
		font-family: Arial,"Helvetica Neue",Helvetica,sans-serif;
		font-size: 11px;
		color: #242729;
		text-shadow: 0 1px 0 #FFF;
		background-color: #e1e3e5;
		border: 1px solid #adb3b9;
		border-radius: 3px;
		white-space: nowrap;
	}

	.titlebar {
		//TODO Not sure if terminal.png is free
		background: #ccc url(/images/terminal.png) no-repeat ~"1px/24px";
		padding-left: 25px;
		cursor: pointer;

		.title {
			margin: 2px;
			height: 22px;
			width: ~"calc(100% - 3px)";
			padding: 2px 0px 2px 4px;
			border: 2px solid #000;
			background-image: linear-gradient(#555, #888);
			display: inline-block;
			color: #fff;
			font-size: 8pt;

			&::before {
				content: "user@mrozekma.com:/";
			}
		}
	}

	#terminal {
		height: ~"calc(100% - 22px - 4px)";
		background-color: #000;
		padding: 4px;
		overflow-y: scroll;
		outline: none !important; // http://stackoverflow.com/a/11928222/309308
	}

	// I can't figure out how to disable overscroll, so instead minimize how bad it looks:
	body {
		overflow-y: hidden;
	}
	#default {
		background-color: #000;
	}
</style>
