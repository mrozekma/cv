<template>
	<div class="screenshot">
		<img :src="src" @click="clicked">
	</div>
</template>

<script>
	export default {
		name: "cv-project-screenshot",
		props: ['name'],
		inject: ['project', 'screenshots'],
		computed: {
			src: function() {
				return `/images/projects/${this.project.project}/${this.name}.${this.screenshots.dims[this.name].type}`;
			},
			description: function() {
				return this.$slots.default[0].text.trim();
			},
		},
		methods: {
			clicked: function() {
				this.screenshots.show(this.name);
			}
		},
	}
</script>
