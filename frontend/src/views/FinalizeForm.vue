<template>
  <b-container fluid>
    <form v-on:submit.prevent="UpdateReport">
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
                          <!-- Checkbox -->
                          <td>
                            <div>
                              <b-form-checkbox
                                v-model="clientsFormArray"
                                :value="client"
                                >&nbsp;{{ client }}</b-form-checkbox
                              >
                            </div>
                          </td>
                          <!-- Number Input -->
                          <td>
                            <div>
                              <input
                                type="radio"
                                :name="client"
                                v-model="cliAmountFormArray[index]"
                                :value="1000"
                              />1,000+
                              <input
                                type="radio"
                                :name="client"
                                v-model="cliAmountFormArray[index]"
                                :value="5000"
                              />5,000+
                              <input
                                type="radio"
                                :name="client"
                                v-model="cliAmountFormArray[index]"
                                :value="10000"
                              />10,000+
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
            >Finalizar Reporte</b-button
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
  name: "FinalizeForm",
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      report: {
        report_type: "Finalizado",
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
      clientRawAmount: [],
      clientRadioObject: [],
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
      newServices: {},
      newClients: {},
      PuertoRico,
    };
  },
  computed: {
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
    UpdateReport() {
      // ! Testing making the report update
      this.buildNewClientObject();
      this.buildNewServiceObject();
      var tempReport = {
        report_type: "Finalizado",
        noc_ticket: this.report.noc_ticket,
        third_party_ticket: this.report.third_party_ticket,
        date_of_outage: this.report.date_of_outage,
        time_of_outage: this.report.time_of_outage,
        notes: this.report.notes,
        municipalities: this.report.municipalities.toString(),
        outage_type: this.report.outage_type.toString(),
        causes: this.report.causes.toString(),
        services: this.newServices,
        clients: this.newClients,
      };
      console.log("testing new update report: " + JSON.stringify(tempReport));

      /**
       * Axios PUT verb for backend API
       */
      axios
        .put(`/api/report-update/${tempReport.noc_ticket}/`, tempReport, {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response);
        });
      this.$router.push({
        name: "Detail",
        params: { noc_ticket: tempReport.noc_ticket },
      });
      window.location.reload();
    },
    getReportData() {
      const noc_ticket_url = this.$route.params.noc_ticket;

      axios
        .get(`/api/report-detail/${noc_ticket_url}/`, {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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
          let cliAmountArray = [];
          let reportedCliAmount = Object.values(
            JSON.parse(response.data.clients)
          );
          // ! I need to add original amount array
          this.clientRawAmount = reportedCliAmount;
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
          // console.log(
          //   "reported clients: " +
          //     clientsArray +
          //     "\n" +
          //     "API clients: " +
          //     clientList +
          //     "\n" +
          //     "reported client amount: " +
          //     reportedCliAmount +
          //     "\n" +
          //     "client amount with zero: " +
          //     cliAmountArray
          // );
          this.clientsFormArray = clientsArray;
          this.cliAmountFormArray = cliAmountArray;
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
        .get("/api/services-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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
        .get("/api/clients-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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
        .get("/api/cause-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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
        .get("/api/outage_type-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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
    buildNewServiceObject() {
      // !Testing new Objec building method.
      let serviceName = this.servicesFormArray;
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
      this.newServices = JSON.stringify(serviceObject);
      let servicesString = this.newServices;
      servicesString.replace(RegExp("\\\\", "g"), "");
      this.newServices = servicesString;
      console.log("new service Object: " + this.newServices);
    },
    //* Fucntion that builds the Client portion of the outage report in Json format.
    buildNewClientObject() {
      // ! Testing
      let clientName = this.clientsFormArray;
      let clientAmount = [];
      // Client amount fetching
      for (let index = 0; index < clientName.length; index++) {
        let radioGroupName = document.getElementsByName(clientName[index]);
        // let amountToCheck = clientName[index]

        // Radio group loop.
        for (let button = 0; button < radioGroupName.length; button++) {
          if (radioGroupName[button].checked == true) {
            console.log("checked" + radioGroupName[button].value);
            clientAmount.push(radioGroupName[button].value);
          }
        }
      }
      // for (let entry = 0; entry < clientName.length; entry++) {
      //   clientAmount.push(document.getElementById(clientName[entry]).value);
      // }
      let clientObject = clientName.reduce(
        (acc, value, index) => ((acc[value] = clientAmount[index]), acc),
        {}
      );
      this.newClients = JSON.stringify(clientObject);
      console.log("testing client object: " + this.newClients);
    },

    //* Setting the radio buttons.
    setClientRadio() {
      // this is the client amount array fetched from the report.
      let reportedCliAmount = this.cliAmountFormArray;
      let presetAmount = [];
      let reportedClients = Object.keys(this.report.clients);

      // For Loop to remove zeroes from the amount array.
      // for (let index = 0; index < reportedCliAmount.length; index++) {
      //   if (reportedCliAmount[index] == 0) {
      //     reportedCliAmount.splice(index,1)
      //   }
      // }

      // Reported client name for loop.
      for (let name = 0; name < reportedClients.length; name++) {
        let radioGroupName = document.getElementsByName(reportedClients[name]);
        let amountToCheck = reportedCliAmount[name];

        // Radio Button input element for loop
        for (let button = 0; button < radioGroupName.length; button++) {
          if (amountToCheck == radioGroupName[button].value) {
            radioGroupName[button].checked = true;
          }
        }
      }
      this.cliAmountFormArray = reportedCliAmount;
      // console Log testing output:
      console.log("reported client amount: " + reportedCliAmount);
      console.log("client amount array" + this.cliAmountFormArray);
      console.log("new amount with zeros: " + presetAmount);
    },

    clientObjectBuilder() {
      let testObject = [];
      let allClients = this.APIclients;
      let checkedClients = this.clientsFormArray;
      let checkedClientAmounts = this.clientRawAmount;

      // For Loop that goes through all the API clients:
      for (let index = 0; index < allClients.length; index++) {
        let client = allClients[index];
        // console.log("API client in loop: " + client)

        // for loop that has the previously checked clients:
        for (let subIndex = 0; subIndex < checkedClients.length; subIndex++) {
          let checked = checkedClients[subIndex];
          // console.log("Checked client in loop: " + checked)

          // match conditional
          if (client == checked) {
            console.log("match");
          } else {
            console.log("no match.");
          }
        }
      }

      console.log("test object: " + JSON.stringify(testObject));
      console.log("API Clients: " + allClients);
      console.log("Prev selected Clients: " + checkedClients);
      console.log("Amounts in form: " + this.cliAmountFormArray);
      console.log("Prev selected amounts: " + checkedClientAmounts);
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
    document.title = `Forumulario de Finalizacion ${this.$route.params.noc_ticket}`;
  },
  mounted() {
    this.getServices();
    this.getClients();
    this.getCause();
    this.getOutageType();
    this.getReportData();
    this.setClientRadio();
    this.setReportServiceObjects();
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
