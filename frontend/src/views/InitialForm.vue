<template>
  <b-container fluid>
    <form v-on:submit.prevent="testFucntion">
      <!-- First Row of Form (No more than 2 cols per row.) -->
      <b-row>
        <!-- These are the text input fields (date and time included) -->
        <b-col id="report-specific">
          <!-- NOC Ticket Input -->
          <b-form-group>
            <label for="noc-ticket">Taquilla del NOC:</label>
            <b-form-input
              placeholder="E.g: GD09RG8S0E97F7E"
              id="noc-ticket"
              :maxlength="15"
              v-model="reportNOCTicket"
            ></b-form-input>
            <!-- NOC Ticket Input End. -->

            <!-- Third Party Ticket Input -->
            <label for="third-ticket">Taquilla de Tercero:</label>
            <b-form-input
              placeholder="E.g: G8S0E97F7E"
              id="third-ticket"
              :maxlength="15"
              v-model="reportThirdPartyTicket"
            ></b-form-input>
            <!-- Third Party Ticket Input End -->

            <!-- Event Date Input -->
            <label for="event-date">Fecha de Averia:</label>
            <b-form-input
              placeholder="E.g: 10/10/2020"
              id="event-date"
              type="date"
              v-model="reportOutageDate"
            ></b-form-input>
            <!-- Event Date Input End. -->

            <!-- Time of Event Input -->
            <label for="event-time">Tiempo de Averia:</label>
            <b-form-input
              placeholder="E.g: 10:10 AM"
              id="event-time"
              type="time"
              v-model="reportOutageTime"
            ></b-form-input>
          </b-form-group>
          <!-- Time of Event Input End.  -->
        </b-col>

        <!-- Beginning of Dropdown lists. -->
        <b-col id="report-repetitive">
          <b-form-group>
            <!-- Service Dropdown lists. -->
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
                                v-model="selectedServices"
                                :value="service"
                                >&nbsp;{{ service }}</b-form-checkbox
                              >
                            </div>
                          </td>
                          <td>
                            <div>
                              <!-- <b-form-input type="number" value="0" v-model="selectedServiceAmount[index]"></b-form-input> -->
                              <input
                                type="number"
                                name="amountSlots"
                                value="0"
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
                                v-model="selectedCauses"
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
                                v-model="selectedClients"
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
                    v-model="selectedOutageTypes"
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
      report: {
        report_type: null,
        noc_ticket: null,
        third_party_ticket: null,
        date_of_outage: null,
        time_of_outage: null,
        notes: null,
        municipalities: null,
        outage_type: null,
        causes: null,
        services: null,
        clients: null,
      },
      reportState: "Inicial",
      reportNOCTicket: "",
      reportThirdPartyTicket: "",
      reportOutageDate: null,
      reportOutageTime: null,
      reportNotes: null,
      selectedMunicipalities: [],
      selectedServices: [],
      selectedClients: [],
      selectedServiceAmount: {
        type: Array,
        default: "0",
      },
      selectedClientAmount: {
        type: Array,
        default: "0",
      },
      selectedCauses: [],
      selectedOutageTypes: [],
      stringifiedServices: JSON,
      stringifiedClients: JSON,
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
    // ? Test dump function
    testFucntion() {
      let tempReport = {}
      tempReport.report_type = this.reportState
      tempReport.noc_ticket = this.reportNOCTicket
      tempReport.third_party_ticket = this.reportThirdPartyTicket  
      tempReport.date_of_outage = this.reportOutageDate
      tempReport.time_of_outage = this.reportOutageTime
      tempReport.notes = this.reportNotes
      let tempMuni = this.selectedMunicipalities.toString()
      tempReport.municipalities = tempMuni
      let tempOutType = this.selectedOutageTypes.toString()
      tempReport.outage_type = tempOutType
      let tempReportCauses = this.selectedCauses.toString()
      tempReport.causes = tempReportCauses
      this.buildServiceObject();
      this.buildClientObject();
      tempReport.services = this.stringifiedServices
      tempReport.clients = this.stringifiedClients
      // tempReport = JSON.stringify(this.report)
      console.log(tempReport)
      axios({
        method: 'post',
        url: '/api/report-create/',
        data:{
          report: tempReport
        },
        auth:{
          username: 'bb81204',
          password: 'grimm-94'
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    //* Function that builds the Service portion of the Outage report in JS forma
    buildServiceObject() {
      let tempSelectedServices = this.selectedServices;
      let tempAmount = [];

      for (let entry = 0; entry < tempSelectedServices.length; entry++) {
        tempAmount.push(
          document.getElementById(tempSelectedServices[entry]).value
        );
      }
      // * TESTING: stringify this so it will match the Djando service field.
      let testCase = this.selectedServices.reduce(
        (acc, value, index) => ((acc[value] = tempAmount[index]), acc),
        {}
      );
      let servicesObject = JSON.stringify(testCase);
      this.stringifiedServices = servicesObject;
    },
    buildClientObject() {
      // TODO: transfer this function to do the same operation as @buildServiceObject()
      let tempSelectedClients = this.selectedClients;
      let tempAmount = [];

      for (let entry = 0; entry < tempSelectedClients.length; entry++) {
        tempAmount.push(
          document.getElementById(tempSelectedClients[entry]).value
        );
      }

      //*  TESTING: stringify this so it will match the Djando service field.
      let testCase = this.selectedClients.reduce(
        (acc, value, index) => ((acc[value] = tempAmount[index]), acc),
        {}
      );
      let clientsObject = JSON.stringify(testCase);
      console.log(clientsObject);
      this.stringifiedClients = clientsObject;
    },
    setServiceZeroes() {
      let amountSlots = [];
      for (let service = 0; service < this.services.length; service++) {
        let stringIndex = service.toString();
        amountSlots[service] = document.getElementById(`${stringIndex}`).value;
      }
      console.log(amountSlots);
    },
    // TODO: Make sure that this has the parts it needs to process report objects properly
    createReport() {
      // axios.post("/api/report-create/").then((response) => {
      //   this.report = response.data;
      // });
      console.log(this.report);
    },

    //* Get function for Report Services.
    // TODO reformat axios section
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
  mounted() {
    document.title = "Formulario de Reporte Inicial";
    this.getServices();
    this.getClients();
    this.getCause();
    this.getOutageType();
    this.setServiceZeroes();
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
