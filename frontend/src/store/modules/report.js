import APIService from '../../services/APIService.js'
export const namespaced = true
export const state = {
  report: {
    report_type: null,
    noc_ticket: null,
    third_party_ticket: null,
    date_of_outage: null,
    time_of_outage: null,
    notes: null,
    causes: null,
    outage_type: null,
    municipalities: null,
    clients: null,
    equipment: null,
  },
  reports: [],
  equipment: [],
  outage_types: [],
  causes: [],
  clients: [],
  reportTotal: null,
  perPage: 5,
  municipalities: [
    'Adjuntas',
    'Aguada',
    'Aguadilla',
    'Aguas Buenas',
    'Aibonito',
    'Añasco',
    'Arecibo',
    'Arroyo',
    'Barceloneta',
    'Barranquitas',
    'Bayamón',
    'Cabo Rojo',
    'Caguas',
    'Camuy',
    'Canóvanas',
    'Carolina',
    'Cataño',
    'Cayey',
    'Ceiba',
    'Ciales',
    'Cidra',
    'Coamo',
    'Comerío',
    'Corozal',
    'Culebra',
    'Dorado',
    'Fajardo',
    'Florida',
    'Guánica',
    'Guayama',
    'Guayanilla',
    'Guaynabo',
    'Gurabo',
    'Hatillo',
    'Hormigueros',
    'Humacao',
    'Isabela',
    'Jayuya',
    'Juana Díaz',
    'Juncos',
    'Lajas',
    'Lares',
    'Las Marías',
    'Las Piedras',
    'Loíza',
    'Luquillo',
    'Manatí',
    'Maricao',
    'Maunabo',
    'Mayagüez',
    'Moca',
    'Morovis',
    'Naguabo',
    'Naranjito',
    'Orocovis',
    'Patillas',
    'Peñuelas',
    'Ponce',
    'Quebradillas',
    'Rincón',
    'Río Grande',
    'Sabana Grande',
    'Salinas',
    'San Germán',
    'San Juan',
    'San Lorenzo',
    'San Sebastián',
    'Santa Isabel',
    'Toa Alta',
    'Toa Baja',
    'Trujillo Alto',
    'Utuado',
    'Vega Alta',
    'Vega Baja',
    'Vieques',
    'Villalba',
    'Yabucoa',
    'Yauco',
  ],
  comments: [],
}
export const mutations = {
  // Report Mutations
  SET_REPORT(state, report) {
    state.report = report
  },
  SET_REPORTS(state, reports) {
    state.reports = reports
  },
  SET_COMMENTS(state, comments) {
    state.comments = comments
  },
  SET_NEW_COMMENT(state, comment) {
    state.comments.push(comment)
  },
  SET_REPORT(state, report) {
    state.report = report
  },
  SET_EQUIPMENT_LIST(state, equipment) {
    state.equipment = equipment
  },
  SET_OUTAGE_TYPES(state, outage_types) {
    state.outage_types = outage_types
  },
  SET_CAUSES(state, payload) {
    state.causes = payload
  },
  SET_CLIENTS(state, clients) {
    state.clients = clients
  },
  SET_REPORT_TOTAL(state, reportTotal) {
    state.reportTotal = reportTotal
  },
}
export const actions = {
  async createReport({ dispatch, commit }, payload) {
    const res = APIService.createReport(payload)
    if (res) {
      commit('SET_REPORT', payload)
    } else {
      throw new Error('There was an error creating the report: ')
    }
  },
  async updateReport({ dispatch, commit }, payload) {
    return APIService.updateReport(payload)
      .then((response) => {
        console.log('Store actions: ' + response.data)
        commit('SET_REPORT', response.data)
      })
      .catch((error) => {
        const notification = {
          type: 'error',
          message: 'There was a problem updating the report: ' + error.message,
        }
        console.log(error.response)
        dispatch('notification/add', notification, { root: true })
      })
  },
  async fetchReport({ commit, getters }, noc_ticket) {
    let report = getters.getReportById(noc_ticket)

    if (report) {
      commit('SET_REPORT', report)
      return report
    } else {
      return APIService.getReport(noc_ticket)
        .then((response) => {
          commit('SET_REPORT', response.data)
          return response.data
        })
        .catch((error) => {
          const notification = {
            type: 'error',
            message:
              'There was a problem fetching the report: ' + error.message,
          }
        })
    }
  },
  async fetchReportData({ commit, getters }, noc_ticket) {
    let report = getters.getReportById(noc_ticket)

    if (report) {
      commit('SET_REPORT', report)
      return report
    } else {
      return APIService.getReport(noc_ticket)
        .then((response) => {
          commit('SET_REPORT', response.data)
          return response.data
        })
        .catch((error) => {
          const notification = {
            type: 'error',
            message:
              'There was a problem fetching the reports data: ' + error.message,
          }
        })
    }
  },
  async createComment({ commit }, payload) {
    const res = APIService.writeComment(payload)
    if (res) {
      commit('SET_NEW_COMMENT', payload)
    } else {
      throw new Error('There was an error posting the new report.')
    }
  },
  async fetchComments({ commit, getters }) {
    return APIService.getComments()
      .then((response) => {
        console.log('comment action: ' + response.data)
        commit('SET_COMMENTS', response.data)
      })
      .catch((error) => {
        const notification = {
          type: 'error',
          message: 'There was a problem fetching comments: ' + error.message,
        }
        console.log(error.response)
        dispatch('notification/add', notification, { root: true })
      })
  },
  async fetchUpdateReport({ commit, getters, state, dispatch }, noc_ticket) {
    let report = getters.getReportById(noc_ticket)
    if (report) {
      commit('SET_REPORT', report)
      return report
    } else {
      return APIService.getReport(noc_ticket)
        .then((response) => {
          commit('SET_REPORT', response.data)
          return response.data
        })
        .catch((error) => {
          const notification = {
            type: 'error',
            message:
              'There was a problem fetching the report update: ' +
              error.message,
          }
        })
    }
  },
  async fetchReports({ commit, dispatch, state }) {
    return APIService.getReports()
      .then((response) => {
        console.log('The total reports are ' + response.data)
        commit('SET_REPORTS', response.data)
        commit('SET_REPORT_TOTAL', response.headers['x-total-count'])
      })
      .catch((error) => {
        const notification = {
          type: 'error',
          message: 'There was a problem fetching reports: ' + error.message,
        }
        console.log(error.response)
        dispatch('notification/add', notification, { root: true })
      })
  },
  async fetchEquipmentList({ commit, dispatch, state }) {
    const res = await APIService.getEquipmentList()
    if (res) {
      let element = []
      let temp_equipment = res.data
      console.log(res)
      for (let item = 0; item < temp_equipment.length; item++) {
        element.push(temp_equipment[item].equipment)
      }
      commit('SET_EQUIPMENT_LIST', element)
    } else {
      throw new Error('There was an error fetching the equipment list: ')
    }
    // return APIService.apiClient
    //   .getEquipmentList()
    //   .then((response) => {
    //     let element = []
    //     let temp_equipment = response.data
    //     console.log(response)
    //     for (let item = 0; item < temp_equipment.length; item++) {
    //       element.push(temp_equipment[item].equipment)
    //     }
    //     commit('SET_EQUIPMENT_LIST', element)
    //   })
    //   .catch((error) => {
    //     const notification = {
    //       type: 'error',
    //       message:
    //         'There was a problem fetching the equipment list: ' + error.message,
    //     }
    //     dispatch('notification/add', notification, { root: true })
    //   })
  },
  async fetchCauseList({ commit, dispatch }) {
    const res = await APIService.getCauseList()
    if (res) {
      let element = []
      let temp_causes = res.data

      for (let item = 0; item < temp_causes.length; item++) {
        element.push(temp_causes[item].causes)
      }
      commit('SET_CAUSES', element)
    } else {
      throw new Error('Error fetching cause list: ')
    }
    // .then((response) => {
    //     let element = []
    //     let temp_causes = response.data

    //     for (let item = 0; item < temp_causes.length; item++) {
    //       element.push(temp_causes[item].causes)
    //     }
    //     commit('SET_CAUSES', element)
    //   })
    //   .catch((error) => {
    //     const notification = {
    //       type: 'error',
    //       message:
    //         'There was a problem fetching the cause list: ' + error.message,
    //     }
    //     dispatch('notification/add', notification, { root: true })
    //   })
  },
  async fetchOutageTypeList({ commit, dispatch }) {
    const res = await APIService.getOutageTypeList()
    if (res) {
      let element = []
      let temp_outage_types = res.data

      for (let item = 0; item < temp_outage_types.length; item++) {
        element.push(temp_outage_types[item].outage_type)
      }
      commit('SET_OUTAGE_TYPES', element)
    } else {
      throw new Error('There was an error fetching the outage type list: ')
    }
    // .then((response) => {
    //   let element = []
    //   let temp_outage_types = response.data

    //   for (let item = 0; item < temp_outage_types.length; item++) {
    //     element.push(temp_outage_types[item].outage_type)
    //   }
    //   commit('SET_OUTAGE_TYPES', element)
    // })
    // .catch((error) => {
    //   const notification = {
    //     type: 'error',
    //     message:
    //       'There was a problem fetching the outage type list: ' +
    //       error.message,
    //   }
    //   dispatch('notification/add', notification, { root: true })
    // })
  },
  async fetchClientTypeList({ commit, dispatch }) {
    const res = await APIService.getClientList()
    if (res) {
      let element = []
      let temp_client_types = res.data

      for (let item = 0; item < temp_client_types.length; item++) {
        element.push(temp_client_types[item].clients)
      }
      commit('SET_CLIENTS', element)
    } else {
      throw new Error('There was an error fetching client list: ')
    }
  },
}
export const getters = {
  getReportById: (state) => (noc_ticket) => {
    return state.reports.find((report) => report.noc_ticket === noc_ticket)
  },
  getUpdatableReportList: (state) => {
    return state.reports.filter((report) => report.report_type != 'Finalizado')
  },
  getTotalImpactedClients: (state) => {
    return Object.keys(state.report.clients).reduce(
      (sum, values) => sum + parseInt(state.report.clients[values] || 0),
      0
    )
  },
  getReportMunicipalities: (state) => {
    return state.report.municipalities.split(',')
  },
  getComments: (state) => {
    return state.comments
  },
  getCauses: (state) => {
    return state.causes
  },
  getOutageTypes: (state) => {
    return state.outage_types
  },
  getEquipments: (state) => {
    return state.equipment
  },
  getClients: (state) => {
    return state.clients
  },
  getMunicipalities: (state) => {
    return state.municipalities
  },
}
