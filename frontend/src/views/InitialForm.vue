<template>
  <b-container fluid>
    <form v-on:submit.prevent="createReport">
      <!-- First Row of Form (No more than 2 cols per row.) -->
      <b-row>
        <b-col id="report-specific">
          <!-- NOC Ticket Input -->
          <label for="noc-ticket">Taquilla del NOC:</label>
          <b-form-group>
            <b-form-input
              placeholder="E.g: GD09RG8S0E97F7E"
              id="noc-ticket"
            ></b-form-input>
            <!-- NOC Ticket Input End. -->

            <!-- Third Party Ticket Input -->
            <label for="third-ticket">Taquilla de Tercero:</label>
            <b-form-input
              placeholder="E.g: G8S0E97F7E"
              id="third-ticket"
            ></b-form-input>
            <!-- Third Party Ticket Input End -->

            <!-- Event Date Input -->
            <label for="event-date">Fecha de Averia:</label>
            <b-form-input
              placeholder="E.g: 10/10/2020"
              id="event-date"
              type="date"
            ></b-form-input>
            <!-- Event Date Input End. -->

            <!-- Time of Event Input -->
            <label for="event-time">Tiempo de Averia:</label>
            <b-form-input
              placeholder="E.g: 10:10 AM"
              id="event-time"
              type="time"
            ></b-form-input>
          </b-form-group>
          <!-- Time of Event Input End.  -->
        </b-col>

        <!-- Beginning of Dropdown lists. -->
        <!-- TODO: make these checkbox come from the Django Backend -->
        <!-- TODO: add the followed number input for some cases -->
        <b-col id="report-repetitive">
          <b-form-group>
            <!-- Service Dropdown lists. -->
            <b-form-group>
              <b-dropdown
                block
                variant="danger"
                text="Servicios Impactados"
                class="d-block mt-4"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-row>
                    <b-col>
                      <div v-for="(service, index) in services" :key="index">
                        <input
                          type="checkbox"
                          v-model="service[index]"
                          :value="service[index]"
                          id="service"
                        />
                        <label :for="service">&nbsp; {{service}} </label>
                      </div>
                      <div>
                        <!-- TODO: add number inputs for each checkbox -->
                      <b-form-input
                        type="number"
                        v-for="service in services"
                        :key="service"
                        v-model="selectedServiceAmount"
                      ></b-form-input>
                      </div>
                    </b-col>
                  </b-row>
                </b-dropdown-form>
              </b-dropdown>
              <hr />
            </b-form-group>

            <!-- Cause type dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Causa de Averia"
                class="d-block"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-form-checkbox-group
                    :options="cause"
                    v-model="selectedCauses"
                    stacked
                  ></b-form-checkbox-group>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <hr />

            <!-- Client dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Clientes Impactados"
                class="d-block"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-form-checkbox-group
                    :options="clients"
                    v-model="selectedClients"
                    stacked
                  ></b-form-checkbox-group>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <hr />

            <!-- Outage Type Dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Tipo de Averia"
                class="d-block"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-form-checkbox-group
                    :options="outage_type"
                    v-model="selectedOutageTypes"
                    stacked
                  ></b-form-checkbox-group>
                </b-dropdown-form>
              </b-dropdown>
              <hr />
            </b-form-group>
          </b-form-group>
        </b-col>
      </b-row>

      <!-- Title Row. -->
      <b-row align-h="center">
        <h4>Municipios Impactados:</h4>
      </b-row>

      <!-- Municipality Row -->
      <b-row>
        <!-- Beginning of Municipality Checkbox. -->
        <b-col>
          <div class="overflow-auto" id="municipality-table">
            <b-form-checkbox-group
              v-model="selectedMunicipalities"
              :options="municipalities"
              stacked
            ></b-form-checkbox-group>
          </div>
        </b-col>
        <!-- Beginning of Municipality CheckboxEnd. -->

        <!-- Beggingin of SVG Map. -->
        <b-col>
          <div>
            <CheckboxSvgMap
              v-model="selectedMunicipalities"
              :map="PuertoRico"
              @mouseover="pointLocation"
              @mouseout="unpointLocation"
              @focus="focusLocation"
              @blur="blurLocation"
            />
            <div>
              <h3 class="b-tooltip tool">
                Municipio Apuntado: {{ pointedLocation }}
              </h3>
            </div>
          </div>
        </b-col>
        <!-- Portion SVG Map End. -->
      </b-row>

      <!-- Submit Button row -->
      <b-row>
        <div style="center">
          <b-button type="submit" variant="danger" class="btn-lg btn-block mt-4"
            >Crear Reporte</b-button
          >
        </div>
      </b-row>
    </form>
  </b-container>
</template>

<script>
import axios from "axios";
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico";
import { getLocationName, getSelectedLocationName } from "../utilities";

