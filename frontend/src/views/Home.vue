<template>
  <div class="home is-centered">
    <div class="hero is-small is-grey is-light mb-2">
      <div class="hero-body has-text-centered">
        <p class="title mb-4">Tablero Principal De NOC Claro</p>
      </div>
    </div>
    <div
      id="button-row"
      class="buttons is-centered is-grouped text-center gap-2 d-md-block"
    >
      <div class="button has-background-info has-text-white is-large">
        <div class="card-content font-weight-bolder">
          <span
            ><router-link
              class="media-content has-text-white-bis"
              :to="{ name: 'Archive' }"
              >Archivo de Reportes</router-link
            ></span
          >
        </div>
      </div>
      <div class="button has-background-danger has-text-white is-large">
        <div class="card-content font-weight-bolder">
          <span
            ><router-link
              class="media-content has-text-white-bis"
              :to="{ name: 'InitialForm' }"
              >Iniciar Reporte</router-link
            ></span
          >
        </div>
      </div>
      <div class="button has-background-warning has-text-white is-large">
        <div class="card-content font-weight-bolder">
          <router-link
            :to="{ name: 'UpdateList' }"
            class="media-content has-text-white-bis"
            >Actualizar Reporte</router-link
          >
        </div>
      </div>
      <div class="button has-background-success has-text-white is-large">
        <div class="card-content font-weight-bolder">
          <span
            ><router-link
              class="media-content has-text-white-bis"
              :to="{ name: 'FinalizeList' }"
              >Finalizar Reporte</router-link
            ></span
          >
        </div>
      </div>
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
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      reportList: [],
    };
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
  computed: {
    isAuthenticated: function () {
      return this.$store.state.isAuthenticated;
    },
  },
  mounted() {
    // if (!this.isAuthenticated) {
    //   this.$router.push("/login");
    // }
    console.log(this.isAuthenticated);
    // console.log(this.$store.state.isAuthenticated);
    document.title = "Herramienta de Reporte del Claro NOC";
    this.getReportList();
    console.log(this.$store.state.access);
  },
};
</script>

<style scoped></style>
