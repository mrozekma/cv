<template>
	<cv-subpage :path="school" :mtime="mtime" :catName="`by-school/${school}`">
		<div class="school">
			<a v-if="url" target="_blank" :href="url">
				<img class="logo" :src="`/images/education/${logo}`">
			</a>
			<img v-else class="logo" :src="`/images/education/${logo}`">

			<div class="degree">{{ degree }}</div>
			<div class="timeframe">{{ timeframe }}</div>
			<br>
			<slot/>
		</div>
	</cv-subpage>
</template>

<script lang="ts">
	import Vue from 'vue';

	import CvSubpage from '~/components/subpage.vue';
	export default Vue.extend({
		name: "cv-school",
		components: { CvSubpage },
		props: {
			'school': String,
			'level': String,
			'mtime': Number,
			'url': String,
			'logo': String,
			'degree': String,
			'timeframe': String,
		},
	});
</script>

<style lang="less" scoped>
	.school {
		img.logo {
			display: block;
			padding-top: 10px;
			margin-bottom: 20px;
			width: 300px;
		}

		.degree {
			display: inline-block;
			font-weight: bold;
			width: 600px;
		}

		div.timeframe {
			display: inline-block;
		}
	}
</style>
