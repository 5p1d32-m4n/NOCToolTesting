<template>
  <div class="detail">
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4">Report Details: {{ noc_ticket }}</h1>
        <p class="lead">Highlighted Report Table</p>
      </div>
    </div>
    <div class="card-deck container-fluid" id="table-card">
      <div class="card">
        <div class="card-body float-left">
          <table class="table-hover table-bordered container-fluid">
            <tbody class="table-striped">
              <tr>
                <th scope="col">Taquilla de NOC:</th>
                <td>{{ noc_ticket }}</td>
              </tr>
              <tr>
                <th scope="col">Taquilla de tercero:</th>
                <td>{{ third_party_ticket }}</td>
              </tr>
              <tr>
                <th scope="col">Estado de Reporte:</th>
                <td>{{ report_type }}</td>
              </tr>
              <tr>
                <th scope="col">Fecha de Evento:</th>
                <td>{{ date_of_outage }}</td>
              </tr>
              <tr>
                <th scope="col">Tiempo de Evento:</th>
                <td>{{ time_of_outage }}</td>
              </tr>
              <tr>
                <th scope="col">Municipios Impactados:</th>
                <td>{{ municipalities }}</td>
              </tr>
              <tr>
                <th scope="col">Clientes Impactados</th>
                <!-- this is going to be a v-for -->
                <td>
                  <p v-for="client in clients" :key="client">
                    {{ client.clients }}: {{ client.client_amount }}
                  </p>
                </td>
              </tr>
              <tr>
                <th scope="col">Servicios Impactados:</th>
                <td>
                  <p v-for="service in services" :key="service">
                    {{ service.services }}: {{ service.service_amount }}
                  </p>
                </td>
              </tr>
              <tr>
                <th scope="col">Typo de Averia:</th>
                <td>
                  <p v-for="item in outage_type" :key="item">
                    {{ item.outage_type }}
                  </p>
                </td>
              </tr>
              <tr>
                <th scope="col">Causas de Averia:</th>
                <td>
                  <p v-for="cause in causes" :key="cause">{{ cause.causes }}</p>
                </td>
              </tr>
              <tr>
                <th scope="col">Notas:</th>
                <td>{{ notes }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="card align-self-center" id="map-card">
        <div class="card-image">
          <div class="container">
            <img
              id="pr-map"
              src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/USA_Puerto_Rico_labeled.svg/800px-USA_Puerto_Rico_labeled.svg.png"
              style=""
            />
          </div>
        </div>
      </div>
    </div>
    <div class="card container-fluid" id="comment-card"></div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "../common/api.service.js";
export default {
  name: "detail",
  props: {
    report_type: {
      type: String,
      required: false,
    },
    noc_ticket: {
       type: String
    }
    ,
    third_party_ticket: {
      type: String,
      required: false,
    },
    date_of_outage: {
      type: String,
      required: false,
    },
    time_of_outage: {
      type: String,
      required: false,
    },
    notes: {
      type: String,
      required: false,
    },
    municipalities: {
      type: String,
      required: false,
    },
    services: {
      type: Array,
      required: false,
    },
    clients: {
      type: Array,
      required: false,
    },
    outage_type: {
      type: Array,
      required: false,
    },
    causes: {
      type: Array,
      required: false,
    },
  },
  data() {
    return {
      report: {},
    };
  },
  methods: {
    getReportData() {
      let endpoint = `/api/report-detail/${this.noc_ticket}/`;
      apiService(endpoint).then((data) => {
        Object.assign(this.report, data);
        this.report = data;
        console.log(this.report);
      });
    },
  },
  created() {
    this.getReportData();
  },
};
</script>

<style scoped>
#pr-map {
  /* -webkit-transform: rotate(90deg);
  -moz-transform: rotate(90deg);
  -o-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg); */

  object-fit: cover;
}
</style>