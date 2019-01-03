<template>
  <cv-terminal prompts="ls -la --sort=relevance" :paths="pages"/>
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

<style>
  @import "../node_modules/animate.css/animate.css";

  .animated.quick {
    -webkit-animation-duration: 250ms;
    animation-duration: 250ms;
  }

  .full {
    height: 100%;
  }

  /*
  .page-enter-active {
    animation: acrossIn .40s ease-out both;
  }
  .page-leave-active {
    animation: acrossOut .60s ease-in both;
  }
  @keyframes acrossIn {
    0% {
      transform: translate3d(-100%, 0, 0);
    }
    100% {
      transform: translate3d(0, 0, 0);
    }
  }
  @keyframes acrossOut {
    0% {
      transform: translate3d(0, 0, 0);
    }
    100% {
      transform: translate3d(100%, 0, 0);
    }
  }
  */
</style>
