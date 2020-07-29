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

<script>
	const _ = require('lodash');

	import { faGithub, faGitlab } from '@fortawesome/free-brands-svg-icons';
	import { faBook, faColumns } from '@fortawesome/pro-regular-svg-icons';
	const repoSources = {
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

	import CvSubpage from '~/components/subpage.vue';
	export default {
		name: "cv-project",
		components: {
			CvSubpage,
		},
		props: ['project', 'name', 'tagline', 'mtime', 'tags', 'links'],
		computed: {
			personalProjects: function() {
				for(let seek = this.$parent; seek; seek = seek.$parent) {
					if(seek.selectedTags !== undefined) {
						return seek;
					}
				}
				throw "Unable to find root";
			},
			visible: function() {
				const selectedTags = this.personalProjects.selectedTags;
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
			repo: function() {
				if(this.links && this.links.repo) {
					const obj = _.isString(this.links.repo) ? {name: this.links.repo} : this.links.repo;
					if(obj.host && !repoSources[obj.host]) {
						throw `Unrecognized host: ${obj.host}`;
					}
					const host = obj.host || 'github';
					return {
						name: obj.name,
						hostKey: host,
						hostName: _.capitalize(host),
						icon: obj.icon || repoSources[host].icon,
						public: repoSources[host].public,
						url: `${repoSources[host].root}/${obj.name}`,
					};
				}
			},
			production: function() {
				if(this.links && this.links.production) {
					return {
						url: this.links.production,
						icon: faColumns,
					};
				}
			},
			docs: function() {
				if(this.links && this.links.docs) {
					return {
						url: this.links.docs,
						icon: faBook,
					};
				}
			},
		},
		provide: function() {
			return {
				project: this,
			};
		},
	}
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
