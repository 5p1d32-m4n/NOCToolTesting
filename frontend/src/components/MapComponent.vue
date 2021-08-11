<template>
  <div class="columns">
    <div class="column">
      <div class="container">
        <SvgMap
        :map="map"
        view-box = "0 0 25220 25220"
        />
      </div>
    </div>
    <div class="column" id="municipality-table">
      <MunicipalityList
        :municipalities="map"
      />
    </div>
  </div>
</template>

<script>
import MunicipalityList from "../components/MunicipalityList.vue";
import SvgMap from 'vue-simple-svg-map'
import map from '../assets/puertoRicoHigh'

export default {
  name: "MapComponent",
  components: {
    MunicipalityList,
    SvgMap
  },
  data() {
    return {
      map,
      selectedMunicipalities: [],
    };
  },
  methods: {
    getMunicipalityID(e) {
      this.title = e.target.id;
      console.log(this.title);
    },
    toggleMunicipality(e) {
      let municipality = e.target.id;
      // let element = document.getElementById(e.target.id)
      console.log(municipality);
    },
  },
  mounted() {},
};
</script>

<style scoped>
path {
  fill: #558b2f;
  cursor: pointer;
  -webkit-transition: all 150ms;
  -moz-transition: all 150ms;
  -o-transition: all 150ms;
  transition: all 150ms;
}
path:hover {
  opacity: 0.85;
  fill: gold;
}
.land {
  fill: #0c7402;
  fill-opacity: 1;
  stroke: white;
  stroke-opacity: 1;
  stroke-width: 0.5;
}

.selected {
  opacity: 0.85;
  fill: red;
}
#municipality-talbe {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
