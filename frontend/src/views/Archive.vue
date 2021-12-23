<template>
  <b-container fluid>
    <div class="title">
      <p>Formulario de busqueda:</p>
    </div>
    <div class="table-container is-centered">
      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <tr>
          <th>Taquilla NOC</th>
          <th>Boleto de Tercero</th>
          <th>Municipios Impactados</th>
          <th>Total de Clientes Impactados</th>
        </tr>
        <tr
          v-for="report in reportList"
          :key="report.noc_ticket"
          v-bind:report="report"
        >
          <td>
            <router-link
              v-bind:to="{
                name: 'Detail',
                params: { noc_ticket: report.noc_ticket },
              }"
            >
              {{ report.noc_ticket }}
            </router-link>
          </td>
          <td>{{ report.third_party_ticket }}</td>
          <td>{{ report.municipalities }}</td>
          <td>{{ report.outage_type }}</td>
        </tr>
      </table>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Archive",
  data() {
    return {
      reportList: [],
    };
  },
  components: {},
  mounted() {
    document.title = "Archivo de Reportes";
    this.getReportList();
  },
  methods: {
    getReportList() {
      axios
        .get("/api/report-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.reportList = response.data;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
  },
};
</script>
<style scoped></style>
