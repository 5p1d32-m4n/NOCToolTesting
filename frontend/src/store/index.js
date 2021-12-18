import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    }
  },
  getters:{
    loggedIn (state) {
      return state.accessToken != null
    }
  },
  actions: {
    userLogin(context, usercredentials) {
      /* eslint-disable */
      return new Promise((resolve, reject) => {
        axios.post('api/api-token/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
            resolve()
          })
      })
    }
  },
  modules: {},
});
