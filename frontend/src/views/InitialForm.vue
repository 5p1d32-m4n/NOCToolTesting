<template>
  <div id="initial-form">
    <form>
      <div class="columns">
        <div class="column" id="report-specific">
          <label for="noc_ticket">Taquilla del NOC:</label>
          <input type="text" name="noc_ticket" id="noc_ticket" class="input" />
          <label for="third_party_ticket">Taquilla de Tercero:</label>
          <input
            type="text"
            name="has-text-white-bis"
            id="has-text-white-bis"
            class="input"
          />
          <label for="dateOfEvent">Fecha de Averia:</label>
          <input
            type="date"
            name="dateOfEvent"
            id="dateOfEvent"
            class="input"
          />
          <label for="timeOfEvent">Tiempo de Averia</label>
          <input
            type="time"
            name="timeOfEvent"
            id="timeOfEvent"
            class="input"
          />
        </div>
        <!-- Dropdowns -->
        <!-- TODO: -Add the checkbox and integer inputs -->
        <div
          class="column field is-grouped btn-group-vertical"
          id="service-specific"
        >
          <!-- Service Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Outage type dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Tipo de Averia
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Client dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Clientes Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Service Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Cause Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- AM4 Map chart -->
      <div class="columns">
        <div class="column">
          <div id="mapchart" @click="appendToMunicipalitiesList"></div>
          <!-- <MunicipalityMap /> -->
          <!-- using the mapchart as a component -->
        </div>

        <!-- List of Municipality Checkboxesw -->
        <div class="column">
          <!-- <MunicipalityList /> -->
          <!-- <div id="municipality-talbe">
            <table class="table is-bordered is-fullwidth overflow-scroll">
              <thead>
                <th>Municipios Impactados</th>
              </thead>

              <tbody>
                <tr
                  v-for="country in listOfMunicipalities"
                  v-bind:key="country"
                >
                  <div class="checkbox">
                    <label
                      ><input type="checkbox" name="map" value="country" />{{
                        country
                      }}</label
                    >
                  </div>
                </tr>
              </tbody>
            </table>
          </div> -->

          <!-- testing portion. -->
          <!-- <div
            v-bind:listOfMunicipalities="listOfMunicipalities"
          >
            <div
              class="btn-group" 
              role="group" 
              aria-label="Selector de Municipios"
              id="municipality-checkbox"
              name= "flavour"
              @change="changeStateOfMunicipality($event)"
              >

                <ul>
                  <li v-for="(country) in listOfMunicipalities" v-bind:key="country">
                    <input type="checkbox" name="{{country}}" id="{{country}}">
                    <label for="{{country}}">{{country}}</label>
                  </li>
                </ul>
            </div>
          </div> -->
          <!-- End of testing portion. -->

<!-- straight amcharts rip -->

