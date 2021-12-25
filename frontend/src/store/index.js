import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
Vue.use(Vuex);

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    access: localStorage.getItem("access"),
    endpoints: {
      accessToken: "http://127.0.0.1:8000/api/api-token/",
      refreshToken: "http://127.0.0.1:8000/api/api-token-refresh/",
      baseUrl: "http://127.0.0.1:8000",
    },
  },
  mutations: {
    SET_AUTH_USER(state, { authUser, isAuthenticated }) {
      Vue.set(state, "authUser", authUser);
      Vue.set(state, "isAuthenticated", isAuthenticated);
    },
    updateToken(state, newToken) {
      // TODO: some day take this out of local storage. I know, but not now.
      localStorage.setItem("access", newToken);
      state.access = newToken;
    },
    removeToken(state) {
      // TODO: same, take out local storage.
      localStorage.removeItem("access");
      state.access = "";
    },
  },
  actions: {},
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
  },
});
