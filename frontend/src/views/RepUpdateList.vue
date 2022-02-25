<template>
  <b-container fluid="1" class="p-3">
    <b-row>
      <b-jumbotron
        class="text-center w-100 p-3 h-25 d-inline-block"
        header="Reportes Actualizables"
        header-level="4"
        container-fluid="1"
        align-h="center"
      ></b-jumbotron>
    </b-row>
    <b-row class="p-3">
      <b-col>
        <b-button size="lg" block variant="primary" :to="{ name: 'RepArchive' }"
          >Archivo de NOC</b-button
        >
      </b-col>
      <b-col>
        <b-button size="lg" block variant="danger" :to="{ name: 'RepCreate' }"
          >Iniciar Reporte</b-button
        >
      </b-col>
      <b-col>
        <b-button
          size="lg"
          block
          variant="warning"
          :to="{ name: 'RepUpdateList' }"
          >Actualizar Reporte</b-button
        >
      </b-col>
      <b-col>
        <b-button
          size="lg"
          block
          variant="success"
          :to="{ name: 'RepFinalizeList' }"
          >Finalizar Reporte</b-button
        >
      </b-col>
    </b-row>
    <b-row>
      <RepList :reportList="updatableReportList" />
    </b-row>
    <router-link rel="prev" :to="{ name: 'Dashboard' }"
      >Previous Page</router-link
    >
    <router-link rel="next" :to="{ name: 'Dashboard' }">Next Page</router-link>
  </b-container>
</template>

<script>
import RepList from '@/components/RepList.vue'
import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  name: 'RepUpdateList',
  components: {
    RepList,
  },
  methods: {},
  created() {
    this.fetchReports
  },
  computed: {
    ...mapState('report', ['reports', 'reportTotal']),
    ...mapActions('report', ['fetchReports']),
    ...mapGetters('report', ['getUpdatableReportList']),
    ...mapState('user', ['userInfo']),
    rows() {
      return this.reports.length
    },
    updatableReportList() {
      this.fetchReports
      return this.getUpdatableReportList
    },
  },
}
</script>

<style></style>
