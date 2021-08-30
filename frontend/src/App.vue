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
          <a href="" class="navbar-item">Notificacion</a>
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
export default {
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
