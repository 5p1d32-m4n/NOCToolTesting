<template>
  <div>
    <h1>Uh-Oh!</h1>
    <h3>Al parecer hay problemas de coneción, regrese para intentar denuevo</h3>
    <router-link :to="{ name: 'Dashborad' }"
      >Regresar al tablero principal</router-link
    >
  </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped></style>
