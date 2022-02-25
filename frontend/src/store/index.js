import Vue from 'vue'
import Vuex, { Store } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import * as report from '@/store/modules/report.js'
import * as user from '@/store/modules/user.js'
import * as notification from './modules/notification.js'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
  modules: {
    user,
    notification,
    report,
  },
  state: {
    loggedIn: false,
  },
  mutations: {
    initializeStore() {
      if (localStorage.getItem('access')) {
        user.state.access = localStorage.getItem('access')
      } else {
        user.state.access = ''
      }
    },
    SET_LOGGED_IN(state, value) {
      state.loggedIn = value
    },
  },
  actions: {},
  getters: {
    isLoggedIn(state) {
      return state.loggedIn
    },
  },
})
