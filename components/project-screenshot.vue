<template>
	<div class="screenshot">
		<img :src="src" @click="clicked">
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';

	import { Project } from './project.vue';
	import { ProjectScreenshots } from './project-screenshots.vue';
	const components = Vue.extend({
		name: "cv-project-screenshot",
		props: [ 'name' ],
		inject: [ 'project', 'screenshots' ],
		computed: {
			src(): string {
				const project = (this as any).project as Project;
				const screenshots = (this as any).screenshots as ProjectScreenshots;
				return `/images/projects/${project.project}/${this.name}.${screenshots.dims[this.name].type}`;
			},
			description(): string {
				return this.$slots.default?.[0].text?.trim() ?? '';
			},
		},
		methods: {
			clicked() {
				const screenshots = (this as any).screenshots as ProjectScreenshots;
				screenshots.show(this.name);
			}
		},
	});
	export default components;
	export type ProjectScreenshot = InstanceType<typeof components>;
</script>
