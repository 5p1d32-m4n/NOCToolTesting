import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import {
  BootstrapVue,
  IconsPlugin
} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue, IconsPlugin)
// Vue.use(IconsPlugin)
//  Insert here custom url for live hosting url to fetch with axios: https://8000-lime-cattle-yegqyfpg.ws-us18.gitpod.io
axios.defaults.baseURL = 'https://8000-lime-cattle-yegqyfpg.ws-us18.gitpod.io'
new Vue({
  router,
  store,
  axios,
  render: (h) => h(App),
}).$mount("#app");