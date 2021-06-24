<template>
  <div id="nav">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
// import HelloWorld from "./components/HelloWorld.vue"
export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Courier New", Courier, monospace;
}
</style>
