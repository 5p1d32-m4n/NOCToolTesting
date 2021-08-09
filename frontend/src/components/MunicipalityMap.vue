<template>
  <div id="municipality-map" class="columns">
    <div ref="mapchart" class="column"></div>
    <div id="municipality-talbe" class="column">
      <table class="table is-bordered is-fullwidth overflow-scroll">
        <thead>
          Municipios Impactados
        </thead>
        <tbody>
          <tr
            v-for="municipality in municipalities.slice().reverse()"
            :key="municipality"
          >
            <td>
              <MunicipalityList
                :municipality="municipality"
                ref="{{municipality.id}}"
                v-model="selectedMunicipalities"
              />
            </td>
          </tr>
        </tbody>
      </table>
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
      municipalities: [
        { id: "PR-YU", name: "Yauco" },
        { id: "PR-YB", name: "Yabucoa" },
        { id: "PR-VL", name: "Villalba" },
        { id: "PR-VQ", name: "Vieques" },
        { id: "PR-VB", name: "Vega Baja" },
        { id: "PR-VA", name: "Vega Alta" },
        { id: "PR-UT", name: "Utuado" },
        { id: "PR-TJ", name: "Trujillo Alto" },
        { id: "PR-TB", name: "Toa Baja" },
        { id: "PR-TA", name: "Toa Alta" },
        { id: "PR-SI", name: "Santa Isabel" },
        { id: "PR-SS", name: "San Sebastián" },
        { id: "PR-SL", name: "San Lorenzo" },
        { id: "PR-SJ", name: "San Juan" },
        { id: "PR-SG", name: "San Germán" },
        { id: "PR-SA", name: "Salinas" },
        { id: "PR-SB", name: "Sabana Grande" },
        { id: "PR-RG", name: "Río Grande" },
        { id: "PR-RC", name: "Rincón" },
        { id: "PR-QB", name: "Quebradillas" },
        { id: "PR-PO", name: "Ponce" },
        { id: "PR-PN", name: "Peñuelas" },
        { id: "PR-PT", name: "Patillas" },
        { id: "PR-OR", name: "Orocovis" },
        { id: "PR-NR", name: "Naranjito" },
        { id: "PR-NG", name: "Naguabo" },
        { id: "PR-MV", name: "Morovis" },
        { id: "PR-MC", name: "Moca" },
        { id: "PR-MG", name: "Mayagüez" },
        { id: "PR-MB", name: "Maunabo" },
        { id: "PR-MR", name: "Maricao" },
        { id: "PR-MT", name: "Manatí" },
        { id: "PR-LQ", name: "Luquillo" },
        { id: "PR-LZ", name: "Loíza" },
        { id: "PR-LP", name: "Las Piedras" },
        { id: "PR-LM", name: "Las Marías" },
        { id: "PR-LR", name: "Lares" },
        { id: "PR-LJ", name: "Lajas" },
        { id: "PR-JC", name: "Juncos" },
        { id: "PR-JD", name: "Juana Díaz" },
        { id: "PR-JY", name: "Jayuya" },
        { id: "PR-IS", name: "Isabela" },
        { id: "PR-HU", name: "Humacao" },
        { id: "PR-HO", name: "Hormigueros" },
        { id: "PR-HA", name: "Hatillo" },
        { id: "PR-GR", name: "Gurabo" },
        { id: "PR-GB", name: "Guaynabo" },
        { id: "PR-GL", name: "Guayanilla" },
        { id: "PR-GM", name: "Guayama" },
        { id: "PR-GC", name: "Guánica" },
        { id: "PR-FL", name: "Florida" },
        { id: "PR-FJ", name: "Fajardo" },
        { id: "PR-DO", name: "Dorado" },
        { id: "PR-CU", name: "Culebra" },
        { id: "PR-CZ", name: "Corozal" },
        { id: "PR-CM", name: "Comerío" },
        { id: "PR-CO", name: "Coamo" },
        { id: "PR-CD", name: "Cidra" },
        { id: "PR-CL", name: "Ciales" },
        { id: "PR-CB", name: "Ceiba" },
        { id: "PR-CY", name: "Cayey" },
        { id: "PR-CT", name: "Cataño" },
        { id: "PR-CN", name: "Carolina" },
        { id: "PR-CV", name: "Canóvanas" },
        { id: "PR-CA", name: "Camuy" },
        { id: "PR-CG", name: "Caguas" },
        { id: "PR-CR", name: "Cabo Rojo" },
        { id: "PR-BY", name: "Bayamón" },
        { id: "PR-BQ", name: "Barranquitas" },
        { id: "PR-BC", name: "Barceloneta" },
        { id: "PR-AR", name: "Arroyo" },
        { id: "PR-AC", name: "Arecibo" },
        { id: "PR-AN", name: "Añasco" },
        { id: "PR-AI", name: "Aibonito" },
        { id: "PR-AB", name: "Aguas Buenas" },
        { id: "PR-AL", name: "Aguadilla" },
        { id: "PR-AD", name: "Aguada" },
        { id: "PR-AJ", name: "Adjuntas" },
      ],
      selectedMunicipalites: [],
      map: Object,
    };
  },
  methods: {
    renderMap() {
      let map = am4core.create(this.$refs.mapchart, am4maps.MapChart);
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
      let tempArray = [];

      // This is where the array of municipalities is called in geodata.
      let polygonData = polygonSeries.data;
      console.log(polygonData);
      // event to switch active state.
      // polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);
      polygonTemplate.events.on(
        "hit",
        (ev) => {
          let clickedMapID = ev.target.dataItem.dataContext;
          // Create an event to toggle "active" state
          ev.target.isActive = !ev.target.isActive;
          console.log(clickedMapID.id + " " + ev.target.isActive);
          if (ev.target.isActive === true) {
            console.log(
              "The checkbox for " + clickedMapID.name + " was clicked."
            );
            // fucnction call with clickedMapID.id as an argument
            tempArray.push(clickedMapID.id);
            console.log("So far you've selected: " + tempArray);
            console.log(clickedMapID.id);
          } else {
            console.log("deactivated " + clickedMapID.name);
            for (let index = 0; index < tempArray.length; index++) {
              if (tempArray[index] === clickedMapID.id) {
                tempArray.splice(index, 1);
              }
            }
            console.log("So far you've selected: " + tempArray);
          }
        },
        this
      );
      // Endo of struggle-o
      this.map = map;
      this.selectedMunicipalites = tempArray;
    },
  },
  mounted() {
    this.renderMap();
  },
  watch: {

  },
};
</script>

<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}

#municipality-talbe {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
