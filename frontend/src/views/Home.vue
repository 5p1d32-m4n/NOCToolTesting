<template>
  <div class="home">
    <div class="container">
      <div class="container-fluid">
        <h1 class="mt-4">Tablero</h1>
        <ol class="breadcrumb mb-4">
          <li class="breadcrumb-item active">Tablero</li>
        </ol>
        <div class="row">
          <div class="col-xl-3 col-md-6">
            <div class="card bg-primary text-white mb-4">
              <div class="card-body">Archivo de Reportes</div>
              <div
                class="
                  card-footer
                  d-flex
                  align-items-center
                  justify-content-between
                "
              >
                <a class="small text-white stretched-link" href=""
                  >View Details</a
                >
                <div class="small text-white">
                  <i class="fas fa-angle-right"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6">
            <div class="card bg-danger text-white mb-4">
              <div class="card-body">Iniciar Reporte</div>
              <div
                class="
                  card-footer
                  d-flex
                  align-items-center
                  justify-content-between
                "
              >
                <a class="small text-white stretched-link" href=""
                  >View Details</a
                >
                <div class="small text-white">
                  <i class="fas fa-angle-right"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6">
            <div class="card bg-warning text-white mb-4">
              <div class="card-body">Actualizar Reporte</div>
              <div
                class="
                  card-footer
                  d-flex
                  align-items-center
                  justify-content-between
                "
              >
                <router-link class="small text-white stretched-link" :to="{name:'listUpdate', params:{reports:reports}}"
                  >View Details</router-link
                >
                <div class="small text-white">
                  <i class="fas fa-angle-right"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6">
            <div class="card bg-success text-white mb-4">
              <div class="card-body" href="">Finalizar Reporte</div>
              <div
                class="
                  card-footer
                  d-flex
                  align-items-center
                  justify-content-between
                "
              >
                <a class="small text-white stretched-link" href=""
                  >View Details</a
                >
                <div class="small text-white">
                  <i class="fas fa-angle-right"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <h1>Summary Table</h1>
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
                  <td id="report-noc-ticket">
                    <router-link
                      :to="{
                        name: 'detail',
                        params: {
                          report_type: report.report_type,
                          noc_ticket: report.noc_ticket,
                          third_party_ticket: report.third_party_ticket,
                          date_of_outage: report.date_of_outage,
                          time_of_outage: report.time_of_outage,
                          notes: report.notes,
                          municipalities: report.municipalities,
                          services: report.services,
                          clients: report.clients,
                          outage_type: report.outage_type,
                          causes: report.causes,
                          report: report,
                        },
                      }"
                    >
                      {{ report.noc_ticket }}</router-link
                    >
                  </td>

                  <td id="report-outage-type">
                    <p v-for="outage in report.outage_type" :key="outage.id">
                      {{ outage.outage_type }}
                    </p>
                  </td>
                  <td id="report-cient-amount">
                    <p v-for="amount in report.clients" :key="amount.id">
                      {{ amount.client_amount }},
                    </p>
                  </td>

                  <td id="report-municipalities">
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
// @ is an alias to /src
import { apiService } from "../common/api.service.js";
export default {
  name: "Home",
  data() {
    return {
      reports: [],
    };
  },
  methods: {
    getReports() {
      let endpoint = `api/report-list`;
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
