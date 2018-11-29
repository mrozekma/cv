<template>
  <div id="default">
    <div class="titlebar" @click="$router.push('/')">
      <div class="title">{{ title }}</div>
    </div>
    <div id="terminal">
      <!--<div id="reveal"></div>-->
      <nuxt/>
    </div>
  </div>
</template>

<script>
  export default {
    head: function() {
      return {
        titleTemplate: '%s - Michael Mrozek',
      };
    },
    computed: {
      title: function() {
        return (this.$route.name == 'index') ? '' : this.$route.name;
      }
    },
  };
</script>

<style lang="less">
  @import '../node_modules/animate.css/animate.css';
  @import '../node_modules/bootstrap-less/bootstrap/variables';
  @import '../node_modules/bootstrap-less/bootstrap/mixins/labels';
  @import '../node_modules/bootstrap-less/bootstrap/labels';

  .label {
    cursor: default;
    font-weight: normal;
    margin-right: 4px;
  }

  /*
  #reveal {
    height: ~"calc(100% - 22px - 4px - 60px)";
    width: ~"calc(100% - 50px)";
    background-color: #000;
    position: absolute;
    animation-duration: 5s;
    animation-name: slideOutDown;
    animation-fill-mode: forwards;
  }
  */

  .animated.quick {
    -webkit-animation-duration: 250ms;
    animation-duration: 250ms;
  }

  * {
    box-sizing: border-box;
  }

  html {
    height: ~"calc(100% - 32px)";
  }

  body, #__nuxt, #__layout, #default, .full {
    height: 100%;
  }

  body {
    margin: 10px;
    background-color: #eee;
    color: #fff;
    border: 3px solid #888;
  }

  a {
    text-decoration: none;
    color: #66f; // #00f is a bit hard to read on the black terminal background
    &:hover {
      text-decoration: underline;
    }
  }

  // All civilized people agree that the proper way to emphasize text is with bold, not italics
  em {
    font-weight: bold;
    font-style: normal;
  }

  // Mostly copied from Stack Exchange's stylesheet, but fiddled a little bit
  kbd {
    display: inline-block;
    margin: 0 .1em;
    padding: .1em .6em;
    font-family: Arial,"Helvetica Neue",Helvetica,sans-serif;
    font-size: 11px;
    color: #242729;
    text-shadow: 0 1px 0 #FFF;
    background-color: #e1e3e5;
    border: 1px solid #adb3b9;
    border-radius: 3px;
    white-space: nowrap;
  }

  .titlebar {
    //TODO Not sure if terminal.png is free
    background: #ccc url(/images/terminal.png) no-repeat ~"1px/24px";
    padding-left: 25px;
    cursor: pointer;

    .title {
      margin: 2px;
      height: 22px;
      width: ~"calc(100% - 3px)";
      padding: 2px 0px 2px 4px;
      border: 2px solid #000;
      background-image: linear-gradient(#555, #888);
      display: inline-block;
      color: #fff;
      font-size: 8pt;

      &::before {
        content: "user@mrozekma.com:/";
      }
    }
  }

  #terminal {
    height: ~"calc(100% - 22px - 4px)";
    background-color: #000;
    padding: 4px;
    overflow-y: scroll;
    outline: none !important; // http://stackoverflow.com/a/11928222/309308
  }

  // I can't figure out how to disable overscroll, so instead minimize how bad it looks:
  body {
    overflow-y: hidden;
  }
  #default {
    background-color: #000;
  }
</style>
