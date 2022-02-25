<template>
  <div></div>
</template>

<script>
import PuertoRico from '../assets/puerto-rico'
import { getLocationName, getSelectedLocationName } from '../utilities'
export default {
  name: 'RepDataPR',
  props: ['municipalityList', 'municipalityOption'],
  components: {},
  data() {
    return {
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
    }
  },
  methods: {
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target)
    },
    unpointLocation() {
      this.pointedLocation = null
    },
    focusLocation(event) {
      this.focusedLocation = getLocationName(event.target)
    },
    blurLocation() {
      this.focusedLocation = null
    },
    getSelectedLocationName,
    updateMunicipalities(event) {
      this.$emit('update-municipalities', event.target.municipalityOption)
    },
  },
}
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
<style src="vue-svg-map/dist/index.css"></style>
