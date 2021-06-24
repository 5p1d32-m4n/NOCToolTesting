<template>
  <div class="detail container">
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4">Report Details</h1>
        <p class="lead">Highlighted Report Table</p>
      </div>
    </div>
    <h1 >{{ noc_ticket }}</h1>
    <p >{{ notes }}</p>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "../common/api.service.js";
export default {
  name: "Report",
  props: {
    report_type:{
      type: String,
      required: false
    },
    noc_ticket:{
      type: String,
      required: false
    },
    third_party_ticket:{
      type: String,
      required: false
    },
    date_of_outage:{
      type: String,
      required: false
    },
    time_of_outage:{
      type: String,
      required: false
    },
    notes:{
      type: String,
      required: false
    },
    municipalities:{
      type: String,
      required: false
    },
    services:{
      type: String,
      required: false
    },
    clients:{
      type: String,
      required: false
    },
    outage_type:{
      type: String,
      required: false
    },
    causes:{
      type: String,
      required: false
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
      apiService(endpoint).then(data => {
        Object.assign(this.report, data);
        // this.report = data;
        console.log(data);
      });
    },
  },
  created() {
    this.getReportData();
  },
};
</script>
