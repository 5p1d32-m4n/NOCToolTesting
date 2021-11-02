<template>
  <b-container fluid>
    <form v-on:submit.prevent="createReport">
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
                          <!-- checkbox -->
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="selectedClients"
                                :value="client"
                                >&nbsp;{{ client }}</b-form-checkbox
                              >
                            </div>
                          </td>
                          <!-- Number input. -->
                          <td>
                            <!-- <div>
                              <input
                                type="number"
                                name="clientAmount"
                                value="0"
                                min="0"
                                :id="client"
                              />
                            </div> -->
                            
                              <b-form-radio-group
                                :id="client"
                                :options="amountOptions"
                                stacked
                              >
                              </b-form-radio-group>
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
                text="Tipo de Averias"
                class="m-2 d-grid mt-3"
                menu-class="w-100"
              >
                <b-dropdown-form>
                  <b-row align-h="center">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">Tipos de Averias:</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(type, index) in outage_type" :key="index">
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="selectedOutageTypes"
                                :value="outage_type"
                                >&nbsp;{{ type }}</b-form-checkbox
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
          <div>
            <input
              type="text"
              class="form-control"
              id="notes"
              v-model="reportNotes"
              :maxlength="500"
            />
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
      reportType: "Inicial",
      reportNOCTicket: "",
      reportThirdPartyTicket: "",
      reportOutageDate: null,
      reportOutageTime: null,
      reportNotes: "",
      amountOptions: [
        {
          text: "1,000",
          value: "1,000",
        },
        {text: "5,000",
          value: "5,000",},
        {text: "10,000",
          value: "10,000",},
      ],
      selectedMunicipalities: [],
      selectedOutageTypes: [],
      selectedCauses: [],
      selectedServices: [],
      selectedServiceAmount: {
        type: Array,
        default: "0",
      },
      selectedClients: [],
      selectedClientAmount: {
        type: Array,
        default: "0",
      },
      ServicesObject: null,
      ClientsObject: null,
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

    // * Function that creates report Objects
    createReport() {
      this.buildServiceObject();
      this.buildClientObject();
      let tempReport = {
        report_type: this.reportType,
        noc_ticket: this.reportNOCTicket,
        third_party_ticket: this.reportThirdPartyTicket,
        date_of_outage: this.reportOutageDate,
        time_of_outage: this.reportOutageTime,
        notes: this.reportNotes,
        municipalities: this.selectedMunicipalities.toString(),
        outage_type: this.selectedOutageTypes.toString(),
        causes: this.selectedCauses.toString(),
        services: this.ServicesObject,
        clients: this.ClientsObject,
      };
      // * The problem data here seems to be causes, municipalities and outage_type.
      // * The string format appears to be incorrect.
      console.log(tempReport);
      // axios.post("/api/report-create/", tempReport).catch((error) => {
      //   console.log(error.response);
      // });
      // this.$router.push({
      //   name: "Detail",
      //   params: { noc_ticket: tempReport.noc_ticket },
      // });
      // window.location.reload();
    },
    //* Function that builds the Service portion of the Outage report in JS forma
    buildServiceObject() {
      // !Testing new Objec building method.
      let serviceName = this.selectedServices;
      let serviceAmount = [];

      for (let entry = 0; entry < serviceName.length; entry++) {
        serviceAmount.push(document.getElementById(serviceName[entry]).value);
      }
      // * TESTING: stringify this so it will match the Djando service field.
      console.log(serviceName);
      console.log(serviceAmount);
      let serviceObject = serviceName.reduce(
        (acc, key, index) =>
          Object.assign(acc, { [key]: serviceAmount[index] }),
        {}
      );
      this.ServicesObject = JSON.stringify(serviceObject);
      let servicesString = this.ServicesObject;
      servicesString.replace(RegExp("\\\\", "g"), "");
      this.ServicesObject = servicesString;
      console.log("Stringy Service: " + this.ServicesObject);
    },
    //* Fucntion that builds the Client portion of the outage report in Json format.
    buildClientObject() {
      // ! Testing
      let clientName = this.selectedClients;
      let clientAmount = [];

      for (let entry = 0; entry < clientName.length; entry++) {
        clientAmount.push(document.getElementById(clientName[entry]).value);
      }
      //*  TESTING: stringify this so it will match the Djando service field.
      let clientObject = clientName.reduce(
        (acc, value, index) => ((acc[value] = clientAmount[index]), acc),
        {}
      );
      this.ClientsObject = JSON.stringify(clientObject);
      console.log("Stringy Client: " + this.ClientsObject);
    },
    setServiceZeroes() {
      let amountSlots = [];
      for (let service = 0; service < this.services.length; service++) {
        let stringIndex = service.toString();
        amountSlots[service] = document.getElementById(`${stringIndex}`).value;
      }
      console.log(amountSlots);
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
