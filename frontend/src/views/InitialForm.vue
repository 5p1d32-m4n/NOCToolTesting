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
      <div class="columns" >
        <MunicipalityList />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import MunicipalityList from "../components/MunicipalityList.vue";

export default {
  name: "InitialForm",
  components: {
    MunicipalityList,
  },
  data() {
    return {
      report: {},
      map: {},
      polygonTemplate: {},
      polygonSeries: {},
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
      selected: [],
    };
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
  },
  mounted() {
    document.title = "Formulario de Reporte Inicial";
    
  },
};

// RAW JS for amcharts because nobody works it with vue 3
</script>
<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}


</style>
