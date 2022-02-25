<template>
  <b-container fluid="1">
    <div>
      <b-jumbotron>
        <template #header>
          Data de Reporte: {{ report.report.noc_ticket }}
        </template>
      </b-jumbotron>
      <div class="container-fluid">
        <b-row>
          <b-col>
            <b-table-simple hover bordered>
              <b-tbody>
                <b-tr>
                  <b-th> Boleto del NOC: </b-th>
                  <b-td>{{ report.report.noc_ticket }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Boleto de Tercero:</b-th>
                  <b-td>{{ report.report.third_party_ticket }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Fecha de Averia: </b-th>
                  <b-td>{{ report.report.date_of_outage }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Tiempo de Averia: </b-th>
                  <b-td>{{ report.report.time_of_outage }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Municipios Impactados: </b-th>
                  <b-td>{{ report.report.municipalities }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Clientes Impactados: </b-th>
                  <b-td v-if="report.report.clients">
                    <p
                      v-for="(value, client) in report.report.clients"
                      :key="client"
                    >
                      {{ client }}: {{ value }}
                    </p>
                    <p><strong>Total:</strong> {{ getTotalImpactedClients }}</p>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-th>Tipo de Averia: </b-th>
                  <b-td>{{ report.report.outage_type }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Causas de Averia: </b-th>
                  <b-td>{{ report.report.causes }}</b-td>
                </b-tr>
                <b-tr>
                  <b-th>Equipos Impactados: </b-th>
                  <b-td v-if="report.report.equipment">
                    <p
                      v-for="(value, equipment) in report.report.equipment"
                      :key="equipment"
                    >
                      {{ equipment }}: {{ value }}
                    </p>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </b-col>
          <b-col>
            <!-- PR map goes here -->
            <h2>Mapa de Municipios Impactados:</h2>
            <!-- map plugin -->
            <CheckboxSvgMap
              :map="PuertoRico"
              v-model="getReportMunicipalities"
            />
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <b-alert
              show
              variant="danger"
              border-variant="transparent"
              text-variant="light"
            >
              <h1>Notas de Averia:</h1>
              <hr class="my-4" />
              <p>{{ report.report.notes }}</p>
            </b-alert>
          </b-col>
        </b-row>
        <hr class="my-4" />
        <b-row>
          <!-- Comment Section -->
          <b-col>
            <b-col>
              <b-row>
                <h1 class="ml-4">Añadir Un Comentario</h1>
              </b-row>
              <b-row class="m-2">
                <b-card class="w-100">
                  <b-form-group>
                    <b-form v-on:submit.prevent="test">
                      <b-form-input
                        type="text"
                        v-model="commentFormContent"
                      ></b-form-input>
                      <b-button class="mt-2" variant="danger" type="submit"
                        >Añadir</b-button
                      >
                    </b-form>
                  </b-form-group>
                </b-card>
              </b-row>
            </b-col>
            <b-col>
              <b-row>
                <h1 class="ml-4">Comentarios de Usuarios:</h1>
              </b-row>
              <b-list-group
                v-for="comment in commentList"
                :key="comment.id"
                class="mb-4"
              >
                <b-list-group-item
                  v-if="comment.report == report.report.noc_ticket"
                >
                  <b-card :header="comment.author" :footer="comment.published">
                    <b-card-text>
                      {{ comment.content }}
                    </b-card-text>
                  </b-card>
                </b-list-group-item>
              </b-list-group>
            </b-col>
          </b-col>
        </b-row>
      </div>
    </div>
  </b-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import APIService from '../services/APIService.js'
import { CheckboxSvgMap } from 'vue-svg-map'
import PuertoRico from '../assets/puerto-rico'
import { getLocationName, getSelectedLocationName } from '../utilities'
import NProgress from 'nprogress'
import store from '@/store/index.js'
export default {
  props: ['noc_ticket'],
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
      commentFormContent: '',
      commentFormReport: '',
      commentFormUserID: null,
    }
  },
  methods: {
    ...mapActions('report', ['fetchReport', 'fetchComments']),
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target)
    },
    filterComments: function (commentList, report) {
      return commentList.filter((comment) => {
        comment.report.match(report.noc_ticket)
      })
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
    async test() {
      try {
        let commentPayload = {
          content: this.commentFormContent,
          report: this.report.report.noc_ticket,
          author: this.userName,
        }
        console.log('comment payload:' + JSON.stringify(commentPayload))
        this.$store.dispatch('report/createComment', commentPayload)
      } catch (err) {
        console.log('there was a commenting error.')
      }
    },
    getSelectedLocationName,
  },
  computed: {
    ...mapState(['report']),
    ...mapGetters('report', [
      'getTotalImpactedClients',
      'getReportMunicipalities',
      'getComments',
    ]),
    ...mapGetters('user', ['getUserName']),
    ...mapState(['user']),
    commentList() {
      return this.getComments
    },
    filteredCommentList() {
      return this.filterComments(this.commentList, this.report.report)
    },
    userName() {
      return this.getUserName
    },
  },
  beforeRouteEnter(routeTo, routeFrom, next) {
    NProgress.start()
    store.dispatch('report/fetchReport', routeTo.params.noc_ticket).then(() => {
      NProgress.done()
      next()
    })
  },

  created() {
    this.fetchReport(this.noc_ticket)
    this.fetchComments()
  },

  mounted() {
    // this.filterComments(this.commentList, this.report.report)
    console.log(
      'this is the mounted report object: ' + JSON.stringify(this.report.report)
    )
  },
}
</script>

<style lang="scss" scoped></style>
