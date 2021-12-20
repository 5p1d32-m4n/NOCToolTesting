<template>
  <div id="wrapper">
    <nav class="navbar is-danger">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>Claro NOC</strong></router-link
        >

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <!-- TODO: Replace these links with router-link-->
          <router-link :to="{name:'EmailList'}" class="navbar-item">Notificacion</router-link>
          <a href="" class="navbar-item">Manejo de Usuarios</a>
          <a href="" class="navbar-item">Cuenta</a>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view />
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'App',
  beforeCreate(){
    this.$store.commit("initializeStore")
    const accessToken = this.$store.state.accessToken

    if (accessToken){
      axios.defaults.heasers.common['Authorization'] = "JWT " + accessToken
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted(){
    setInterval(()=> {
      this.getAccess()
    }, 1800000)
  },
  methods:{
    getAccess(){
      const accessData = {
        refreshToken: this.$store.state.refreshToken
      }

      axios
      .post('/api/v1/jwt/refresh/', accessData)
      .then(response => {
        const accessToken = response.data.accessToken

        localStorage.setItem('accessToken', accessToken)
        this.$$store.commit('setAccessToken', accessToken)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>

<style lang="scss">
@import "~bulma";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
