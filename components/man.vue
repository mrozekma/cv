<template>
	<div class="man">
		<div class="prompt">man {{ section }} {{ cmd }}</div>
		<div class="stdout">
			<div class="header">
				<div>{{ cmd }}({{ section }})</div>
				<div>User commands</div>
				<div>{{ cmd }}({{ section }})</div>
			</div>
			<div class="body">
				<h1>Name</h1>
				{{ cmd }}<template v-if="description"> - {{ description }}</template>
				<slot/>
			</div>
		</div>
	</div>
</template>

<script>
	import Vue from 'vue';

	export default Vue.extend({
		name: "cv-man",
		props: {
			cmd: String,
			section: {
				type: Number,
				default: 7,
			},
			description: String,
		},
	});
</script>

<style lang="less" scoped>
.man {
	margin-right: 5ch;

	.header {
		display: flex;
		justify-content: space-between;
		margin-top: 1em;

		div:first-child, div:last-child {
			text-transform: uppercase;
		}
	}
	.body {
		white-space: normal;
		margin-left: 7ch;
		text-align: justify;
		// hyphens: auto; // Come on, Chrome, don't be like that

		h1 {
			margin: 0 0 0 -7ch;
			font-size: inherit;
			text-transform: uppercase;

			&:not(:first-child) {
				margin-top: 1em;
			}
		}
	}
}
</style>
