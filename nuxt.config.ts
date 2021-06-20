import { spawnSync } from 'child_process';
import fs from 'fs';
import { imageSize } from 'image-size';
import moment from 'moment';
import webpack from 'webpack'

export interface GitInfo {
	description: string;
	hash: string;
	commitDate: string;
}

export interface Dimensions {
	[ dir: string ]: {
		[ subdir: string ]: DimensionsByFilename;
	}
}

export interface DimensionsByFilename {
	[ filename: string ]: {
		width: number;
		height: number;
		type: string;
	}
}

const screenshotRoot = 'static/images';
const screenshotDirs = [ 'projects' ];

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

	buildModules: [
		'@nuxt/typescript-build',
	],

	pageTransition: {
		enterActiveClass: 'animated quick fadeInUp',
		leaveActiveClass: 'animated quick fadeOut',
		afterEnter() {
			const root = (this as any).$root;
			if(root.afterRouteFn) {
				root.afterRouteFn();
				delete root.afterRouteFn;
			}
		},
	},

	/*
	** Build configuration
	*/
	build: {
		plugins: [
			new webpack.DefinePlugin({
				'GIT_INFO': webpack.DefinePlugin.runtimeValue(() => {
					const desc = spawnSync('git', [ 'describe', '--all', '--long', '--abbrev=40', '--dirty' ], { encoding: 'utf8' }).stdout.trim();
					const [ hash, ts ] = spawnSync('git', [ 'show', '-s', '--format=%H %ct' ], { encoding: 'utf8' }).stdout.trim().split(' ');

					const rtn: GitInfo = {
						description: desc.replace(/^heads\//, ''),
						hash: hash,
						commitDate: moment(parseInt(ts) * 1000).format('MMMM Do, YYYY'),
					};
					return JSON.stringify(rtn);
				}, true),
				'SCREENSHOT_DIMS': webpack.DefinePlugin.runtimeValue(() => {
					let rtn: Dimensions = {};
					for(const dir of screenshotDirs) {
						const root = `${screenshotRoot}/${dir}`;
						rtn[dir] = {};
						for(const subdir of fs.readdirSync(root)) {
							const dims: DimensionsByFilename = rtn[dir][subdir] = {};
							for(const filename of fs.readdirSync(`${root}/${subdir}`)) {
								const { width, height, type } = imageSize(`${root}/${subdir}/${filename}`);
								dims[filename.replace(/\.[^.]+$/, '')] = { width: width!, height: height!, type: type! };
							}
						}
					}
					return JSON.stringify(rtn);
				}, screenshotDirs.map(dir => `${screenshotRoot}/${dir}`)),
			}),
		],
	},
};
