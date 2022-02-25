<template>
  <b-container fluid="1">
    <b-navbar toggleable="lg" type="dark" variant="danger">
      <b-navbar-brand :to="{ name: 'Dashboard' }">Claro NOC</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <!-- Nav collapse toggle -->
      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" type="light">
          <b-nav-item right :to="{}">Notificacion</b-nav-item
          ><b-nav-item right :to="{}">Manejar Objetos</b-nav-item
          ><b-nav-item right :to="{}">Cuenta</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <section class="section"></section>
  </b-container>
</template>

<script>
export default {
  name: 'RepNavBar',
}
</script>

<style scoped></style>
