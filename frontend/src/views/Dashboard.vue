<template>
  <b-container fluid="1" class="p-3">
    <b-row>
      <b-jumbotron
        class="text-center w-100 p-3 h-25 d-inline-block"
        header="Tablero del NOC"
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
      <RepList :reportList="reports" />
    </b-row>
    <router-link rel="prev" :to="{ name: 'Dashboard' }"
      >Previous Page</router-link
    >
    <router-link rel="next" :to="{ name: 'Dashboard' }">Next Page</router-link>
    <!-- <div>
      <h1>Hello {{ userInfo.first_name }}</h1>
    </div> -->
  </b-container>
</template>

<script>
import RepList from '@/components/RepList.vue'
import { mapState, mapActions } from 'vuex'
export default {
  name: 'Dashboard',
  components: {
    RepList,
  },
  methods: {
    async fetchReportList() {
      try {
        await this.$store.dispatch('report/fetchReports')
      } catch (err) {
        console.log('there was an error fetching reports')
      }
    },
  },
  created() {
    try {
      this.fetchReportList()
    } catch (err) {
      console.log(err)
    }
  },
  computed: {
    rows() {
      return this.reports.length
    },

    ...mapState('report', ['reports', 'reportTotal']),
    ...mapActions('report', ['fetchReports']),

    // ...mapState('user', ['userInfo']),
  },
}
</script>

<style lang="scss" scoped></style>
