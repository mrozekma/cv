<template>
  <cv-terminal prompts="ls -la --sort=relevance" :paths="pages" :style="{'--line-count': pages.length}"/>
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

  import CvTerminal from '~/components/cv-terminal.vue';
  export default {
    components: {
      CvTerminal,
    },
    head: function() {
      return {
        title: 'Michael Mrozek',
        titleTemplate: null,
      };
    },
    data: function() {
      return {pages};
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
    line-height: 1.2;

    // The descriptions are pretty useful on the homepage, so if the screen is too small, show them below the links instead
    // This is very inelegant, but I can't think of a better pure-CSS way to do it
    @media only screen and (min-width: 801px) and (max-width: 1223px) {
      .file_entry {
        .description {
          position: absolute;
          left: calc(16px + 36ch); // The metadata is 36 characters long (at this size, anyway)
          top: calc(39px + (4em + 2em + var(--line-count) * 1em + 1em) * 1.2); // 4 lines for the command and total count, 2 for '.' and '..', 1 for each page, and 1 more to leave a blank line before the description. All multiplied by the line-height
          white-space: normal;
        }
        &:hover .description {
          visibility: visible;
        }
      }
    }
  }
</style>
