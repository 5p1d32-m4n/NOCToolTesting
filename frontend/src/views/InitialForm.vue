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
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-AK">Alaska</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-AL">Alabama</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-AR">Arkansas</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-AZ">Arizona</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-CA">California</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-CO">Colorado</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-CT">Connecticut</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-DC">Washington,
                                        DC</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-DE">Delaware</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-FL">Florida</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-GA">Georgia</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-HI">Hawaii</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-IA">Iowa</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-ID">Idaho</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-IL">Illinois</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-IN">Indiana</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-KS">Kansas</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-KY">Kentucky</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-LA">Louisiana</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MA">Massachusetts</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MD">Maryland</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-ME">Maine</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MI">Michigan</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MN">Minnesota</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MO">Missouri</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MS">Mississippi</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-MT">Montana</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-NC">North
                                        Carolina</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-ND">North
                                        Dakota</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-NE">Nebraska</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-NH">New
                                        Hampshire</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-NJ">New
                                        Jersey</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-NM">New
                                        Mexico</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-NV">Nevada</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-NY">New
                                        York</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-OH">Ohio</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-OK">Oklahoma</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-OR">Oregon</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-PA">Pennsylvania</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-RI">Rhode
                                        Island</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-SC">South
                                        Carolina</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-SD">South
                                        Dakota</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-TN">Tennessee</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-TX">Texas</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-UT">Utah</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-VA">Virginia</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-VT">Vermont</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-WA">Washington</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-WI">Wisconsin</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map" value="US-WV">West
                                        Virginia</label></div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="checkbox"><label><input type="checkbox" name="map"
                                            value="US-WY">Wyoming</label></div>
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
    polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);

    // console.log(polygonSeries.datal)

    let polyData = polygonSeries.dataItems;
    console.log(polyData);

    let listFields = polygonSeries.dataFields
    let arrayPR = []
    for (let entry = 0; entry < arrayPR.length; entry ++){
      arrayPR.push(arrayPR[entry].name)
      console.log(arrayPR[entry].value.name)
      console.log("in the loop")
    }
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
