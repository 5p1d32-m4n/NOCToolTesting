<template>
  <div class="update-list">
    <div class="container">
      <div class="container-fluid">
        <h1 class="mt-4">Reportes Actualizables</h1>
        <ol class="breadcrumb mb-4">
          <li class="breadcrumb-item active">Tablero/Reportes Actualizables</li>
        </ol>

        <div class="row">
          <div class="container container-fluid">
            <table class="table table-hover table-bordered">
              <thead>
                <tr>
                  <th scope="col">NOC Ticket</th>
                  <th scope="col">Tipo de Averia</th>
                  <th scope="col">Cantidad de Cliente Impactados</th>
                  <th scope="col">Municipios Impactados</th>
                </tr>
              </thead>

              <tbody>
                <!-- start making the for loop here -->
                <tr v-for="report in reports" :key="report.pk">
                  <td>
                    <p>
                      <a> {{ report.noc_ticket }}</a>
                    </p>
                  </td>

                  <td>
                    <p v-for="outage in report.outage_type" :key="outage.id">
                      {{ outage.outage_type }}
                    </p>
                  </td>
                  <td>
                    <p v-for="amount in report.clients" :key="amount.id">
                      {{ amount.client_amount }},
                    </p>
                  </td>

                  <td>
                    <p
                      v-for="municipality in report.municipalities.split('+')"
                      :key="municipality"
                    >
                      {{ municipality }},
                    </p>
                  </td>
                </tr>
                <!-- End it here. -->
              </tbody>
            </table>
          </div>
        </div>

        <div class="row">
          <h1>
            <!-- {#            Mini Charts go here.#} -->
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { apiService } from "../common/api.service.js";
export default {
  name: "listUpdate",
  data() {
    return {
      reports: [],
    };
  },
  methods: {
    getReports() {
      let endpoint = `api/report-update-list/`;
      apiService(endpoint).then((data) => {
        this.reports.push(...data);
      });
    },
  },
  created() {
    this.getReports();
    console.log(this.reports);
  },
};
</script>
<style scoped>
</style>