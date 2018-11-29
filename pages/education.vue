<template>
  <cv-terminal :prompts="['cd /education', 'ls -lart by-school/']">
    <br>
    <div class="prompt">ls -lrt by-level/</div><br>
    <div class="stdout">
      <div v-for="link in symlinks" class="file_entry">lrwxr-xr-x   1 mrozekma mrozekma  {{ link.sizeStr }} {{ link.mtimeStr }} <a class="symlink" :href="`#${link.school}`">{{ link.level }}</a> -> <a :href="`#${link.school}`">{{ link.ln }}</a></div>
    </div>

    <cv-school
      school="purdue"
      level="master's"
      :mtime="1431882000"
      url="https://purdue.edu/"
      logo="purdue.png"
      degree="Master of Science in Computer Science"
      timeframe="2011 - 2015"
    >
      Continuing education while employed at <nuxt-link to="/work-history#microsemi">Microsemi</nuxt-link><br>
      Cumulative GPA: <em>3.67</em><br>
      Courses:
      <ul>
        <li v-for="course in [
          { id: 502, semester: 201120, name: 'Compiling and Programming Systems'},
          { id: 536, semester: 201210, name: 'Data Communication and Computer Networks'},
          { id: 555, semester: 201220, name: 'Cryptography'},
          { id: 503, semester: 201310, name: 'Operating Systems'},
          { id: 580, semester: 201320, name: 'Algorithm Design, Analysis, and Implementation'},
          { id: 526, semester: 201410, name: 'Information Security'},
          { id: 525, semester: 201420, name: 'Parallel Computing'},
          { id: 626, semester: 201420, name: 'Advanced Information Assurance'},
          { id: 505, semester: 201510, name: 'Distributed Systems'},
          { id: 565, semester: 201520, name: 'Programming Languages'},
        ].sort((a, b) => a.id - b.id)">
          <a target="_blank" :href="`https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.p_disp_course_detail?cat_term_in=${course.semester}&subj_code_in=CS&crse_numb_in=${course.id}00`"><em>CS{{ course.id }}</em> {{ course.name }}</a>
        </li>
      </ul>
    </cv-school>

    <cv-school
      school="rose-hulman"
      level="bachelor's"
      :mtime="1245085200"
      url="https://rose-hulman.edu/"
      logo="rose-hulman.png"
      degree="Bachelor of Science in Computer Science and Software Engineering"
      timeframe="2005 - 2009"
    >
      Cum Laude<br>
      Cumulative GPA: <em>3.48</em>&nbsp;&nbsp;&nbsp;&nbsp;Upperclass GPA: <em>3.70</em>
    </cv-school>

    <cv-school
      school="perry"
      level="high_school"
      :mtime="1118854800"
      url="http://www.perry-lake.k12.oh.us/"
      logo="perry.png"
      degree="High School"
      timeframe="2005 - 2009"
    >
      Graduate with Honors<br>
      Class rank: 3<br>
      National AP Scholar with Distinction
    </cv-school>
  </cv-terminal>
</template>

<script>
  import { iterChildren } from '~/scripts/vue-hierarchy';
  import renderMtime from '~/scripts/mtime.js';

  const _ = require('lodash');

  import CvTerminal from '~/components/cv-terminal.vue';
  import CvSchool from '~/components/cv-school.vue';
  export default {
    name: "education",
    components: {
      CvTerminal,
      CvSchool,
    },
    head: function() {
      return {
        title: 'Education',
      };
    },
    data: function() {
      return {
        symlinks: null,
      };
    },
    mounted: function() {
      this.symlinks = Array.from(iterChildren(this, 'cv-school')).map(child => ({
        school: child.school,
        level: child.level,
        mtimeStr: renderMtime(child.mtime),
        ln: `../by-school/${child.school}`,
        sizeStr: _.padStart(`../by-school/${child.school}`.length, 4, ' '),
      }));
    },
  }
</script>

<style lang="less" scoped>

</style>

