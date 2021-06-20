<template>
	<cv-subpage v-if="visible" :path="project" :mtime="mtime" :description="tagline">
		<div class="name">{{ name }}</div>
		<div class="tagline">{{ tagline }}</div>
		<div class="project-filters">
			<span v-for="tag in tags" class="label label-default">{{ tag }}</span>
		</div>
		<div v-if="links" class="project-links">
			<a v-if="repo" :class="`${repo.hostKey}-link`" target="_blank" :href="repo.url">
				<font-awesome-icon :icon="repo.icon"/>&nbsp;{{ repo.hostName }} repository
			</a>
			<template v-if="!repo.public">(private, but available on request)</template>
			<a v-if="production" class="prod-link" target="_blank" :href="production.url">
				<font-awesome-icon :icon="production.icon"/>&nbsp;Live website
			</a>
			<a v-if="docs" class="doc-link" target="_blank" :href="docs.url">
				<font-awesome-icon :icon="docs.icon"/>&nbsp;Documentation
			</a>
		</div>
		<slot/>
	</cv-subpage>
</template>

<script lang="ts">
	import Vue, { PropType } from 'vue';
	import _ from 'lodash';

	type RepoSourceName = 'github' | 'gitlab';
	interface RepoSource {
		root: string;
		icon: IconDefinition;
		public: boolean;
	}

	interface Links {
		repo?: RepoSourceName | {
			host?: RepoSourceName;
			name: string;
			icon?: IconDefinition;
		};
		production?: string;
		docs?: string;
	}

	interface Link {
		url: string;
		icon: IconDefinition;
	}

	interface RepoLink extends Link {
		name: string;
		hostKey: string;
		hostName: string;
		public: boolean;
	}

	import { faGithub, faGitlab, IconDefinition } from '@fortawesome/free-brands-svg-icons';
	import { faBook, faColumns } from '@fortawesome/pro-regular-svg-icons';
	const repoSources: {
		[ K: /* RepoSourceName */ string ]: RepoSource
	} = {
		github: {
			root: 'https://github.com/mrozekma',
			icon: faGithub,
			public: true,
		},
		gitlab: {
			root: 'https://gitlab.com/mrozekma',
			icon: faGitlab,
			public: false,
		},
	};

	import { findParent } from '~/scripts/vue-hierarchy';
	import CvPersonalProjects from '~/pages/personal-projects.vue';
	import CvSubpage from '~/components/subpage.vue';
	const component = Vue.extend({
		name: "cv-project",
		components: { CvSubpage },
		props: {
			'project': String,
			'name': String,
			'tagline': String,
			'mtime': Number,
			'tags': Array as PropType<string[]>,
			'links': Object as PropType<Links>,
		},
		computed: {
			visible(): boolean {
				const personalProjects = findParent(this, CvPersonalProjects);
				const selectedTags = personalProjects.selectedTags;
				if(selectedTags.length == 0) {
					return true;
				}
				for(const tag of selectedTags) {
					if(!this.tags.includes(tag)) {
						return false;
					}
				}
				return true;
			},
			repo(): RepoLink | undefined {
				if(this.links?.repo) {
					const obj = _.isString(this.links.repo) ? { name: this.links.repo } : this.links.repo;
					if(obj.host && !repoSources[obj.host]) {
						throw `Unrecognized host: ${obj.host}`;
					}
					const host = obj.host || 'github';
					return {
						name: obj.name,
						hostKey: host,
						hostName: _.capitalize(host),
						icon: obj.icon ?? repoSources[host].icon,
						public: repoSources[host].public,
						url: `${repoSources[host].root}/${obj.name}`,
					};
				}
			},
			production(): Link | undefined {
				if(this.links?.production) {
					return {
						url: this.links.production,
						icon: faColumns,
					};
				}
			},
			docs(): Link | undefined {
				if(this.links?.docs) {
					return {
						url: this.links.docs,
						icon: faBook,
					};
				}
			},
		},
		provide(): any {
			return {
				project: this,
			};
		},
	});
	export default component;
	export type Project = InstanceType<typeof component>;
</script>

<style lang="less" scoped>
	.stdout.project-tags {
		margin: 0 0 20px 20px;

		.label {
			font-weight: normal;
			margin-right: 4px;
			cursor: pointer;

			&.selected {
				background-color: #c00;
			}
		}
	}

	.tag-filter {
		display: none;

		.prompt .tag-list {
			display: inline;
		}
	}

	.subpage .stdout {
		.name {
			display: inline-block;
			margin-top: 10px;
			font-size: 2em;
			font-weight: bold;
		}

		.tagline {
			display: inline-block;
			margin-left: 5px;
			text-transform: lowercase;
		}

		.project-filters {
			display: inline-block;
			margin-left: 20px;
		}

		.project-links a {
			margin-right: 15px;
		}

		a.github-link, a.gitlab-link, a.prod-link, a.doc-link {
			display: inline-block;

			.fa {
				color: #fff;
			}
		}

		.description {
			text-align: justify;
			text-justify: distribute;
			margin-right: 20px;
			line-height: 1.2em;
		}
	}
</style>
