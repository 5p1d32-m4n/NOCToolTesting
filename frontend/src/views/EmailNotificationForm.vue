<template>
  <div class="notificationForm">
    <div class="hero is-small is-gray is-light mb-2">
      <div class="hero-body has-text-centered">
        <p class="title mb-4">Reporte De Averia Mayor</p>
        <p class="subtitle mt-4">
          Reporte Identificado: {{ report.noc_ticket }}
        </p>
      </div>
    </div>
    <div class="columns">
      <div class="column" id="table-column">
        <p class="title">
          <strong>Tabla de Reporte:</strong>
        </p>
        <table class="table is-bordered is-striped is-hoverable">
          <tbody>
            <tr>
              <td class="is-narrow">Taquilla del NOC:</td>
              <td>{{ report.noc_ticket }}</td>
            </tr>
            <tr>
              <td class="is-narrow">Ultimo Estado de Reporte:</td>
              <td>
                <p>{{ report.report_type }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Taquilla de Tercero:</td>
              <td>
                <p>{{ report.third_party_ticket }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Fecha de Averia:</td>
              <td>
                <p>{{ report.date_of_outage }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Tiempo de Averia:</td>
              <td>
                <p>{{ report.time_of_outage }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Municipios Impactados:</td>
              <td>
                <p>{{ report.municipalities }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Clientes Impactados</td>
              <td>
                <p
                  v-for="(value, client) in report.clients"
                  v-bind:key="client"
                >
                  {{ client }}: {{ value }}
                </p>
                <p>
                  <strong>Total: {{ totalImpactedClients }}</strong>
                </p>
                <p></p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Tipo de Averia:</td>
              <td>
                <p>
                  {{ report.outage_type }}
                </p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Causa de Averia:</td>
              <td>
                <p>
                  {{ report.causes }}
                </p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Equipos Impactados:</td>
              <td>
                <p
                  v-for="(value, service) in report.services"
                  v-bind:key="service"
                >
                  {{ service }}: {{ value }}
                </p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Descripcion de la Averia</td>
              <td>
                <p>{{ report.notes }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="flexbox column mt-auto mb-auto" id="map_column">
        <strong class="title">Mapa de Impacto Municipal:</strong>

        <CheckboxSvgMap
          v-model="selectedMunicipalities"
          :map="PuertoRico"
          :value="selectedMunicipalities"
        />

        <b-alert variant="danger" show class="w-100 h-50 mt-0"
          ><p>{{ report.notes }}</p></b-alert
        >
      </div>
    </div>
    <div class="hero is-small is-gray is-light mb-2">
      <div class="hero-body has-text-centered">
        <p class="title mb-4">Notificación De Averia Mayor</p>
        <p class="subtitle mt-4">
          Reporte a Notificar: {{ report.noc_ticket }}
        </p>
      </div>
    </div>
    <div id="form">
      <form>
        <div class="columns">
          <div class="column">
            <div class="row">thing 1</div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico";
import { getLocationName, getSelectedLocationName } from "../utilities";
export default {
  name: "EmailNotificationForm",
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
      pointedLocation: null,
      focusedLocation: null,
      PuertoRico,
      componentKey: 0,
    };
  },
  watch: {
    selectedMunicipalities: function () {
      console.log(this.selectedMunicipalities);
      this.selectedMunicipalities = [];
      this.selectedMunicipalities = this.report.municipalities;
    },
  },
  computed: {
    clientName() {
      for (let client = 0; client < this.report.clients.length; client++) {
        const element = this.report.clients[client].keys;
        console.log(element);
      }
      return this.element;
    },
    totalImpactedClients() {
      return Object.keys(this.report.clients).reduce(
        (sum, values) => sum + parseInt(this.report.clients[values] || 0),
        0
      );
    },
    selectedMunicipalities: function () {
      let selection = [];
      selection = this.report.municipalities.split(",");
      return selection;
    },
  },
  methods: {
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
          this.report.report_type = response.data.report_type;
          this.report.noc_ticket = response.data.noc_ticket;
          this.report.third_party_ticket = response.data.third_party_ticket;
          this.report.date_of_outage = response.data.date_of_outage;
          this.report.time_of_outage = response.data.time_of_outage;
          this.report.notes = response.data.notes;
          this.report.municipalities = response.data.municipalities;
          this.report.outage_type = response.data.outage_type;
          this.report.causes = response.data.causes;
          this.report.services = JSON.parse(response.data.services);
          this.report.clients = JSON.parse(response.data.clients);
          console.log(this.report);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    setMap() {
      this.selectedMunicipalities = this.report.municipalities;
    },
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
  created() {
    document.title = `Notificación de Reporte ${this.$route.params.noc_ticket}`;
    this.getReportData();
    this.setMap();
  },
  mounted() {},
};
</script>
