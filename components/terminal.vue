<template>
	<div class="full">
		<div class="prompt mobile">export LAYOUT=mobile</div>
		<template v-if="promptList">
			<div v-for="prompt in promptList" class="prompt">{{ prompt }}</div><br>
		</template>
		<div v-if="annotatedPaths.length > 0" class="stdout">
			<div>total {{ formatSize(totalSize) }}</div>
			<div v-for="path in annotatedPaths" class="file_entry">
				<br v-if="path.name == '-'">
				<template v-else>
					<div class="metadata">{{ path.bits }}   {{ path.numLinks }} <div class="ownership">mrozekma mrozekma</div>  {{ path.sizeStr }} {{ path.mtimeStr }} </div>
					<a v-if="path.path.startsWith('#')" :href="path.path">{{ path.name }}</a>
					<a v-else-if="path.path.startsWith('http')" _target="_blank" :href="path.path" class="symlink">{{ path.name }}</a>
					<nuxt-link v-else :to="path.path">{{ path.name }}</nuxt-link>
					<template v-if="path.description">{{ path.descSpacer }}<div class="description">{{ path.description }}</div></template>
				</template>
			</div>
		</div>
		<slot/>
		<div class="end"></div>
	</div>
</template>

<script lang="ts">
	import Vue, { PropType } from 'vue';
	import _ from 'lodash';

	import { iterChildren } from '~/scripts/vue-hierarchy';
	import renderMtime from '~/scripts/mtime';

	export interface Path {
		name: string;
		path?: string;
		bits: string;
		mtime: number;
		description?: string;
		size?: number;
	}

	interface AnnotatedPath extends Path {
		path: string;
		size: number;

		isDir: boolean;
		numLinks: number;
		sizeStr: string;
		mtimeStr: string;
		descSpacer: string;
	}

	type PathOrSpacer = Path | '-';
	type AnnotatedPathOrSpacer = AnnotatedPath | { name: '-'; size: 0 }

	function isPath(path: PathOrSpacer): path is Path {
		return path !== '-';
	}

	import CvSubpage from './subpage.vue';

	export default Vue.extend({
		name: "cv-terminal",
		props: {
			prompts: {
				type: [ String, Array, Boolean ] as PropType<string | string[] | false>,
				required: true,
			},
			paths: {
				type: [ Boolean, Array ] as PropType<undefined | false | PathOrSpacer[]>,
				default: undefined,
			},
		},
		computed: {
			promptList(): string[] {
				return (this.prompts === false) ? [] : _.castArray<string>(this.prompts);
			},
			annotatedPaths(): AnnotatedPathOrSpacer[] {
				return (this.paths === false) ? [] : Array.from(this.annotatePaths(this.paths ?? this.dynamicPaths));
			},
			totalSize(): number {
				return this.annotatedPaths.map(path => path.size).reduce((total, num) => total + num);
			},
		},
		data() {
			return {
				dynamicPaths: [] as Path[],
			};
		},
		methods: {
			annotatePath(path: Path, maxPathLen: number): AnnotatedPath {
				const isDir = path.bits.includes('d');
				const ownerBits = path.bits.includes('s') ? 'rws' : 'rwx';
				const otherBits = ['r', 'w', 'x'].map(c => path.bits.includes(c) ? c : '-').join('');
				const size = (path.size !== undefined) ? path.size : isDir ? 4 * 1024 : 0;

				return {
					...path,
					path: path.path || path.name,
					isDir: isDir,
					bits: (isDir ? 'd' : '-') + ownerBits + otherBits + otherBits,
					numLinks: isDir ? 2 : 1,
					size: size,
					sizeStr: _.padStart(this.formatSize(size), 4, ' '),
					mtimeStr: renderMtime(path.mtime),
					descSpacer: ' '.repeat(Math.max(0, maxPathLen - path.name.length + 3)),
				};
			},
			*annotatePaths(paths: PathOrSpacer[]): IterableIterator<AnnotatedPathOrSpacer> {
				const route = this.$route;
				const maxPathLen = Math.max.apply(null, paths.map(path => isPath(path) ? path.name.length : 0));
				const latestMtime = Math.max.apply(null, paths.map(path => isPath(path) ? path.mtime : 0));

				yield this.annotatePath({ name: '.', path: '#', bits: 'drx', mtime: latestMtime }, maxPathLen);
				yield this.annotatePath({ name: '..', path: (route.name == 'index') ? '#' : '/', bits: 'drx', mtime: latestMtime }, maxPathLen);
				for(const path of paths) {
					if(path === '-') {
						yield { name: '-', size: 0 };
					} else {
						yield this.annotatePath(path, maxPathLen);
					}
				}
				yield this.annotatePath({ name: 'source', path: `https://github.com/mrozekma/cv/blob/master/pages/${route.name}.vue`, bits: 'rx', mtime: latestMtime, size: 6 }, maxPathLen);
			},
			formatSize(size: number): string {
				if(size < 1024) {
					return '' + size;
				} else {
					let mag, unit;
					if(size < 1024 * 1024) {
						mag = size / 1024;
						unit = 'K';
					} else {
						// Nothing larger than megabytes is expected or handled here
						mag = size / 1024 / 1024;
						unit = 'M';
					}
					if(mag < 10) {
						return mag.toFixed(1) + unit;
					} else {
						return Math.floor(mag) + unit;
					}
				}
			},
		},
		mounted() {
			if(this.paths === undefined) {
				this.dynamicPaths = Array.from(iterChildren(this, CvSubpage)).map<Path>(child => ({
					name: child.path,
					path: '#' + child.path,
					description: child.description,
					mtime: child.mtime,
					size: child.$el.innerHTML.length,
					bits: 'r',
				}));
				console.log(this.dynamicPaths.length);
			}
		}
	});
</script>

<style lang="less">
	.cv-terminal {
		height: 100%;
	}

	.prompt, .stdout {
		font-family: "Lucida Console", monospace;
		white-space: pre;

		&.desktop, .desktop {
			display: none;
		}

		@media only screen and (min-width: 800px) {
			&.desktop, .desktop {
				display: inline;
			}
			&.mobile, .mobile {
				display: none;
			}
		}
	}

	.prompt {
		&::before {
			content: "$ ";
		}

		a {
			color: #fff;
		}
	}
</style>

<style lang="less" scoped>
	.stdout .file_entry {
		display: block;

		.metadata {
			display: inline;
		}

		.ownership {
			display: none;
			@media only screen and (min-width: 1420px) {
				display: inline;
			}
		}

		.description {
			display: inline;
			visibility: hidden;
		}

		@media only screen and (min-width: 1224px) {
			&:hover .description {
				visibility: visible;
			}
		}

		a.symlink {
			color: #0ff;
		}

		@media only screen and (max-width: 799px) {
			margin-bottom: 10px;

			.metadata {
				display: none;
			}

			a {
				font-size: 2em;
			}

			.description {
				display: block;
				visibility: visible;
				white-space: normal;
				margin-left: 1ch;
			}
		}
	}
</style>
