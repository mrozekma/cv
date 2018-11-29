<template>
  <div class="screenshot">
    <img :src="src" @click="clicked">
  </div>
</template>

<script>
  import { findParent } from '~/scripts/vue-hierarchy.js';

  export default {
    name: "cv-project-screenshot",
    props: ['name'],
    computed: {
      src: function() {
        return `/images/projects/${this.project.project}/${this.name}.${this.screenshotsWrapper.dims[this.name].type}`
      },
      description: function() {
        return this.$slots.default[0].text.trim();
      },
      screenshotsWrapper: function() {
        return findParent(this, 'cv-project-screenshots');
      },
      project: function() {
        return findParent(this, 'cv-project');
      },
    },
    methods: {
      clicked: function() {
        this.screenshotsWrapper.show(this.name);
      }
    },
  }
</script>
