<template>
  <cv-subpage :path="path" :mtime="mtime">
    <div class="job">
      <a v-if="url" target="_blank" :href="url">
        <img class="logo" :src="`/images/work/${logo}`">
      </a>
      <img v-else class="logo" :src="`/images/work/${logo}`">

      <div class="title">{{ title }}</div>
      <div class="timeframe">{{ timeframe }}</div>
      <br>
      <slot/>
    </div>
  </cv-subpage>
</template>

<script>
  import CvSubpage from '~/components/cv-subpage.vue';
  export default {
    name: "cv-work",
    components: {
      CvSubpage,
    },
    props: ['path', 'mtime', 'url', 'logo', 'title', 'timeframe'],
  }
</script>

<style lang="less" scoped>
  .job {
    img.logo {
      display: block;
      padding-top: 10px;
      margin-bottom: 20px;
      width: 300px;
    }

    .title {
      display: inline-block;
      font-weight: bold;
      width: 500px;
    }

    div.timeframe {
      display: inline-block;
    }
  }
</style>
