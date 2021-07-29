<template>
  <div id="municipality-map">
    <div id="mapchart" class="column"></div>
    <div id="municipality-list" class="column">
      <MunicipalityList
        v-bind:listOfMunicipalities="listOfMunicipalities"
        :changeStateOfMunicipality="changeStateOfMunicipality"
      />
    </div>
  </div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
import MunicipalityList from "../components/MunicipalityList.vue";

export default {
  name: "MunicipalityMap",
  components: {
    MunicipalityList,
  },
  data() {
    return {
      listOfMunicipalities: [
        
      ],
    };
  },
  mounted() {
    // Setting the Doc Tittle
    document.title = "Formulario de Reporte Inicial";

    // geo map portion
    let map = am4core.create("mapchart", am4maps.MapChart);
    map.geodata = am4geodata_puertoRicoHigh;
    map.projection = new am4maps.projections.Miller();
    let polygonSeries = map.series.push(new am4maps.MapPolygonSeries());
    polygonSeries.useGeodata = true;

    // Configure Template
    let polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.fill = am4core.color("#74B266");

    // Create hover state for the map
    let hoverState = polygonTemplate.states.create("hover");
    hoverState.properties.fill = am4core.color("#367B25");

    // Zooom Controls for the map
    map.seriesContainer.wheelable = false;
    map.seriesContainer.draggable = false;
    map.maxZoomLevel = 1;

    // configuration for active state in map.
    let activeState = polygonTemplate.states.create("active");
    activeState.properties.fill = am4core.color("#FF0000");

    // event to switch active state.
    polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);

    // console.log(polygonSeries.datal)

    // let polyData = polygonSeries.data;
    // console.log(polyData);
  },
  methods:{
    changeStateOfMunicipality(municipalities){
      this.listOfMunicipalities = municipalities;
    },
  }
};
</script>

<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}
</style>