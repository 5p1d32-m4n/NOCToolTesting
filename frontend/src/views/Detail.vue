<template>
  <div class="detail">
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
                <p v-for="client in report.clients" v-bind:key="client">{{ client.clients }}: {{client.client_amount}}</p>
                <p><strong>Total:</strong></p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Tipo de Averia:</td>
              <td>
                <p v-for="type in report.outage_type" v-bind:key="type">{{ type.outage_type }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Causa de Averia:</td>
              <td>
                <p v-for="cause in report.causes" v-bind:key="cause">{{ cause.causes }}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Equipos Impactados:</td>
              <td>
                <p v-for="service in report.services" v-bind:key="service">{{ service.services }}:{{service.service_amount}}</p>
              </td>
            </tr>
            <tr>
              <td class="is-narrow">Descripcion de la Averia</td>
              <td>
                <p>{{ report.notes }}</p>
              </td>
            </tr>
            <!-- <tr>
                <td class="is-narrow">Field</td>
                <td> <p>{{report.}}</p> </td>
            </tr> -->
          </tbody>
        </table>
      </div>
      <div class="column" id="map column">
        <strong class="title">Mapa de Impacto Municipal:</strong>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import axios from "axios";
export default {
  name: "Detail",
  data() {
    return {
      report: {},
    };
  },
  mounted() {
    this.getReportData();
    document.title = `Detalles de Reporte ${this.$route.params.noc_ticket}`
  },
  methods: {
    getReportData() {
      const noc_ticket_url = this.$route.params.noc_ticket;

      axios
        .get(`/api/report-detail/${noc_ticket_url}/`)
        .then((response) => {
          this.report = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>