<template>
  <b-container fluid>
    <b-row>
      <b-jumbotron
        class="text-center w-100 p-3 h-25 d-inline-block"
        header="Formulario de Actualización"
        header-level="4"
        container-fluid="1"
        align-h="center"
      ></b-jumbotron>
    </b-row>
    <form v-on:submit.prevent="updateReport">
      <div class="row">
        <!-- Unique Report Data Column -->
        <div class="col mt-3">
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Boleto de NOC</label>
            <div class="col-sm-8">
              <input
                name="label"
                disabled
                :value="reportData.noc_ticket"
                placeholder="E.G: AF0S9E8Q0AD9S0A"
                class="form-control"
                :maxlength="15"
              />
            </div>
          </div>
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Boleto de Tercero</label>
            <div
              class="col-sm-8"
              v-if="checkTicket(reportData.third_party_ticket)"
            >
              <input
                name="label"
                disabled
                v-model="reportData.third_party_ticket"
                placeholder="E.G: AF0S9E8Q0A"
                class="form-control"
                :maxlength="10"
              />
            </div>
            <div class="col-sm-8" v-else>
              <input
                name="label"
                v-model="reportData.third_party_ticket"
                placeholder="E.G: AF0S9E8Q0A"
                class="form-control"
                :maxlength="10"
              />
            </div>
          </div>
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Fecha de Averia:</label>
            <div class="col-sm-8">
              <input
                name="label"
                v-model="reportData.date_of_outage"
                placeholder="E.G: AF0S9E8Q0A"
                class="form-control"
                type="date"
              />
            </div>
          </div>
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Tiempo de Averia:</label>
            <div class="col-sm-8">
              <input
                name="label"
                v-model="reportData.time_of_outage"
                placeholder="E.G: AF0S9E8Q0A"
                class="form-control"
                type="time"
              />
            </div>
          </div>
        </div>
        <div class="col">
          <!-- Dropdown select form sections -->
          <b-form-group>
            <!-- Cause Dropdown -->
            <b-dropdown
              variant="danger"
              block
              text="Causa de Averia"
              class="m-2 d-grid mt-3"
              menu-class="w-100"
            >
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
                          v-model="reportData.causes"
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
            <!-- Outage Type Dropdown -->
            <b-dropdown
              variant="danger"
              block
              text="Tipo de Averia"
              class="m-2 d-grid mt-3"
              menu-class="w-100"
            >
              <b-dropdown-form>
                <b-row align-h="center">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col">Tipos de Averia:</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <b-form-checkbox-group
                          v-model="reportData.outage_type"
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
            <!-- Equipment Dropdown -->
            <b-dropdown
              variant="danger"
              block
              text="Equipos Impactados"
              class="m-2 d-grid mt-3"
              menu-class="w-100"
            >
              <b-dropdown-form>
                <b-row align-h="center">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col">Equipo</th>
                        <th scope="col">Cantidad Impactda</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr
                        v-for="(equipment, index) in equipmentList"
                        :key="index"
                      >
                        <td>
                          <b-form-checkbox
                            v-model="equipmentOption"
                            :value="equipment"
                            stacked
                            >{{ equipment }}</b-form-checkbox
                          >
                        </td>
                        <td>
                          <!-- Original number input for client amount -->
                          <div>
                            <input
                              type="number"
                              name="amountSlots"
                              v-model="equipmentCount[index]"
                              value="0"
                              required
                              min="0"
                              :id="equipment"
                            />
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </b-row>
              </b-dropdown-form>
            </b-dropdown>
            <!-- Client Dropdown -->
            <b-dropdown
              variant="danger"
              block
              text="Clientes Impactados"
              class="m-2 d-grid mt-3"
              menu-class="w-100"
            >
              <b-dropdown-form>
                <b-row align-h="center">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col">Tipo de Cliente:</th>
                        <th scope="col">Cantidad Impactada:</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(client, index) in clientList" :key="index">
                        <!-- Checkbox -->
                        <td>
                          <div>
                            <b-form-checkbox
                              v-model="clientOption"
                              :value="client"
                              stacked
                              >{{ client }}</b-form-checkbox
                            >
                          </div>
                        </td>
                        <!-- Number input. -->
                        <td>
                          <div>
                            <input
                              type="radio"
                              :name="client"
                              v-model="clientCount[index]"
                              :value="1000"
                            />1,000+
                            <input
                              type="radio"
                              :name="client"
                              v-model="clientCount[index]"
                              :value="5000"
                            />5,000+
                            <input
                              type="radio"
                              :name="client"
                              v-model="clientCount[index]"
                              :value="10000"
                            />10,000+
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </b-row>
              </b-dropdown-form>
            </b-dropdown>
          </b-form-group>
          <!-- <RepBaseSelect :modelValue="report.equipment" label="Tipo" /> -->
        </div>
      </div>
      <div class="row">
        <div class="col">
          <b-container fluid>
            <hr />
            <!-- Title Row. -->
            <b-row align-h="center">
              <h4>Municipios Impactados:</h4>
            </b-row>
            <!-- Municipality Row -->
            <b-row>
              <!-- Beginning of Municipality Checkbox. -->
              <b-col>
                <div class="overflow-auto" id="municipality-table">
                  <b-form-checkbox-group
                    v-model="reportData.municipalities"
                    :options="municipalityList"
                    stacked
                    bordered
                  ></b-form-checkbox-group>
                </div>
              </b-col>
              <!-- Beginning of Municipality CheckboxEnd. -->

              <!-- Beggingin of SVG Map. -->
              <b-col>
                <div>
                  <CheckboxSvgMap
                    v-model="reportData.municipalities"
                    :map="PuertoRico"
                    @mouseover="pointLocation"
                    @mouseout="unpointLocation"
                    @focus="focusLocation"
                    @blur="blurLocation"
                  />
                  <div>
                    <h3 class="b-tooltip tool">
                      Municipio Apuntado: {{ pointedLocation }}
                    </h3>
                  </div>
                </div>
              </b-col>
              <!-- Portion SVG Map End. -->
            </b-row>

            <!-- Submit Button row -->
          </b-container>
        </div>
      </div>
      <div class="row justify-content-lg-center mt-5">
        <h3>Notas de Avería:</h3>
        <b-form-textarea
          label="Notas de Averia"
          type="text"
          v-model="reportData.notes"
          class="form-control w-50 p-3"
          id="notes"
          :maxlength="500"
        >
        </b-form-textarea>
      </div>
      <div class="row justify-content-lg-center">
        <div style="center">
          <b-button
            type="submit"
            variant="danger"
            class="btn-lg btn-block mt-4 mb-2"
            >Actualizar Reporte</b-button
          >
        </div>
      </div>
    </form>
  </b-container>
