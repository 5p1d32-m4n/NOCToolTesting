import axios from 'axios'
import NProgress from 'nprogress'

// let csrf_token = Cookies.get('csrftoken')
// axios.defaults.xsrfHeaderName = 'csrftoken'
// axios.defaults.xsrfCookieName = 'X-CSRFToken'
// axios.defaults.withCredentials = true
const apiClient = axios.create({
  // baseURL: 'http://localhost:8000/api/',
  baseURL:
    // 'https://8000-5p1d32m4n-noctoolv1-bcvppwjcvrc.ws-us32.gitpod.io/api/',
    'http://127.0.0.1:8000/api/',
  headers: {
    'Content-type': 'application/json',
    Authorization: `JWT ${localStorage.getItem('access')}`,
    xhrFields: {
      withCredentials: false,
    },
  },
})

apiClient.interceptors.request.use((config) => {
  NProgress.start()
  return config
})

apiClient.interceptors.response.use((response) => {
  NProgress.done()

  return response
})

export default {
  apiClient,
  getReports() {
    return apiClient.get('/report-list/')
  },
  getComments() {
    return apiClient.get('/comment-list/')
  },
  createReport(payload) {
    return apiClient.post('/report-create/', payload)
  },
  writeComment(payload) {
    return apiClient
      .post('/comment-create/', payload)
      .then((response) => {
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error.response)
      })
  },
  logout() {
    localStorage.removeItem('user')
  },
  updateReport(payload) {
    return apiClient.put(`/report-update/${payload.noc_ticket}/`, payload)
  },
  getReport(noc_ticket) {
    return apiClient.get('/report-detail/' + noc_ticket)
  },
  getEquipmentList() {
    return apiClient.get('/equipment-list/')
  },
  getOutageTypeList() {
    return apiClient.get('/outage_type-list/')
  },
  getCauseList() {
    return apiClient.get('/cause-list/')
  },
  getClientList() {
    return apiClient.get('/clients-list/')
  },
}
