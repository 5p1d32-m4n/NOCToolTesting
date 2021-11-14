<template>
  <div class="update-list is-centered">
    <div class="hero is-small is-grey is-light mb-2">
      <div class="hero-body has-text-centered">
        <p class="title mb-4">Lista de Reportes a Finalizar</p>
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
          v-for="report in filteredList"
          :key="report.noc_ticket"
          v-bind:report="report"
        >
          <td>
            <router-link
              v-bind:to="{
                name: 'FinalizeForm',
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
  name: "FinalizeList",
  data() {
    return {
      finalizableList: [],
    };
  },
  components: {},
  computed:{
    filteredList: function () {
      let shortList = []
      let fullList = this.finalizableList;

      for (let index = 0; index < fullList.length; index++) {
        if (fullList[index].report_type != "Finalizado") {
          shortList.push(fullList[index])
        }
      }

      return shortList
    }
  },
  methods: {
    getFinalizableList() {
      axios
        .get("/api/report-update-list/")
        .then((response) => {
          this.finalizableList = response.data;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
  },
  mounted() {
    document.title = "Lista de Reportes Actualizables";
    this.getFinalizableList();
  },
};
</script>

<style scoped></style>