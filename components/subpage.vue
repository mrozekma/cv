<template>
	<div :id="path" class="subpage">
		<a :name="path"></a>
		<div class="prompt"><a :href="`#${path}`">cat {{ catName }}</a></div>
		<div class="stdout">
			<slot/>
		</div>
	</div>
</template>

<script lang="ts">
	import Vue from 'vue';

	const component = Vue.extend({
		name: "cv-subpage",
		props: {
			path: {
				type: String,
				// required: true,
			},
			mtime: {
				type: Number,
				// required: true,
			},
			catName: {
				type: String,
				default() {
					return this.path;
				},
			},
			description: {
				type: String,
			},
		},
	});
	export default component;
	export type Subpage = InstanceType<typeof component>;
</script>

<style lang="less">
	// Add quite a bit of space after the last subpage so it can be scrolled to the top, but not quite 100% to avoid End taking you to a blank screen
	.subpage ~ .end {
		height: ~"calc(100% - 100px)";
	}
</style>

<style lang="less" scoped>
	.subpage {
		margin-top: 75px;

		.stdout {
			@border-width: 1px;

			position: relative;
			margin-left: 4px;
			padding: 0 10px 10px 16px;
			font-family: "Arial";
			white-space: normal;
			text-align: justify;
			border-left: @border-width solid #fff;

			// Truncated bottom border. http://stackoverflow.com/a/12801460/309308
			&:after {
				content: "";
				background: #fff;
				position: absolute;
				bottom: 0;
				left: 0;
				height: @border-width;
				width: 16px;
			}
		}
	}
</style>
