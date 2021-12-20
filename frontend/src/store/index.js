import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    isAuthenticated: false,
    username: ''
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("accessToken") && localStorage.getItem("refreshToken")) {
        state.accessToken = localStorage.getItem("accessToken")
        state.refreshToken = localStorage.getItem("refreshToken")
        state.isAuthenticated = true
      } else {
        state.accessToken = ''
        state.refreshToken = ''
        state.isAuthenticated = false
      }
    },
    setAccessToken(state, accessToken) {
      state.accessToken = accessToken
      state.isAuthenticated = true 
    },
    setRefreshToken(state, refreshToken){
      state.refreshToken = refreshToken
    },
    removeTokens(state){
      state.accessToken = ''
      state.refreshToken = ''
      state.isAuthenticated = false
    }
  },

  actions: {

  },
});
