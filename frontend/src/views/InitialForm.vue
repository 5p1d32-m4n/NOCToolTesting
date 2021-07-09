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
              style="width:200px;"
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
              style="width:200px;"
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
              style="width:200px;"
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
              style="width:200px;"
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
              style="width:200px;"
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
          <div id="mapchart"></div>
        </div>
        <!-- List of Municipality Checkboxesw -->
        <div class="column">
          <div id="municipality-talbe">
            <table class="table is-bordered is-fullwidth overflow-scroll">
            <thead>
              <th>Municipios Impactados</th>
            </thead>
            <tbody>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Adjuntas"/>Adjuntas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Aguada"/>Aguada</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Aguadilla"/>Aguadilla</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Aguas Buenas"/>Aguas Buenas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Aibonito"/>Aibonito</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Añasco"/>Añasco</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Arecibo"/>Arecibo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Arroyo"/>Arroyo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Barceloneta"/>Barceloneta</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Barranquitas"/>Barranquitas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Bayamón"/>Bayamón</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Cabo Rojo"/>Cabo Rojo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Caguas"/>Caguas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Camuy"/>Camuy</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Canóvanas"/>Canóvanas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Carolina"/>Carolina</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Cataño"/>Cataño</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Cayey"/>Cayey</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Ceiba"/>Ceiba</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Ciales"/>Ciales</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Cidra"/>Cidra</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Coamo"/>Coamo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Comerío"/>Comerío</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Corozal"/>Corozal</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Culebra"/>Culebra</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Dorado"/>Dorado</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Fajardo"/>Fajardo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Florida"/>Florida</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Guánica"/>Guánica</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Guayama"/>Guayama</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Guayanilla"/>Guayanilla</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Guaynabo"/>Guaynabo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Gurabo"/>Gurabo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Hatillo"/>Hatillo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Hormigueros"/>Hormigueros</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Humacao"/>Humacao</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Isabela"/>Isabela</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Jayuya"/>Jayuya</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="JuanaDíaz"/>JuanaDíaz</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Juncos"/>Juncos</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Lajas"/>Lajas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Lares"/>Lares</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Las Marías"/>Las Marías</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Las Piedras"/>Las Piedras</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Loíza"/>Loíza</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Luquillo"/>Luquillo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Manatí"/>Manatí</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Maricao"/>Maricao</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Maunabo"/>Maunabo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Mayagüez"/>Mayagüez</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Moca"/>Moca</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Morovis"/>Morovis</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Naguabo"/>Naguabo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Naranjito"/>Naranjito</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Orocovis"/>Orocovis</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Patillas"/>Patillas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Peñuelas"/>Peñuelas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Ponce"/>Ponce</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Quebradillas"/>Quebradillas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Rincón"/>Rincón</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="RíoGrande"/>RíoGrande</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Sabana Grande"/>Sabana Grande</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Salinas"/>Salinas</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="San Germán"/>San Germán</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="San Juan"/>San Juan</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="capital"/>capital</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="San Lorenzo"/>San Lorenzo</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="San Sebastián"/>San Sebastián</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Santa Isabel"/>Santa Isabel</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Toa Alta"/>Toa Alta</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Toa Baja"/>Toa Baja</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Trujillo Alto"/>Trujillo Alto</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Utuado"/>Utuado</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Vega Alta"/>Vega Alta</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Vega Baja"/>Vega Baja</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Vieques"/>Vieques</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Villalba"/>Villalba</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Yabucoa"/>Yabucoa</label></div></td></tr>
              <tr><td><div class="checkbox"><label><input type="checkbox" name="map" value="Yauco"/>Yauco</label></div></td></tr>
            </tbody>
          </table>
          </div>
          
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

// default exports
export default {
  name: "InitialForm",
  components: {},
  data() {
    return {
      report: {},
    };
  },
  methods: {
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
    map.maxZoomLevel = 1;
  },
};

// dropdown configurations
</script>
<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}

#municipality-talbe{
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