export default {
  name: "InitialForm",
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      report: {},
      selectedMunicipalities: [],
      selectedServices: [],
      selectedClients: [],
      selectedServiceAmount: [],
      selectedClientAmount: [],
      selectedCauses: [],
      selectedOutageTypes: [],
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
      services: [],
      clients: [],
      outage_type: [],
      cause: [],
      municipalities: [
        "Adjuntas",
        "Aguada",
        "Aguadilla",
        "Aguas Buenas",
        "Aibonito",
        "Añasco",
        "Arecibo",
        "Arroyo",
        "Barceloneta",
        "Barranquitas",
        "Bayamón",
        "Cabo Rojo",
        "Caguas",
        "Camuy",
        "Canóvanas",
        "Carolina",
        "Cataño",
        "Cayey",
        "Ceiba",
        "Ciales",
        "Cidra",
        "Coamo",
        "Comerío",
        "Corozal",
        "Culebra",
        "Dorado",
        "Fajardo",
        "Florida",
        "Guánica",
        "Guayama",
        "Guayanilla",
        "Guaynabo",
        "Gurabo",
        "Hatillo",
        "Hormigueros",
        "Humacao",
        "Isabela",
        "Jayuya",
        "Juana Díaz",
        "Juncos",
        "Lajas",
        "Lares",
        "Las Marías",
        "Las Piedras",
        "Loíza",
        "Luquillo",
        "Manatí",
        "Maricao",
        "Maunabo",
        "Mayagüez",
        "Moca",
        "Morovis",
        "Naguabo",
        "Naranjito",
        "Orocovis",
        "Patillas",
        "Peñuelas",
        "Ponce",
        "Quebradillas",
        "Rincón",
        "Río Grande",
        "Sabana Grande",
        "Salinas",
        "San Germán",
        "San Juan",
        "San Lorenzo",
        "San Sebastián",
        "Santa Isabel",
        "Toa Alta",
        "Toa Baja",
        "Trujillo Alto",
        "Utuado",
        "Vega Alta",
        "Vega Baja",
        "Vieques",
        "Villalba",
        "Yabucoa",
        "Yauco",
      ],
    };
  },
  methods: {
    // TODO: Make sure that this has the parts it needs to process report objects properly
    createReport() {
      this.report;
      axios.post("/api/report-create/").then((response) => {
        this.report = response.data;
      });
    },
    // Function to build the report from the form inputs.
    buildReport() {},

    // Get function for Report Services.
    getServices() {
      let element = [];
      let uniqueServices = [];
      axios
        .get("/api/services-list/")
        .then((response) => {
          // this.services = response.data;
          let temp_services = response.data;
          for (let item = 0; item < temp_services.length; item++) {
            element.push(temp_services[item].services);
          }
          // TODO: clean duplicates from the @element array.
          element.forEach((entry) => {
            if (!uniqueServices.includes(entry)) {
              uniqueServices.push(entry);
            }
          });
          console.log(uniqueServices);
          this.services = uniqueServices;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    // Get function for Report Clients.
    getClients() {
      let element = [];
      let uniqueClients = [];
      axios
        .get("/api/clients-list/")
        .then((response) => {
          // this.clients = response.data;
          let temp_clients = response.data;
          for (let item = 0; item < temp_clients.length; item++) {
            element.push(temp_clients[item].clients);
          }
          // TODO: clean duplicates from the @element array.
          element.forEach((entry) => {
            if (!uniqueClients.includes(entry)) {
              uniqueClients.push(entry);
            }
          });
          console.log(uniqueClients);
          this.clients = uniqueClients;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    // Get function for Report Causes.
    getCause() {
      let element = [];
      let uniqueCause = [];
      axios
        .get("/api/cause-list/")
        .then((response) => {
          // this.cause = response.data;
          let temp_cause = response.data;
          for (let item = 0; item < temp_cause.length; item++) {
            element.push(temp_cause[item].causes);
          }
          // TODO: clean duplicates from the @element array.
          element.forEach((entry) => {
            if (!uniqueCause.includes(entry)) {
              uniqueCause.push(entry);
            }
          });
          console.log(uniqueCause);
          this.cause = uniqueCause;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },

    // Get function for Report Outage Types.
    getOutageType() {
      // TODO: make this function get the outage_type.
      let element = [];
      let uniqueOutageType = [];
      axios
        .get("/api/outage_type-list/")
        .then((response) => {
          // this.outage_type = response.data;
          let temp_outage_type = response.data;
          for (let item = 0; item < temp_outage_type.length; item++) {
            element.push(temp_outage_type[item].outage_type);
          }
          // TODO: clean duplicates from the @element array.
          element.forEach((entry) => {
            if (!uniqueOutageType.includes(entry)) {
              uniqueOutageType.push(entry);
            }
          });
          console.log(uniqueOutageType);
          this.outage_type = uniqueOutageType;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },

    // Svg map Checkbox functions for evets.
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target);
    },
    unpointLocation() {
      this.pointedLocation = null;
    },
    focusLocation(event) {
      this.focusedLocation = getLocationName(event.target);
    },
    blurLocation() {
      this.focusedLocation = null;
    },
    getSelectedLocationName,
  },
  watch: {},
  mounted() {
    document.title = "Formulario de Reporte Inicial";
    this.getServices();
    this.getClients();
    this.getCause();
    this.getOutageType();
  },
  
};

// RAW JS for amcharts because nobody works it with vue 3
</script>
<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
<style src="vue-svg-map/dist/index.css"></style>