<div class="col-sm-8">
    <h2 class="family-light size-biggerer underline section-map-list-title">Select states you visited</h2>
    <div class="section-map-list">
        <div class="tab-content overflow-auto" style="height: 350px;">
            <div id="states" class="tab-pane active">
                <table class="table table-hover table-striped">
                    <tbody>
                        <tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-YU" />Yauco</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-YB" />Yabucoa</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-VL" />Villalba</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-VQ" />Vieques</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-VB" />Vega Baja</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-VA" />Vega Alta</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-UT" />Utuado</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-TJ" />Trujillo Alto</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-TB" />Toa Baja</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-TA" />Toa Alta</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SI" />Santa Isabel</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SS" />San Sebastián</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SL" />San Lorenzo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SJ" />San Juan</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SG" />San Germán</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SA" />Salinas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-SB" />Sabana Grande</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-RG" />Río Grande</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-RC" />Rincón</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-QB" />Quebradillas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-PO" />Ponce</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-PN" />Peñuelas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-PT" />Patillas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-OR" />Orocovis</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-NR" />Naranjito</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-NG" />Naguabo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MV" />Morovis</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MC" />Moca</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MG" />Mayagüez</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MB" />Maunabo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MR" />Maricao</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-MT" />Manatí</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LQ" />Luquillo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LZ" />Loíza</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LP" />Las Piedras</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LM" />Las Marías</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LR" />Lares</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-LJ" />Lajas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-JC" />Juncos</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-JD" />Juana Díaz</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-JY" />Jayuya</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-IS" />Isabela</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-HU" />Humacao</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-HO" />Hormigueros</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-HA" />Hatillo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-GR" />Gurabo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-GB" />Guaynabo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-GL" />Guayanilla</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-GM" />Guayama</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-GC" />Guánica</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-FL" />Florida</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-FJ" />Fajardo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-DO" />Dorado</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CU" />Culebra</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CZ" />Corozal</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CM" />Comerío</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CO" />Coamo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CD" />Cidra</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CL" />Ciales</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CB" />Ceiba</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CY" />Cayey</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CT" />Cataño</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CN" />Carolina</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CV" />Canóvanas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CA" />Camuy</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CG" />Caguas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-CR" />Cabo Rojo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-BY" />Bayamón</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-BQ" />Barranquitas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-BC" />Barceloneta</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AR" />Arroyo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AC" />Arecibo</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AN" />Añasco</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AI" />Aibonito</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AB" />Aguas Buenas</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AL" />Aguadilla</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AD" />Aguada</label>
    </div>
  </td>
</tr>

<tr>
  <td>
    <div class="checkbox">
      <label><input type="checkbox" name="map" value="PR-AJ" />Adjuntas</label>
    </div>
  </td>
</tr>

                        
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- end of amcharts rinp -->

        </div>
      </div>
    </form>
  </div>
</template>

<script>
// axios imports
import axios from "axios";
// amcharts imports

import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
// import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
// am4core.useTheme(am4themes_animated)
// Free SVG stand alone component
// import MunicipalityMap from "../components/MunicipalityMap";
// import MunicipalityList from "../components/MunicipalityList.vue";
// default exports
export default {
  name: "InitialForm",
  components: {
    // MunicipalityMap,
    // MunicipalityList,
  },
  data() {
    return {
      report: {},
      // listOfMunicipalities: [],
      // selected: this.listOfMunicipalities,
    };
  },
  watch: {

  },
  methods: {
    // TODO: Make sure that this has the parts it needs to process report objects properly
    postReport(report) {
      axios
        .post(`/api/report-create/`, report)
        .then((report) => {
          this.response = report;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // changeStateOfMunicipality(municipalities) {
    //   this.listOfMunicipalities = municipalities;
    // },

// appendToMunicipalitiesList: function (event) {
    //   event.target.isActive = !event.target.isActive;
    //   let municipality = event.target.dataItem.dataContext.name;
    //   if (event.target.isActive === true) {
    //     this.listOfMunicipalities.push(municipality);
    //     console.log(this.listOfMunicipalities);
    //   } else {
    //     this.listOfMunicipalities.pop(municipality);
    //     console.log(this.listOfMunicipalities);
    //   }
    // },
  },

  mounted() {
    // Setting the Doc Tittle
    document.title = "Formulario de Reporte Inicial";
    // let list={
    //   municipalities: am4geodata_puertoRicoHigh.svg.g.path
    // };
    // let names = {};
        
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
    // polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);
    polygonTemplate.events.on("hit", function (ev) {
      let clickedMapID = ev.target.dataItem.dataContext;
      // Create an event to toggle "active" state
      ev.target.isActive = !ev.target.isActive;
      console.log(clickedMapID.id + " " + ev.target.isActive)
      let checkboxClone = document.getElementById(clickedMapID.id); 
      if (ev.target.isActive === true){
        console.log("The checkbox for " + clickedMapID.name + ", " + checkboxClone)
      }else{
        console.log("deactivated")
      }
    })

    // console.log(polygonSeries.datal)

    let polyData = polygonSeries.dataItems;
    console.log(polyData);

    let listFields = polygonSeries.data
    let arrayPR = []
    console.log(arrayPR)
    // console.log(listOfPR)
    console.log(listFields)
    
    
  },
};

// dropdown configurations
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
