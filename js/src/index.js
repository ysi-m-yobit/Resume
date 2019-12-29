import Vue from 'vue';
import ResumeBody from './vue/ResumeBody';

var app = new Vue({
  el: '#resume_body',
  components: { ResumeBody },
  template: '<ResumeBody/>'
});