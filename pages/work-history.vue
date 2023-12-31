<template>
	<cv-terminal ref="term" :prompts="['cd /work-history', 'ls -lat **/*']">
		<cv-subpage path="README.1ST" :mtime="1477280113">
			<br>
			My work history is slightly confusing because of a series of company splits and acquisitions. The short version is that I've worked at the same place since my <a href="#pre-graduation/arxan">2008 internship</a>, despite the regular name changes:
			<ul>
				<li><div class="timeframe">Oct 2008</div> Arxan splits into Arxan Defense Systems and Arxan Technologies</li>
				<li><div class="timeframe">Sep 2010</div> Arxan Defense Systems is <a target="_blank" href="http://investor.microsemi.com/2010-09-15-Microsemi-Corporation-Acquires-Arxan-Defense-Systems-Inc">acquired</a> by Microsemi</li>
				<li><div class="timeframe">May 2016</div> The security division of Microsemi is <a target="_blank" href="https://www.mrcy.com/presscenter/pressreleases/pressrelease.aspx?id=16578">acquired</a> by Mercury Systems</li>
			</ul>
			The jobs predating this all took place during undergraduate or high school (and are stored in the <code>pre-graduation</code> directory).
		</cv-subpage>

		<cv-work path="mercury" :mtime="1532302550" url="https://www.mrcy.com/" logo="mercury.png" title="Senior Principal Software Engineer" timeframe="2016 - Present">
			<ul>
				<li>Designed and rolled out an automated build and test system for a number of projects.</li>
				<li>Handled the office migration to Atlassian tools, including moving all projects from Subversion to Bitbucket.
					<ul>
						<li>Implemented a <nuxt-link to="/personal-projects#got">tool</nuxt-link> to manage cross-repository dependencies in Bitbucket, and an <a target="_blank" href="https://marketplace.atlassian.com/apps/1218193/project-fields">addon</a> to track additional project information within Bitbucket.</li>
					</ul>
				</li>
				<li>Fully automated a recurring task needed by a customer, so it can now be done on demand in about 90 minutes.</li>
				<li>Fixed and redesigned large portions of an embedded system of interconnected Microblaze cores used by many customers.</li>
				<li>Assisted newer engineers with understanding tasks, solving problems, debugging issues, and generally answering questions about the system architecture and design.</li>
				<li>Approved pull requests before they could be merged and suggested fixes or improvements.</li>
				<li>Tested, packaged, and released many new versions of different projects.</li>
				<li>Handled communications for several programs, including answering customer questions, debugging issues, writing status reports, and releasing new versions to each customer.</li>
			</ul>
		</cv-work>

		<cv-work path="microsemi" :mtime="1462881600" url="http://www.microsemi.com/" logo="microsemi.png" title="Software Developer" timeframe="2010 - 2016">
			<ul>
				<li>Implemented and improved miscellaneous whitebox cryptography algorithms, including RSA, AES, and elliptic curve DSA.</li>
				<li>Developed an OpenSSL engine wrapping our whitebox cryptography implementations so they could be used by any application utilizing OpenSSL.</li>
				<li>Implemented the security model and key management policy for an Android password manager.</li>
				<li>Designed and implemented multiple higher level protocols wrapping existing whitebox cryptography to satisfy customer needs.</li>
				<li><span class="hover" v-tooltip="`A security assessment performed without the customer's help, mimicking the situation a real attacker would be in.`">Red-</span> and <span class="hover" v-tooltip="`A security assessment performed with the customer's help, including access to background information, design documents, and possibly even source code.`">blue-teamed</span> several devices, finding a number of vulnerabilities. Wrote large portions of the final reports detailing the vulnerabilities, their severity, and potential mitigations and fixes.</li>
			</ul>
		</cv-work>

		<cv-work path="arxan-defense-systems" :mtime="1289390400" logo="arxan_defense_systems.png" title="Software Security Analyst" timeframe="2009 - 2010">
			<ul>
				<li>Implemented many features in <a target="_blank" href="http://www.microsemi.com/products/information-assurance/softwareanti-tamper/codeseal">CodeSEAL</a>, a product that analyzes executables and modifies them to protect against reverse engineering or modification.</li>
				<li>Developed <a target="_blank" href="http://www.microsemi.com/products/information-assurance/cryptography/whiteboxcrypto">WhiteboxRSA</a>, an RSA implementation that hides the key to frustrate recovery even when the implementation is fully under the attacker's control.</li>
			</ul>
		</cv-work>

		<cv-work path="pre-graduation/arxan" :mtime="1245672000" logo="arxan.png" title="Intern" timeframe="2008 - 2009">
			<ul>
				<li>Engineering intern on a team that developed <em>TransformIT</em>, a white box cryptography solution.</li>
				<li>Subsequently accepted an opportunity to continue work remotely during the school year before transitioning to full-time employment after graduation.</li>
			</ul>
		</cv-work>

		<cv-work path="pre-graduation/ventures" :mtime="1212148800" url="http://www.rhventures.org/" logo="ventures.png" title="Team Lead" timeframe="2007 - 2008">
			<ul>
				<li>Head of a team of students that specified, designed, developed, and launched the web portal for a promising online startup company.</li>
				<li>Handled maintenance of development servers and software.</li>
				<li>Maintained source code repository and bug tracking system.</li>
				<li>Reviewed code produced by other team members.</li>
			</ul>
		</cv-work>

		<cv-work path="pre-graduation/rose-hulman" :mtime="1244635200" url="http://www.rose-hulman.edu/" logo="rose-hulman.png" title="Teaching Assistant, CSSE Newsletter Editor" timeframe="2005 - 2008">
			<ul>
				<li>Assisted students in many introductory programming classes with fundamental object-oriented techniques, UML, project planning, and completing team-based goals.</li>
				<li>Responsible for all phases of the CSSE newsletter production, from writing to publishing.</li>
			</ul>
		</cv-work>

		<cv-work path="pre-graduation/perry-schools" :mtime="1180612800" url="http://www.perry-lake.k12.oh.us/" logo="perry.png" title="Website Designer, Technician, Database Administrator" timeframe="2001 - 2007">
			<ul>
				<li>Project coordinator that designed and implemented a completely new look and feel for the school district's 5000+ page website, including a custom CMS and DB design.</li>
				<li>Converted all existing webpages to a new format and implemented a new, more efficient interface.</li>
				<li>Designed, implemented, and maintained the school's first online course registration system.</li>
			</ul>
		</cv-work>

		<cv-work path="pre-graduation/perritech" :mtime="1117540800" logo="perritech.png" title="President, Technician" timeframe="2001 - 2005">
			<ul>
				<li>Recruited in 2001 as a computer technician, responsible for the 2000+ computer network.</li>
				<li>Subcontracted to various local businesses for programming, website design, networking and system administration.</li>
				<li>Promoted to President in 2005, managing four directors and a number of technicians.</li>
				<li>Spearheaded a presentation at the Ohio State SchoolNet Convention illustrating the benefits of a student-run technology company fully executed within a school district. Subsequently invited to Seoul, Korea for the 6th Global Forum to make a detailed presentation on how to duplicate our success throughout many school districts.</li>
			</ul>
		</cv-work>
	</cv-terminal>
</template>

<script lang="ts">
	import Vue from 'vue';
	//@ts-ignore No declaration file
	import Tooltip from 'vue-directive-tooltip';
	import 'vue-directive-tooltip/dist/vueDirectiveTooltip.css';
	Vue.use(Tooltip, {
		delay: 0,
	});

	import CvTerminal from '~/components/terminal.vue';
	import CvSubpage from '~/components/subpage.vue';
	import CvWork from '~/components/work.vue';
	export default Vue.extend({
		name: "work-history",
		components: { CvTerminal, CvSubpage, CvWork },
		head() {
			return {
				title: 'Work History',
			};
		},
	});
</script>

<style lang="less" scoped>
	ul li div.timeframe {
		display: inline-block;
		font-weight: bold;
		min-width: 80px;
	}

	.hover {
		cursor: default;
		color: #66f;
	}
</style>

<style lang="less">
	.vue-tooltip {
		background-color: #505050;
		border-color: #303030;
		color: #f3f3f3;

		.tooltip-arrow {
			display: none;
		}
	}
</style>
