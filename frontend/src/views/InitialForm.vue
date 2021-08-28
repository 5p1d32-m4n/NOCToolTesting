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
      <div class="columns">
        <div class="column">
<<<<<<< HEAD
          <MunicipalityList
          :selectedLocation="computedLocations"
          />
          <p>{{selectedLocation}}</p>
=======
          <MunicipalityList v-model="selectedLocations" :selectedLocations="selectedLocations" />
          <p>{{ selectedLocations }}</p>
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
        </div>
        <div class="column" :selectedLocation="selectedLocation">
          <MunicipalityMap />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import MunicipalityList from "../components/MunicipalityList.vue";
import MunicipalityMap from "../components/MunicipalityMap.vue";
export default {
  name: "InitialForm",
  components: {
    MunicipalityList,
    MunicipalityMap,
  },
  data() {
    return {
      report: {},
      // TODO: make selectedLocations a prompt for MunicipalityList and MunicipalityMap Componentes.
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
  computed:{
    computedLocations: function(){
      let computedLocations = []
      return computedLocations
    }
  },
  mounted() {
    document.title = "Formulario de Reporte Inicial";
  },
};

// RAW JS for amcharts because nobody works it with vue 3
</script>
<style scoped>
</style>
