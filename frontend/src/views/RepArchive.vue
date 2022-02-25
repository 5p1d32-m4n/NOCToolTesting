<template>
  <b-container fluid="1" class="p-3">
    <b-row>
      <b-jumbotron
        class="text-center w-100 p-3 h-25 d-inline-block"
        header="Archivo de Reportes del NOC"
        header-level="4"
        container-fluid="1"
        align-h="center"
      ></b-jumbotron>
    </b-row>
    <b-row class="p-3">
      <b-col>
        <b-button size="lg" block variant="primary" :to="{}"
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
      <div class="text-center w-100 p-3 title">
        <p>Formulario de busqueda:</p>
      </div>
    </b-row>
    <b-row class="p-3 d-block">
      <b-form @submit.prevent="test">
        <b-card bg-variant="light">
          <b-row>
            <b-col>
              <b-form-group label="Boleto del NOC:">
                <b-form-input v-model="searchNOCTicket"></b-form-input>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group label="Boleto de Tercero:">
                <b-form-input v-model="searchThirdPartyTicket"></b-form-input>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group label="Rango de Fecha:">
                <b-form-input
                  type="date"
                  v-model="searchDateBegin"
                ></b-form-input>
                <b-form-input
                  type="date"
                  v-model="searchDateEnd"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <!-- Dropdown sections -->
            <b-col>
              <b-form-group>
                <b-dropdown variant="secondary" block text="Causas de Averia">
                  <b-dropdown-form>
                    <b-row align-h="center">
                      <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Causas de Averia:</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <b-form-checkbox-group
                              type="checkbox"
                              v-model="searchCauses"
                              :options="causeList"
                              stacked
                            >
                            </b-form-checkbox-group>
                          </tr>
                        </tbody>
                      </table>
                    </b-row>
                  </b-dropdown-form>
                </b-dropdown>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group>
                <b-dropdown variant="secondary" block text="Tipos de Averias">
                  <b-dropdown-form>
                    <b-row align-h="center">
                      <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Tipos de Averias:</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <b-form-checkbox-group
                              type="checkbox"
                              v-model="searchTypes"
                              :options="outageTypeList"
                              stacked
                            >
                            </b-form-checkbox-group>
                          </tr>
                        </tbody>
                      </table>
                    </b-row>
                  </b-dropdown-form>
                </b-dropdown>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group>
                <b-dropdown variant="secondary" block text="Equipos Impactados">
                  <b-dropdown-form>
                    <b-row align-h="center">
                      <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Equipos Impactados:</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <b-form-checkbox-group
                              type="checkbox"
                              v-model="searchEquipment"
                              :options="equipmentList"
                              stacked
                            >
                            </b-form-checkbox-group>
                          </tr>
                        </tbody>
                      </table>
                    </b-row>
                  </b-dropdown-form>
                </b-dropdown>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <div class="container">
              <b-form-group>
                <h4 class="text-center">Municipios Impactados:</h4>
                <b-form-checkbox-group
                  v-model="searchMunicipalities"
                  :options="municipalityList"
                  stacked
                  small
                  id="municipality-table"
                ></b-form-checkbox-group>
              </b-form-group>
            </div>
          </b-row>
        </b-card>
        <div class="row justify-content-lg-center">
          <div style="center">
            <b-button
              type="submit"
              variant="secondary"
              class="btn-lg btn-block mt-4 mb-2"
              >Filtrar Reportes</b-button
            >
          </div>
        </div>
      </b-form>
    </b-row>
    <b-row>
      <RepList :reportList="filteredReports" />
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
  name: 'Dashboard',
  components: {
    RepList,
  },
  data() {
    return {
      causeOption: [],
      outageTypeOption: [],
      equipmentOption: [],
      searchNOCTicket: '',
      searchThirdPartyTicket: '',
      searchDateBegin: '',
      searchDateEnd: '',
      searchCauses: [],
      searchTypes: [],
      searchEquipment: [],
      searchMunicipalities: [],
    }
  },
  methods: {
    filterReportsByNOCTicket: function (reports) {
      return reports.filter((report) =>
        report.noc_ticket.match(this.searchNOCTicket.toUpperCase())
      )
    },
    filterReportsByThirdPartyTicket: function (reports) {
      return reports.filter((report) =>
        report.third_party_ticket.match(
          this.searchThirdPartyTicket.toUpperCase()
        )
      )
    },
    test() {},
    filterReportsByDateRange: function (reports) {
      if (this.searchDateBegin != '' && this.searchDateEnd != '') {
        return reports.filter((report) => {
          console.log('report date ' + report.date_of_outage)
          console.log('search date starts at: ' + this.searchDateBegin)
          console.log('search date ends at: ' + this.searchDateEnd)
          return (
            report.date_of_outage <= this.searchDateEnd &&
            report.date_of_outage >= this.searchDateBegin
          )
        })
      } else {
        return reports
      }
    },
    filterReportsByOutageCause: function (reports) {
      return reports.filter((report) => {
        return report.causes.includes(this.searchCauses)
      })
    },
    filterReportsByOutageType: function (reports) {
      return reports.filter((report) => {
        return report.outage_type.includes(this.searchTypes)
      })
    },
    filterReportsByMunicipalities: function (reports) {
      return reports.filter((report) => {
        return report.municipalities.includes(this.searchMunicipalities)
      })
    },
    filterReportsByEquipment: function (reports) {
      let newList = []
      for (let index = 0; index < reports.length; index++) {
        let report = reports[index]
        let stringy = Object.keys(report.equipment).toString()
        if (stringy.match(this.searchEquipment)) {
          newList.push(report)
        }
      }
      return newList
    },
  },
  created() {
    this.$store.dispatch('report/fetchReports')
    this.$store.dispatch('report/fetchCauseList')
    this.$store.dispatch('report/fetchOutageTypeList')
    this.$store.dispatch('report/fetchEquipmentList')
    this.$store.dispatch('report/fetchClientTypeList')
  },
  mounted() {},
  computed: {
    causeList() {
      return this.getCauses
    },
    outageTypeList() {
      return this.getOutageTypes
    },
    equipmentList() {
      return this.getEquipments
    },
    municipalityList() {
      return this.getMunicipalities
    },
    filteredReports() {
      return this.filterReportsByMunicipalities(
        this.filterReportsByDateRange(
          this.filterReportsByEquipment(
            this.filterReportsByOutageType(
              this.filterReportsByOutageCause(
                this.filterReportsByNOCTicket(
                  this.filterReportsByThirdPartyTicket(this.reports)
                )
              )
            )
          )
        )
      )
    },
    ...mapState('report', ['reports', 'reportTotal']),
    ...mapGetters('report', [
      'getCauses',
      'getOutageTypes',
      'getEquipments',
      'getClients',
      'getMunicipalities',
    ]),
    ...mapActions('report', ['fetchReports']),
    ...mapState('user', ['userInfo']),
  },
  created() {
    this.$store.dispatch('report/fetchReports')
    this.$store.dispatch('report/fetchCauseList')
    this.$store.dispatch('report/fetchOutageTypeList')
    this.$store.dispatch('report/fetchEquipmentList')
    this.$store.dispatch('report/fetchClientTypeList')
  },
}
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
