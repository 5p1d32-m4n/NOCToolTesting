<template>
  <div class="home">
    <div class="container">
      <div class="container-fluid">
        <h1 class="mt-4">Dashboard</h1>
        <ol class="breadcrumb mb-4">
          <li class="breadcrumb-item active">Dashboard</li>
        </ol>
        <div class="row">
          <div class="col-xl-3 col-md-6">
            <div class="card bg-primary text-white mb-4">
              <div class="card-body">Report Archive</div>
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
              <div class="card-body">Initial Report</div>
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
              <div class="card-body">Report Update</div>
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
            <div class="card bg-success text-white mb-4">
              <div class="card-body" href="">Finalize Report</div>
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
                  <th scope="col">TSRM Ticket</th>
                  <th scope="col">Type Of Outage</th>
                  <th scope="col">Amount of Affected Clients</th>
                  <th scope="col">Impacted Municipalities</th>
                </tr>
              </thead>

              <tbody>
                <!-- start making the for loop here -->
                <tr v-for="report in reports" :key="report.pk">
                  <td>
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

                  <td v-for="outage in report.outage_type" :key="outage.id">
                    {{ outage.outage_type }}
                  </td>
                  <td
                    v-for="client_amount in report.clients"
                    :key="client_amount.id"
                  >
                    {{ client_amount.client_amount }}
                  </td>

                  <td
                    v-for="municipality in report.municipalities.split('+')"
                    :key="municipality"
                  >
                    {{ municipality }},
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
