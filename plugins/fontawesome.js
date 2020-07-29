// https://github.com/FortAwesome/vue-fontawesome

import Vue from 'vue';
import { config } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// This is important, we are going to let Nuxt.js worry about the CSS
config.autoAddCss = false;

// Register the component globally
Vue.component('font-awesome-icon', FontAwesomeIcon);
