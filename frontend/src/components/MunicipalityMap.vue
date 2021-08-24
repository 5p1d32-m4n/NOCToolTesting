<template>
  <div>
    <CheckboxSvgMap v-model="selected" :map="PuertoRico" />
  </div>
</template>

<script>
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico"
export default {
  name: "MunicipalityMap",
  components: {
    CheckboxSvgMap
  },
  data() {
    return {
        PuertoRico,
        selected: [],
    };
  },
  methods: {

  },
  mounted() {
  },
  watch: {

  },
};
</script>

<style src="vue-svg-map/dist/index.css">
</style>
