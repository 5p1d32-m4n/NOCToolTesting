<template>
  <div class="w-100">
    <RepNavBar />
    <NotificationContainer />
    <router-view :key="$route.fullPath" />
  </div>
</template>
<script>
import RepNavBar from '@/components/RepNavBar.vue'
import NotificationContainer from './components/NotificationContainer.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    NotificationContainer,
    RepNavBar,
  },
  methods: {},
  data() {
    return {}
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = `JWT ${access}`
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.-text-error {
  color: tomato;
}
.-text-success {
  color: green;
}
</style>
