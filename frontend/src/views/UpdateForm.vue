<template>
  <b-container fluid>
    <form action="">
      <b-row>
        <!-- These are the text input fields (date and time included) -->
        <b-col id="report-specific">
          <b-form-group>
            <!-- NOC Ticket Input -->
            <label for="noc-ticket">Taquilla del NOC:</label>
            <b-form-input
              disabled
              id="noc-ticket"
              :maxlength="15"
              :value="report.noc_ticket"
            ></b-form-input>
            <!-- NOC Ticket Input End. -->

            <!-- Third Party Ticket Input -->
            <label for="third-ticket">Taquilla de Tercero:</label>
            <div v-if="thirdPartyTicketCheck(report.third_party_ticket)">
              <b-form-input
                id="third-ticket"
                :maxlength="15"
                v-model="report.third_party_ticket"
                disabled
              ></b-form-input>
            </div>
            <div v-else>
              <b-form-input
                id="third-ticket"
                :maxlength="15"
                v-model="report.third_party_ticket"
              ></b-form-input>
            </div>
            <!-- Third Party Ticket Input End -->

            <!-- Event Date Input -->
            <label for="event-date">Fecha de Averia:</label>
            <b-form-input
              placeholder="E.g: 10/10/2020"
              id="event-date"
              type="date"
              v-model="report.date_of_outage"
              disabled
            ></b-form-input>
            <!-- Event Date Input End. -->

            <!-- Time of Event Input -->
            <label for="event-time">Tiempo de Averia:</label>
            <b-form-input
              placeholder="E.g: 10:10 AM"
              id="event-time"
              type="time"
              v-model="report.time_of_outage"
              disabled
            ></b-form-input>
          </b-form-group>
          <!-- Time of Event Input End.  -->
        </b-col>

        <!-- Beginning of Dropdown lists. -->
        <b-col id="report-repetitive">
          <b-form-group>
            <!-- SERVICE DROPDOWN -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                text="Servicios Impactados"
                class="m-2 d-grid mt-4"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-row align-h="center">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">Servicios</th>
                          <th scope="col">Cantidad Impactda</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(service, index) in services" :key="index">
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="oldServices"
                                :value="service"
                                >&nbsp;{{ service }}</b-form-checkbox
                              >
                            </div>
                          </td>
                          <td>
                            <div>
                              <input
                                type="number"
                                name="amountSlots"
                                v-model="oldServAmount[index]"
                                required
                                min="0"
                                :id="service"
                              />
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </b-row>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <!-- SERVICE DROPDOWN -->
            <!-- Cause type dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Causa de Averia"
                class="m-2 d-grid mt-3"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-row align-h="center">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">Causas de Averia:</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(cause, index) in cause" :key="index">
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="report.causes"
                                :value="cause"
                                :id="cause"
                                >&nbsp;{{ cause }}</b-form-checkbox
                              >
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </b-row>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <!-- Client dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Clientes Impactados"
                class="m-2 d-grid mt-3"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-row align-h="center">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">Tipo de Cliente:</th>
                          <th scope="col">Cantidad Impactada:</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(client, index) in clients" :key="index">
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="report.clients"
                                :value="client"
                                >&nbsp;{{ client }}</b-form-checkbox
                              >
                            </div>
                          </td>
                          <td>
                            <div>
                              <input
                                type="number"
                                name="clientAmount"
                                value="0"
                                min="0"
                                :id="client"
                              />
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </b-row>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <!-- Outage Type Dropdown -->
            <b-form-group>
              <b-dropdown
                variant="danger"
                block
                text="Tipo de Averia"
                class="m-2 d-grid mt-3"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-form-checkbox-group
                    :options="outage_type"
                    v-model="report.outage_type"
                    stacked
                  ></b-form-checkbox-group>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
          </b-form-group>
        </b-col>
      </b-row>
      <hr />
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
              v-model="report.municipalities"
              :options="municipalities"
              stacked
              disabled
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
          <div>
            <input
              type="text"
              class="form-control"
              id="notes"
              v-model="report.notes"
              :maxlength="500"
            />
          </div>
        </b-col>
        <!-- Portion SVG Map End. -->
      </b-row>
    </form>
  </b-container>
</template>

<script>
// TODO: Duplicate the functionality from Impacted Services with Impacted Clients.
import axios from "axios";
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico";
import { getLocationName, getSelectedLocationName } from "../utilities";

