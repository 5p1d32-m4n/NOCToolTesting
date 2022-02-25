<template>
  <div>
    <h1>Oops !</h1>
    <h3>El {{ resource }} que estas buscando no existe.</h3>
    <router-link :to="{ name: 'Dashboard' }">Regresar a Tablero</router-link>
  </div>
</template>

<script>
export default {
  props: {
    resource: {
      type: String,
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped></style>
