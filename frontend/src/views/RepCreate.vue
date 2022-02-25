<template>
  <b-container fluid>
    <form v-on:submit.prevent="writeReport">
      <div class="row">
        <!-- Unique Report Data Column -->
        <div class="col mt-3">
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Boleto de NOC</label>
            <div class="col-sm-8">
              <input
                name="label"
                v-model="nocTicket"
                placeholder="E.G: AF0S9E8Q0AD9S0A"
                class="form-control"
                :maxlength="15"
              />
            </div>
          </div>
          <div class="row mb-2 mb-3">
            <label class="col-sm-3 col-form-label">Boleto de Tercero</label>
            <div class="col-sm-8">
              <input
                name="label"
                v-model="thirdPartyTicket"
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
                v-model="date"
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
                v-model="time"
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
                          v-model="causeOption"
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
                          v-model="outageTypeOption"
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
                              value="1000"
                            />1,000+
                            <input
                              type="radio"
                              :name="client"
                              value="5000"
                            />5,000+
                            <input
                              type="radio"
                              :name="client"
                              value="10000"
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
                    v-model="municipalityOption"
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
                    v-model="municipalityOption"
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
          v-model="notes"
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
            >Crear Reporte</b-button
          >
        </div>
      </div>
    </form>
  </b-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import { CheckboxSvgMap } from 'vue-svg-map'
import PuertoRico from '../assets/puerto-rico'
import { getLocationName, getSelectedLocationName } from '../utilities'
export default {
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      reportType: 'Inicial',
      nocTicket: '',
      thirdPartyTicket: '',
      date: null,
      time: null,
      causeOption: [],
      outageTypeOption: [],
      equipmentOption: [],
      clientOption: [],
      municipalityOption: [],
      notes: '',
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
    }
  },
  methods: {
    ...mapActions(['fetchCauseList', 'createReport']),

    writeReport() {
      let reportForm = {
        report_type: this.reportType,
        noc_ticket: this.nocTicket,
        third_party_ticket: this.thirdPartyTicket,
        date_of_outage: this.date,
        time_of_outage: this.time,
        notes: this.notes,
        municipalities: this.municipalityOption.toString(),
        outage_type: this.outageTypeOption.toString(),
        causes: this.causeOption.toString(),
        equipment: this.equipmentObjectString,
        clients: this.clientObjectString,
      }
      this.$store.dispatch('report/createReport', reportForm).then(() => {
        this.$router.push({
          name: 'RepDetail',
          params: { noc_ticket: reportForm.noc_ticket },
        })
      })
    },
    async fetchFields() {
      try {
        this.$store.dispatch('report/fetchCauseList')
        this.$store.dispatch('report/fetchOutageTypeList')
        this.$store.dispatch('report/fetchEquipmentList')
        this.$store.dispatch('report/fetchClientTypeList')
      } catch (err) {
        console.log('there was an error fetching the report form fields ' + err)
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
  },
  computed: {
    ...mapState([('equipment', 'causes', 'outage_type')]),
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
    equipmentObjectString() {
      let equipmentName = this.equipmentOption
      let equipmentAmount = []

      for (let selection = 0; selection < equipmentName.length; selection++) {
        equipmentAmount.push(
          document.getElementById(equipmentName[selection]).value
        )
      }
      let equipmentObject = equipmentName.reduce(
        (acc, key, index) =>
          Object.assign(acc, { [key]: equipmentAmount[index] }),
        {}
      )
      return equipmentObject
    },
    clientObjectString() {
      let clientNames = this.clientOption
      let clientAmount = []

      for (let entry = 0; entry < clientNames.length; entry++) {
        let radioGroupName = document.getElementsByName(clientNames[entry])
        for (let button = 0; button < radioGroupName.length; button++) {
          if (radioGroupName[button].checked) {
            clientAmount.push(radioGroupName[button].value)
          }
        }
      }
      let clientObject = clientNames.reduce(
        (acc, value, index) => ((acc[value] = clientAmount[index]), acc),
        {}
      )
      return clientObject
    },
  },
  mounted() {
    // this.$store.dispatch('report/fetchCauseList')
    // this.$store.dispatch('report/fetchOutageTypeList')
    // this.$store.dispatch('report/fetchEquipmentList')
    // this.$store.dispatch('report/fetchClientTypeList')
    this.fetchFields()
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
<style src="vue-svg-map/dist/index.css"></style>