export default {
  name: "UpdateForm",
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      report: {
        report_type: "",
        noc_ticket: "",
        third_party_ticket: "",
        date_of_outage: "",
        time_of_outage: "",
        notes: "",
        municipalities: [],
        outage_type: null,
        causes: null,
        services: null,
        clients: null,
      },
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
      PuertoRico,
    };
  },
  computed: {
    //   TODO: seperate into setter and getter functions or run meta setter.
    oldServices: {
      get: function () {
        let oldServ = [];
        oldServ = this.report.services;
        let arrayServices = [];
        arrayServices = Object.keys(oldServ);
        return arrayServices;
      },
      set: function () {},
    },
    oldServAmount: {
      get: function () {
        let allServices = [];
        let oldServices = [];
        let allAmounts = [];
        let oldServiceAmount = [];
        allServices = this.services;
        oldServices = Object.keys(this.report.services);
        oldServiceAmount = Object.values(this.report.services);

        //* Here I initialize an array that is for the amounts started at zero and change them later in the second for loop.
        for (let entry = 0; entry < allServices.length; entry++) {
          allAmounts.push(0);
        }
        //* this is where we need to run the for loop with existance check
        for (let index = 0; index < allServices.length; index++) {
          let currentService = allServices[index];
          console.log("the current LIST service is :" + currentService);

          for (let subIndex = 0; subIndex < oldServices.length; subIndex++) {
            let reportService = oldServices[subIndex];
            console.log("the current OLD report service is : " + reportService);
            //* Here we compare if the service from our api list matches the selected service from our report:

            if (currentService == reportService) {
              console.log(currentService + " :services Match:" + reportService);
              allAmounts[index] = oldServiceAmount[subIndex];
            }
          }
        }
        console.log("amounts zero: " + allAmounts);

        return allAmounts;
      },
      set: function () {},
    },
    impactedClientData:{
      get: function () {
        return ""
      },
      set: function () {
        return ""
      }
    },
    selectedMunicipalities: function () {
      let selection = this.report.municipalities;
      return selection;
    },
  },
  watch: {
    selectedMunicipalities: function () {
      this.selectedMunicipalities = [];
      this.selectedMunicipalities = this.report.municipalities;
    },
  },
  methods: {
    getReportData() {
      const noc_ticket_url = this.$route.params.noc_ticket;

      axios
        .get(`/api/report-detail/${noc_ticket_url}/`)
        .then((response) => {
          this.report.report_type = response.data.report_type;
          this.report.noc_ticket = response.data.noc_ticket;
          this.report.third_party_ticket = response.data.third_party_ticket;
          this.report.date_of_outage = response.data.date_of_outage;
          this.report.time_of_outage = response.data.time_of_outage;
          this.report.notes = response.data.notes;
          let stringMunicipalities = response.data.municipalities;
          this.report.municipalities = stringMunicipalities.split(",");
          let stringOutageType = response.data.outage_type;
          // this.report.outage_type = response.data.outage_type;
          this.report.outage_type = stringOutageType.split(",");
          this.report.causes = response.data.causes;
          this.report.services = JSON.parse(response.data.services);
          this.report.clients = JSON.stringify(response.data.clients);
          // console.log(this.report);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    thirdPartyTicketCheck(object) {
      if (object == null || object == "") {
        return false;
      } else {
        return true;
      }
    },
    //* Get function for Report Services.
    // TODO reformat axios section
    getServices() {
      let element = [];
      let uniqueServices = [];
      axios
        .get("/api/services-list/")
        .then((response) => {
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
          this.services = uniqueServices;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    //* Get function for Report Clients.
    // TODO reformat axios section
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
    //* Get function for Report Causes.
    // TODO reformat axios section
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
    //* Get function for Report Outage Types.
    // TODO reformat axios section
    getOutageType() {
      // TODO: make this function get the outage_type.
      let element = [];
      let uniqueOutageType = [];
      axios
        .get("/api/outage_type-list/")
        .then((response) => {
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
    // setServiceAmounts() {
    //   let oldServ = this.report.services;
    //   let arrayServices = []
    //   arrayServices = Object.keys(oldServ);
    //   let arrayAmounts = []
    //   arrayAmounts = Object.values(oldServ);
    //   console.log("array services: " + arrayServices);
    //   console.log("array amounts: " + arrayAmounts);
    // },
    //* Svg map Checkbox functions for evets.
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
  beforeMounted() {
    document.title = "Forumulario de Actualizacion";
  },
  mounted() {
    this.getReportData();
    this.getServices();
    // this.setServiceAmounts();
    this.getClients();
    this.getCause();
    this.getOutageType();
  },
};
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
<style src="vue-svg-map/dist/index.css"></style>