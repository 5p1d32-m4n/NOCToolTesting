<template lang="pug">
  .SvgMap svg( xmlns="http://www.w3.org/2000/svg",
  xmlns:xlink="http://www.w3.org/1999/xlink", version="1.1" width="100%"
  height="100%" :viewBox="`0 0 ${viewBoxW} ${viewBoxH}`" ref="svg" )

  g(:transform="`translate(${translateL}, $translateT) scale(${scale})`" ref="g")
  SvgMapPath(
      v-for="path in MUNICIPALITIES",
      :key="path.id",
      v-bind="path",
      
  )
</template>

<script>
import SvgMapPath from "../components/SvgMapPath.vue";
import  MUNICIPALITIES  from "../assets/puertoRicoHigh";
export default {
  name: "SvgMap",
  components: {
    SvgMapPath,
  },
  data() {
    return {
      viewBoxW: 1140,
      viewBoxH: 580,
      translateL: -865,
      translateT: -810,
      scale: 1,
      MUNICIPALITIES
    };
  },
};
</script>
<style scoped>
</style>