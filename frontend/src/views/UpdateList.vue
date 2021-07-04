<template>
  <div class="update-list is-centered">
    <div class="hero is-small is-grey is-light mb-2">
      <div class="hero-body has-text-centered">
        <p class="title mb-4">Lista de Reportes Actualizables</p>
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
          v-for="report in updateableList"
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
          <td>
            <p
              v-for="outage_type in report.outage_type"
              :key="outage_type.outage_type"
            >
              {{ outage_type.outage_type }}
            </p>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UpdateList",
  data() {
    return {
      updateableList: [],
    };
  },
  components: {},
  methods: {
    getUpdatableList() {
      axios
        .get("/api/report-update-list/")
        .then((response) => {
          this.updateableList = response.data;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
  },
  mounted() {
    document.title = "Lista de Reportes Actualizables";
    this.getUpdatableList();
  },
};
</script>

<style scoped>
</style>
