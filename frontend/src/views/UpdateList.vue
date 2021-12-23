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
          <th>Tipo de Averia</th>
        </tr>
        <tr
          v-for="report in updateableList"
          :key="report.noc_ticket"
          v-bind:report="report"
        >
          <td>
            <router-link
              v-bind:to="{
                name: 'UpdateForm',
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
        .get("/api/report-update-list/", {
          headers: {
            /**
             * This is where we set our @Authorization to @JWT
             */
            Authorization: `JWT ${this.$store.state.access}`,
            "Content-Type": "application/json",
          },
        })
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

<style scoped></style>
