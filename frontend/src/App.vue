<template>
  <div id="nav">
    <Navbar />
    <InitialReportForm />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue"
// import HelloWorld from "./components/HelloWorld.vue"
export default {
  name: "App",
  components:{
    Navbar,
    // HelloWorld
  }
}
</script>

<style>
html, body{
  height: 100%;
  font-family: 'Courier New', Courier, monospace;
}
</style>
