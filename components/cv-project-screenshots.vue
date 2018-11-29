<template>
  <div class="screenshots">
    <slot/>
  </div>
</template>

<script>
  import PhotoSwipe from '../node_modules/photoswipe/dist/photoswipe.js';
  import PhotoSwipeUI_Default from '../node_modules/photoswipe/dist/photoswipe-ui-default';
  import '../node_modules/photoswipe/dist/photoswipe.css';
  import '../node_modules/photoswipe/dist/default-skin/default-skin.css';

  import { findParent } from '~/scripts/vue-hierarchy.js';
  import allDims from 'project-screenshots!'; // See ~/scripts/project-screenshots.js

  export default {
    name: "cv-project-screenshots",
    computed: {
      dims: function() {
        return allDims[findParent(this, 'cv-project').project];
      }
    },
    data: function() {
      return {
        photoswipeItems: null,
      };
    },
    methods: {
      show: function(name) {
        const opts = {
          index: this.$children.map(child => child.name).indexOf(name),
          history: false,
        };
        new PhotoSwipe(document.querySelectorAll('.pswp')[0], PhotoSwipeUI_Default, this.photoswipeItems, opts).init();
      }
    },
    mounted: function() {
      this.photoswipeItems = this.$children.map(child => ({
        src: child.src,
        w: this.dims[child.name].width,
        h: this.dims[child.name].height,
        title: child.description,
      }));
    },
  }
</script>

<style lang="less" scoped>
  // The desired layout is one double-tall image on the left, and two rows of images on the right. The number of images is based on the width of the window (we never want more than two rows, since that's all that will fit next to the image on the left)

  @screenshot-height: 200px;
  @screenshot-width: 310px;
  @screenshot-space: 5px;
  @screenshot-max: 13;

  .screenshots {
    margin: 10px auto;
    position: relative;
    height: @screenshot-height * 2 + @screenshot-space;

    /deep/ .screenshot {
      display: none;
      position: absolute;
      vertical-align: top;
      overflow-x: hidden;
      max-width: @screenshot-width;
      cursor: pointer;

      img {
        display: block;
        margin: 0px;
        height: @screenshot-height;
      }

      // First image is double-tall
      &:first-child {
        display: inline-block;
        top: 0px;
        left: 0px;
        padding-left: 0px;
        max-width: @screenshot-width * 2;
        img {
          height: @screenshot-height * 2 + @screenshot-space;
        }
      }

      // Decide how many other images to show based on browser width
      .loop(@num: 1) when (@num =< @screenshot-max) {
        // I can't figure out a way to do math without temporary variables
        @col: (@num - 1) / 2;
        @numPlusOne: @num + 1;
        @numPlusTwo: @num + 2;
        // Skip @screenshot-width * 2 for the width of the first image
        // Skip @screenshot-space + @screenshot-width for each preceding column
        // Skip @screenshot-space for the space between the previous column and this one
        @left: @screenshot-width * 2 + @col * (@screenshot-space + @screenshot-width) + @screenshot-space;

        &:nth-child(@{numPlusOne}) {
          left: @left;
        }
        &:nth-child(@{numPlusTwo}) {
          left: @left;
          top: @screenshot-height + @screenshot-space;
        }

        @minWidth: (75px + @left + @screenshot-width);
        @media(min-width: @minWidth) {
          &:nth-child(@{numPlusOne}), &:nth-child(@{numPlusTwo}) {
            display: inline-block;
          }
        }
        .loop(@num + 2);
      }
      .loop;
    }
  }
</style>
