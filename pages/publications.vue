<template>
  <cv-terminal :prompts="['cd /publications', 'ls -lat **/*']">
    <cv-subpage path="SupportingCS1.pdf" :mtime="1173268800" description="Subverting the fundamentals sequence">
      <br>
      <a href="/papers/SupportingCS1.pdf" target="_blank">
        <img class="pdf" src="/papers/SupportingCS1.png">
      </a>
      <br><br>
      A paper about a pilot program I assisted with while a teaching assistant. The class used individual subversion repositories to manage student assignments: new assignments were committed by the professor, the work was committed by the students, and the grades were committed by me.<br><br>
      Submitted to the Special Interest Group on Computer Science Education (SIGCSE) and presented at the Annual Technical Symposium.
    </cv-subpage>
  </cv-terminal>
</template>

<script>
  import CvTerminal from '~/components/cv-terminal.vue';
  import CvSubpage from '~/components/cv-subpage.vue';
  export default {
    name: "publications",
    components: {
      CvTerminal,
      CvSubpage,
    },
    head: function() {
      return {
        title: 'Publications',
      };
    },
  }
</script>

<style lang="less" scoped>
  img.pdf {
    width: 350px;
    background-color: #fff;
  }
</style>
