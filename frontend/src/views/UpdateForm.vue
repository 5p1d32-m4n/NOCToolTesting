<template>
  <b-container fluid>
    <form v-on:submit.prevent="testFucntion">
      <!-- These are the text input fields (date and time included) -->
      <b-row>
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
                        <tr
                          v-for="(service, index) in APIservices"
                          :key="index"
                        >
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="servicesFormArray"
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
                                v-model="servAmountFormArray[index]"
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
            <!-- SERVICE DROPDOWN END-->
            <!-- CAUSE TYPE dropdown -->
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
                        <tr v-for="(cause, index) in APIcause" :key="index">
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
            <!-- CLIENT dropdown -->
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
                        <tr v-for="(client, index) in APIclients" :key="index">
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="clientsFormArray"
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
                                min="0"
                                v-model="cliAmountFormArray[index]"
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
                    :options="APIoutage_type"
                    v-model="report.outage_type"
                    stacked
                  ></b-form-checkbox-group>
                </b-dropdown-form>
              </b-dropdown>
            </b-form-group>
            <!-- Outage Type Dropdown End -->
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
// TODO: Duplicate the functionality from Impacted Services with Impacted Clients.
// TODO: Need to create new watchers for the service and clienta arryas.
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
        report_type: "Actualización",
        noc_ticket: "",
        third_party_ticket: "",
        date_of_outage: "",
        time_of_outage: "",
        notes: "",
        municipalities: [],
        outage_type: [],
        causes: [],
        services: {},
        clients: {},
      },
      servicesFormArray: [],
      servAmountFormArray: [],
      clientsFormArray: [],
      cliAmountFormArray: [],
      clientArray: [],
      reportType: "Actualización",
      APIservices: [],
      APIclients: [],
      APIoutage_type: [],
      APIcause: [],
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
    // reportedServices: {
    //   get: function () {
    //     let oldServ = [];
    //     oldServ = this.report.services;
    //     let arrayServices = [];
    //     arrayServices = Object.keys(oldServ);
    //     return arrayServices;
    //   },
    //   set: function () {},
    // },
    // computedServAmount: {
    //   get: function () {
    //     let allServices = [];
    //     let oldServices = [];
    //     let allAmounts = [];
    //     let oldServiceAmount = [];

    //     allServices = this.services;
    //     oldServices = Object.keys(this.report.services);
    //     oldServiceAmount = Object.values(this.report.services);

    //     /*
    //      *Here I initialize an array that is for the amounts started at zero
    //      *and change them later in the second for loop.
    //      */
    //     for (let entry = 0; entry < allServices.length; entry++) {
    //       allAmounts.push(0);
    //     }
    //     //* this is where we need to run the for loop with existance check
    //     for (let index = 0; index < allServices.length; index++) {
    //       let currentService = allServices[index];

    //       for (let subIndex = 0; subIndex < oldServices.length; subIndex++) {
    //         let reportService = oldServices[subIndex];
    //         //* Here we compare if the service from our api list matches the selected service from our report:

    //         if (currentService == reportService) {
    //           allAmounts[index] = oldServiceAmount[subIndex];
    //         }
    //       }
    //     }

    //     return allAmounts;
    //   },
    //   set: function () {},
    // },
    // computedImpactedClients: {
    //   get: function () {
    //     let oldImpClients = [];
    //     oldImpClients = this.report.clients;
    //     let reportImpClient = [];
    //     reportImpClient = Object.keys(oldImpClients);
    //     return reportImpClient;
    //   },
    //   set: function () {
    //     return "";
    //   },
    // },
    // computedImpCliAmounts: {
    //   get: function () {
    //     let allClients = [];
    //     let reportClients = [];
    //     let allCliAmounts = [];
    //     let reportCliAmounts = [];

    //     allClients = this.clients;
    //     reportClients = Object.keys(this.report.clients);
    //     reportCliAmounts = Object.values(this.report.clients);

    //     /*
    //      *Here we beggin an array full of zeroes the same size as
    //      *the array of all the impacted clients.
    //      */
    //     for (let index = 0; index < allClients.length; index++) {
    //       allCliAmounts.push(0);
    //     }

    //     /*
    //      * For loop that iterates through all the services then nest into
    //      * the report services and inserts the corresponding values into the
    //      * zero arra.
    //      */

    //     for (let index = 0; index < allClients.length; index++) {
    //       let currentClient = allClients[index];

    //       for (let subIndex = 0; subIndex < reportClients.length; subIndex++) {
    //         let oldImpClients = reportClients[subIndex];

    //         /*
    //          * Conditional that sets value array after comparing existing
    //          * entries to both arrays.
    //          */

    //         if (currentClient == oldImpClients) {
    //           allCliAmounts[index] = reportCliAmounts[subIndex];
    //         }
    //       }
    //     }
    //     console.log("cli amounts: " + allCliAmounts);
    //     return allCliAmounts;
    //   },
    //   set: function () {
    //     // return "";
    //   },
    // },

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
    // TODO: create an array handler.
    servicesArray: {
      deep: true,
      immediate: true,
      // handler: "testServiceArray",
    },
  },
  methods: {
    testServiceArray() {
      console.log("Setting Array!");
      let oldServices = [];
      oldServices = this.report.services;
      let passArray = Object.keys(oldServices);
      this.servicesArray = passArray;
      console.log(this.servicesArray);
    },
    testFucntion() {
      // ! Testing making the report update
      let tempReport = {
        report_type: this.report.report_type,
        noc_ticket: this.report.noc_ticket,
        third_party_ticket: this.report.third_party_ticket,
        date_of_outage: this.report.date_of_outage,
        time_of_outage: this.report.time_of_outage,
        notes: this.report.notes,
        municipalities: this.report.municipalities,
        outage_type: this.report.outage_type,
        causes: null,
        services: null,
        clients: null,
      }
      console.log("testing new update report: " + tempReport.outage_type)
    },
    getReportData() {
      const noc_ticket_url = this.$route.params.noc_ticket;

      axios
        .get(`/api/report-detail/${noc_ticket_url}/`)
        .then((response) => {
          /**
           * *Unique Report felds
           * *These are easily just set
           */
          this.report.report_type = "Actualización";
          this.report.noc_ticket = response.data.noc_ticket;
          this.report.third_party_ticket = response.data.third_party_ticket;
          this.report.date_of_outage = response.data.date_of_outage;
          this.report.time_of_outage = response.data.time_of_outage;
          this.report.notes = response.data.notes;
          this.report.causes = response.data.causes;
          /**
           * *This part of the report requires some string splicing.
           */
          let stringOutageType = response.data.outage_type;
          this.report.outage_type = stringOutageType.split(",");
          let stringMunicipalities = response.data.municipalities;
          this.report.municipalities = stringMunicipalities.split(",");
          /**
           * *This section is parcing the clients and services into objects
           */
          this.report.clients = JSON.parse(response.data.clients);
          this.report.services = JSON.parse(response.data.services);

          /**
           * the order of function calls has been fixed, we now have access to everything.
           */
          //* parsing services into an array
          let servicesArray = [];
          servicesArray = Object.keys(JSON.parse(response.data.services));
          //* putting services in API into an array.
          let serviceList = [];
          serviceList = this.APIservices;
          //* putting all the service values into an array
          let serviceAmountArray = [];
          let reportedServAmount = Object.values(
            JSON.parse(response.data.services)
          );

          /**
           ** This is the for loop that fills our larger array with zeroes.
           */
          for (let index = 0; index < serviceList.length; index++) {
            serviceAmountArray.push(0);
          }

          /**
           * For loop that searches services and sets the matching ones
           * to the reported amount.
           */
          for (let index = 0; index < serviceList.length; index++) {
            let currentService = serviceList[index];

            for (let subInex = 0; subInex < servicesArray.length; subInex++) {
              let reportService = servicesArray[subInex];

              if (currentService == reportService) {
                serviceAmountArray[index] = reportedServAmount[subInex];
              }
            }
          }
          /**
           * This is just the console log to test my objects and what not.
           */
          console.log(
            "API service call: " +
              serviceList +
              "\n" +
              "reported services: " +
              servicesArray +
              "\n" +
              "service amounts with zero: " +
              serviceAmountArray +
              "\n" +
              "service amounts from report:" +
              reportedServAmount +
              "\n"
          );
          this.servicesFormArray = servicesArray;
          this.servAmountFormArray = serviceAmountArray;

          /**
           * *This section is just repeating the process of the services
           * *with clients.
           */
          //* parsing clients into an array.
          let clientsArray = [];
          clientsArray = Object.keys(JSON.parse(response.data.clients));
          //* putting clients in API into an array.
          let clientList = [];
          clientList = this.APIclients;
          //* client amount values into an array
          let cliAmountArray = []
          let reportedCliAmount = Object.values(JSON.parse(response.data.clients))
          /**
           ** This is the for loop that fills our larger array with zeroes.
           */
          for (let index = 0; index < clientList.length; index++) {
            cliAmountArray.push(0);
          }
          /**
           * For loop that searches services and sets the matching ones
           * to the reported amount.
           */
          for (let index = 0; index < clientList.length; index++) {
            let currentService = clientList[index];

            for (let subInex = 0; subInex < clientsArray.length; subInex++) {
              let reportService = clientsArray[subInex];

              if (currentService == reportService) {
                cliAmountArray[index] = reportedCliAmount[subInex];
              }
            }
          }
          /**
           * * Console log to test client form data fetched from report.
           */
          console.log(
            "reported clients: " +
              clientsArray +
              "\n" +
              "API clients: " +
              clientList +
              "\n"+
              "reported client amount: "+ reportedCliAmount +
              "\n" +
              "client amount with zero: " + cliAmountArray
          );
          this.clientsFormArray = clientsArray
          this.cliAmountFormArray = cliAmountArray
          // console.log("report object" + this.report);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    setReportServiceObjects() {
      this.ServicesObject = this.oldServ;
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
          this.APIservices = uniqueServices;
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
          this.APIclients = uniqueClients;
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
          this.APIcause = uniqueCause;
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
          this.APIoutage_type = uniqueOutageType;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    //* Function that builds the Service portion of the Outage report in Json forma
    buildServiceObject() {
      // !Testing new Objec building method.
      let serviceName = this.oldServices;
      let serviceAmount = [];

      for (let entry = 0; entry < serviceName.length; entry++) {
        serviceAmount.push(document.getElementById(serviceName[entry]).value);
      }
      // * WORKS: stringify this so it will match the Djando service field.
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
    },
    //* Fucntion that builds the Client portion of the outage report in Json format.
    buildClientObject() {
      // ! Testing
      let clientName = this.selectedClients;
      let clientAmount = [];

      for (let entry = 0; entry < clientName.length; entry++) {
        clientAmount.push(document.getElementById(clientName[entry]).value);
      }
      let clientObject = clientName.reduce(
        (acc, value, index) => ((acc[value] = clientAmount[index]), acc),
        {}
      );
      this.ClientsObject = JSON.stringify(clientObject);
    },
    // * Function that Updates report Objects
    UpdateReport() {
      this.buildServiceObject();
      this.buildClientObject();
      let tempReport = {
        report_type: this.report.report_type,
        noc_ticket: this.report.noc_ticket,
        third_party_ticket: this.report.third_party_ticket,
        date_of_outage: this.report.date_of_outage,
        time_of_outage: this.report.time_of_outage,
        notes: this.report.notes,
        municipalities: this.report.municipalities.toString(),
        outage_type: this.report.outage_type.toString(),
        causes: this.causes.toString(),
        services: this.ServicesObject,
        clients: this.ClientsObject,
      };
      // * The problem data here seems to be causes, municipalities and outage_type.
      // * The string format appears to be incorrect.
      console.log(tempReport);
      axios.post("/api/report-create/", tempReport).catch((error) => {
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
  beforeMounted() {
    document.title = "Forumulario de Actualizacion";
  },
  mounted() {
    this.getServices();
    this.getClients();
    this.getCause();
    this.getOutageType();
    this.setReportServiceObjects();
    this.testFucntion();
    this.getReportData();
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
