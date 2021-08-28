<template>
  <div>
    <CheckboxSvgMap
      v-model="selectedLocation"
      :map="PuertoRico"
      @mouseover="pointLocation"
      @mouseout="unpointLocation"
      @focus="focusLocation"
      @blur="blurLocation"
    />
    <div class="tooltip-inner">
      Municipio Apuntado:
      <p>{{ pointedLocation }}</p>
    </div>
    <div>{{selectedLocation}}</div>
  </div>
</template>

<script>
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico";
import { getLocationName, getSelectedLocationName } from "../utilities";

export default {
  name: "MunicipalityMap",
  components: {
    CheckboxSvgMap,
  },
  props: {
    selectedLocation: Array,
  },
  data() {
    return {
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
    };
  },
  methods: {
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target);
    },
    unpointLocation() {
      this.pointedLocation = null;
    },
    focusLocation(event) {
      this.focusedLocation = getLocationName(event.target);
    },
    blurLocation() {
      this.focusedLocation = null;
    },
    getSelectedLocationName,
  },
  computed:{},
  watch: {},
};
</script>

<style src="vue-svg-map/dist/index.css">
</style>
