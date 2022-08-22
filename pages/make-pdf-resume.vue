<template>
	<cv-terminal :prompts="false" :paths="false">
		<cv-man cmd="make-pdf-resume" description="PDF generator">
			<h1>Description</h1>
			This tool generates a PDF containing a more traditional résumé. Which sections to include and omit can be customized as desired, but the default values are sane and have been chosen to fit within a single page.
			<h1>Acknowledgements</h1>
			Thanks to Byungjin Park for the use of the <a target="_blank" href="https://github.com/posquit0/Awesome-CV">Awesome CV</a> LaTeX document class.
		</cv-man>
		<br>
		<div class="prompt">export NCURSES=1</div>
		<div class="prompt">make-pdf-resume</div>
		<div class="pdf-generator">
			<div class="title"><input type="checkbox" :checked="allChecked" :indeterminate.prop="!allChecked" @click="toggleRoot">&nbsp;PDF Generator</div>
			<form action="/cgi-bin/pdf.py/resume.pdf"> <!-- The actual script is pdf.py, but we want the filename to be resume.pdf -->
				<input type="hidden" name="background" value="on"/>
				<ul>
					<li><input type="checkbox" checked disabled> Background</li>
					<li v-for="section in sections">
						<input type="checkbox" :id="`chk-${section.key}`" :name="section.key" v-bind.prop="sectionState(section)" @click="toggleSection(section)">&nbsp;<label :for="`chk-${section.key}`">{{ section.name }}</label>
						<ul>
							<li v-for="entry in section.entries">
								<input type="checkbox" :id="`chk-${entry.key}`" :name="entry.key" v-model="entry.checked">&nbsp;<label :for="`chk-${entry.key}`">{{ entry.name }}</label>
							</li>
						</ul>
					</li>
				</ul>
				<div class="buttons">
					<button id="go-button" type="submit">Go</button>
					<nuxt-link tag="button" id="cancel-button" to="/">Cancel</nuxt-link>
				</div>
			</form>
		</div>
		<div class="clear"></div><br>
	</cv-terminal>
</template>

<script lang="ts">
	import Vue from 'vue';

	interface Section {
		name: string;
		entries: {
			name: string;
			checked?: boolean;
		}[];
	}

	const sections: Section[] = [
		{
			name: 'Technical Skills',
			entries: [
				{ name: 'Languages and Frameworks' },
				{ name: 'Tools' },
			],
		},
		{
			name: 'Experience',
			entries: [
				{ name: 'Mercury' },
				{ name: 'Microsemi' },
				{ name: 'Arxan Defense Systems' },
				{ name: 'Arxan', checked: false },
				{ name: 'Rose-Hulman', checked: false },
				{ name: 'Ventures', checked: false },
				{ name: 'Perry Schools', checked: false },
				{ name: 'Perritech', checked: false },
			],
		},
		{
			name: 'Education',
			entries: [
				{ name: 'Masters' },
				{ name: 'Bachelors' },
				{ name: 'High School', checked: false },
			],
		},
		{
			name: 'Projects',
			entries: [
				{ name: 'Serial Bridge' },
				{ name: 'Chalk' },
				{ name: 'Point Vote' },
				{ name: 'Ninja' },
				{ name: 'Sprint' },
				{ name: 'Noisebot' },
				{ name: 'Spades', checked: false },
				{ name: 'Got', checked: false },
				{ name: 'Lync Helper', checked: false },
				{ name: 'Gir', checked: false },
				{ name: 'Woop', checked: false },
			],
		},
		{
			name: 'Publications',
			entries: [
				{ name: 'Subverting the Fundamentals Sequence', checked: false },
			],
		},
	];

	// Foo Bar Baz -> foo-bar-baz
	function makeFormName(text: string) {
		return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+/, '').replace(/-+$/, '');
	}

	import CvTerminal from '~/components/terminal.vue';
	import CvMan from '~/components/man.vue';
	export default Vue.extend({
		name: "make-pdf-resume",
		components: { CvTerminal, CvMan },
		head() {
			return {
				title: 'PDF',
			};
		},
		computed: {
			allChecked(): boolean {
				return this.sections.every(section => section.entries.every(entry => entry.checked));
			},
		},
		data() {
			return {
				sections: sections.map(section => ({
					name: section.name,
					key: makeFormName(section.name),
					entries: section.entries.map(entry => ({
						name: entry.name,
						key: makeFormName(entry.name),
						checked: (entry.checked !== false),
					})),
				})),
			};
		},
		methods: {
			sectionState(section: Section) {
				const all = section.entries.every(entry => entry.checked);
				const some = section.entries.some(entry => entry.checked);
				return {
					checked: some,
					indeterminate: some && !all,
				};
			},
			toggleSection(section: Section) {
				const newState = !section.entries.every(entry => entry.checked);
				for(const entry of section.entries) {
					entry.checked = newState;
				}
			},
			toggleRoot() {
				const newState = !this.allChecked;
				for(const section of this.sections) {
					for(const entry of section.entries) {
						entry.checked = newState;
					}
				}
			},
		},
	});
</script>

<style lang="less" scoped>
	.pdf-generator {
		display: inline-block;
		margin: 10px 0 0 3px;
		border: 1px solid #fff;
		width: 400px;

		.title {
			color: #000;
			background-color: #fff;
			font-size: 1.25em;
			font-weight: bold;
			font-variant: small-caps;
			text-align: center;
		}

		ul {
			list-style-type: none;
		}

		label {
			cursor: pointer;
		}

		.buttons {
			border-top: 1px solid #fff;
			padding: 10px;
			margin-bottom: 20px;

			button {
				cursor: pointer;
				background-color: #f5f5f5;
				border: 1px solid #dedede;
				border-top: 1px solid #eee;
				border-left: 1px solid #eee;
				font-family: "Lucida Grande", Tahoma, Arial, Verdana, sans-serif;

				&#go-button {
					width: 65%;
					font-weight: bold;
					float: left;
					background-color: #28a745;
					border-color: #28a745;

					&:hover {
						background-color: #218838;
						border-color: #1e7e34;
					}
				}

				&#cancel-button {
					width: 25%;
					float: right;

					&:hover {
						background-color: #dff4ff;
						border: 1px solid #c2e1ef;
						color: #336699;
					}
				}
			}
		}

		.clear {
			clear: both;
		}
	}

	#terminal .stdout {
		white-space: normal !important;
	}
</style>