</template>

<script>
import { CheckboxSvgMap } from 'vue-svg-map'
import PuertoRico from '../assets/puerto-rico'
import { getLocationName, getSelectedLocationName } from '../utilities'
import { mapActions, mapGetters, mapState } from 'vuex'
import APIService from '../services/APIService'
export default {
  props: ['noc_ticket'],
  name: 'RepUpdate',
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      causeOption: [],
      outageTypeOption: [],
      equipmentOption: [],
      equipmentCount: [],
      clientOption: [],
      clientCount: [],
      municipalityOption: [],
      notes: '',
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
      reportData: {
        report_type: '',
        noc_ticket: '',
        third_party_ticket: '',
        date_of_outage: '',
        time_of_outage: '',
        notes: '',
        causes: [],
        outage_type: [],
        municipalities: [],
        clients: {},
        equipment: {},
      },
      // equipmentList: [],
      newEquipmentObject: {},
      newClientObject: {},
    }
  },
  computed: {
    ...mapState(['report', 'equipment']),
    ...mapGetters('report', [
      'getCauses',
      'getOutageTypes',
      'getEquipments',
      'getClients',
      'getMunicipalities',
    ]),
    causeList() {
      return this.getCauses
    },
    outageTypeList() {
      return this.getOutageTypes
    },
    equipmentList() {
      return this.getEquipments
    },
    clientList() {
      return this.getClients
    },
    municipalityList() {
      return this.getMunicipalities
    },
    computedEquipmentOption() {
      return Array(Object.keys(JSON.parse(this.reportData.equipment)))
    },
  },
  methods: {
    ...mapActions('report', [
      'fetchReportData',
      'fetchEquipmentList',
      'fetchCauseList',
      'fetchOutageTypeList',
      'fetchClientTypeList',
    ]),
    formLoader() {
      this.reportData.report_type = 'Actualización'
      this.reportData.noc_ticket = this.report.report.noc_ticket
      this.reportData.third_party_ticket = this.report.report.third_party_ticket
      this.reportData.date_of_outage = this.report.report.date_of_outage
      this.reportData.time_of_outage = this.report.report.time_of_outage
      this.reportData.notes = this.report.report.notes
      this.reportData.causes = Array(this.report.report.causes)
      this.reportData.outage_type = Array(this.report.report.outage_type)
      this.reportData.municipalities =
        this.report.report.municipalities.split(',')
      this.reportData.equipment = this.report.report.equipment
      this.equipmentOption = Object.keys(this.reportData.equipment)
      this.reportData.clients = this.report.report.clients
      this.clientOption = Object.keys(this.reportData.clients)
      let equipmentAmount = []
      let reportedEquipmentCount = Object.values(this.reportData.equipment)
      for (let index = 0; index < this.equipmentList.length; index++) {
        equipmentAmount.push(0)
      }

      for (let index = 0; index < this.equipmentList.length; index++) {
        let currentEquipment = this.equipmentList[index]

        for (
          let subIndex = 0;
          subIndex < this.equipmentOption.length;
          subIndex++
        ) {
          let reportEquipment = this.equipmentOption[subIndex]

          if (currentEquipment == reportEquipment) {
            equipmentAmount[index] = reportedEquipmentCount[subIndex]
          }
        }
      }
      this.equipmentCount = equipmentAmount
      // Client Radio setter section
      let clientAmount = []
      let reportedClientCount = Object.values(this.reportData.clients)
      for (let index = 0; index < this.clientList.length; index++) {
        clientAmount.push(0)
      }
      for (let index = 0; index < this.clientList.length; index++) {
        let currentClient = this.clientList[index]

        for (
          let subIndex = 0;
          subIndex < this.clientOption.length;
          subIndex++
        ) {
          let reportClient = this.clientOption[subIndex]

          if (currentClient == reportClient) {
            clientAmount[index] = reportedClientCount[subIndex]
          }
        }
      }
      this.clientCount = clientAmount
    },
    buildReportObjects() {
      // Equipment Object building process.
      let equipmentName = this.equipmentOption
      let equipmentAmount = []

      for (let index = 0; index < equipmentName.length; index++) {
        equipmentAmount.push(
          document.getElementById(equipmentName[index]).value
        )
      }
      let newEquipmentObject = equipmentName.reduce(
        (acc, key, index) =>
          Object.assign(acc, { [key]: equipmentAmount[index] }),
        {}
      )
      this.newEquipmentObject = newEquipmentObject
      // Client Object building process

      let clientName = this.clientOption
      let clientAmount = []

      for (let index = 0; index < clientName.length; index++) {
        let radioGroupName = document.getElementsByName(clientName[index])

        for (let button = 0; button < radioGroupName.length; button++) {
          if (radioGroupName[button].checked == true) {
            clientAmount.push(radioGroupName[button].value)
          }
        }
      }

      let newClientObject = clientName.reduce(
        (acc, value, index) => ((acc[value] = clientAmount[index]), acc),
        {}
      )

      this.newClientObject = newClientObject
      console.log('new client object is: ' + this.newClientObject)
    },
    updateReport() {
      this.buildReportObjects()
      this.reportData.clients = this.newClientObject
      this.reportData.equipment = this.newEquipmentObject
      let tempReport = {
        report_type: this.reportData.report_type,
        noc_ticket: this.reportData.noc_ticket,
        third_party_ticket: this.reportData.third_party_ticket,
        date_of_outage: this.reportData.date_of_outage,
        time_of_outage: this.reportData.time_of_outage,
        notes: this.reportData.notes,
        municipalities: this.reportData.municipalities.toString(),
        outage_type: this.reportData.outage_type.toString(),
        causes: this.reportData.causes.toString(),
        equipment: this.reportData.equipment,
        clients: this.reportData.clients,
      }
      this.$store.dispatch('report/updateReport', tempReport)
      setTimeout(5000)
      this.$router.push({
        name: 'RepDetail',
        params: { noc_ticket: tempReport.noc_ticket },
      })
    },
    checkTicket(parameter) {
      if (parameter == null || parameter == '') {
        return false
      } else {
        return true
      }
    },
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target)
    },
    unpointLocation() {
      this.pointedLocation = null
    },
    focusLocation(event) {
      this.focusedLocation = getLocationName(event.target)
    },
    blurLocation() {
      this.focusedLocation = null
    },
    makeLists() {
      this.equipmentOption = this.equipmentList
    },
    getSelectedLocationName,
  },
  watch: {
    equipmentList(newValue) {},
    clientList(newValue) {},
  },
  created() {
    this.$store.dispatch('report/fetchCauseList')
    this.$store.dispatch('report/fetchOutageTypeList')
    this.$store.dispatch('report/fetchEquipmentList')
    this.$store.dispatch('report/fetchClientTypeList')
    this.fetchReportData(this.noc_ticket)
    this.makeLists()
    setTimeout(this.formLoader, 1000)
  },
  mounted() {},
}
</script>

<style>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
<style src="vue-svg-map/dist/index.css"></style>
