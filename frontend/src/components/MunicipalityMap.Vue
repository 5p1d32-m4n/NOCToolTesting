<template>
  <div id="municipality-map">
      <div id="mapchart"></div>
      <div>
        <MunicipalityList />
      </div>
  </div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
import MunicipalityList from "@components/MunicipalityList.vue";

export default {
    name: "MunicipalityMap",
    components:{
        MunicipalityList
    },
};
</script>

<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}

</style>