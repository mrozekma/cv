<template>
  <cv-terminal prompts="ls -la --sort=relevance" :paths="pages">
    <br>
    <cv-man cmd="cv" description="online portfolio">
      <h1>Description</h1>
      This is a more comprehensive version of my <nuxt-link to="make-pdf-resume">résumé</nuxt-link>. It has my unabridged <nuxt-link to="education">education</nuxt-link> and <nuxt-link to="work-history">work</nuxt-link> history, and vastly more information about my <nuxt-link to="personal-projects">personal projects</nuxt-link>, including source code, screenshots, and videos.<br><br>
      The site itself is a <a target="_blank" href="https://vuejs.org">Vue.js</a> single-page application powered by <a target="_blank" href="https://nuxtjs.org">Nuxt</a>. It's formatted like a terminal window because&hellip; well, I was bored. The links above navigate to each section of the portfolio; links within those sections jump down to the specified subsection. The <a href="#">..</a> link in each section comes back here, as does clicking the titlebar. The <a target="_blank" href="https://github.com/mrozekma/cv/blob/master/pages/index.vue" class="symlink">source</a> link on each page navigates to that page's source code. Any screenshots can be clicked to bring up a full-screen view with captions.
      <h1>Version</h1>
      This is <a target="_blank" :href="`https://github.com/mrozekma/cv/tree/${gitInfo.hash}`"><span class="desktop">{{ gitInfo.description }}</span><span class="mobile">{{ gitInfo.hash.substr(0, 7) }}</span></a>, last updated {{ gitInfo.commitDate }}.
    </cv-man>
  </cv-terminal>
</template>

<script>
  const pages = [
    {name: 'work-history',        bits: 'drx', mtime: 1543120144, description: "The places I've worked and the things I did while I was there"},
    {name: 'personal-projects',   bits: 'drx', mtime: 1477259577, description: "Things nobody paid me to do. Much more interesting, on the whole"},
    {name: 'education',           bits: 'drx', mtime: 1431910800, description: "Where I learned to do the above things"},
    {name: 'publications',        bits: 'drx', mtime: 1196560800, description: "Journal articles. Well, article"},
    // {name: 'hobbies',             bits: 'drx', mtime: 1477259577, description: "Occasionally I'm not at my computer"},
    '-',
    {name: 'make-pdf-resume',     bits: 'xs',  mtime: 1477259577, description: "This page isn't particularly printer-friendly"},
  ];

  import gitInfo from 'git-info!';
  import CvTerminal from '~/components/cv-terminal.vue';
  import CvMan from '~/components/cv-man.vue';
  export default {
    components: {CvTerminal, CvMan},
    head: function() {
      return {
        title: 'Michael Mrozek',
        titleTemplate: null,
      };
    },
    data: function() {
      return {pages, gitInfo};
    },
  };
</script>

<style lang="less" scoped>
  @import "../node_modules/animate.css/animate.css";

  .animated.quick {
    -webkit-animation-duration: 250ms;
    animation-duration: 250ms;
  }

  .full {
    height: 100%;
  }

  /deep/ .stdout {
    // The descriptions are pretty useful on the homepage, so if the screen is too small, show them below the links instead
    @media only screen and (min-width: 801px) and (max-width: 1223px) {
      position: relative;

      .file_entry {
        .description {
          position: absolute;
          left: calc(36ch);
          top: 0;
          white-space: normal;
        }
        &:hover .description {
          visibility: visible;
        }
      }
    }
  }

  a.symlink {
    color: #0ff;
  }
</style>
