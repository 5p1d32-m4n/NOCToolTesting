import APIService from '../../services/APIService.js'
import axios from 'axios'
const cleanClient = axios.create({
  // baseURL: 'http://localhost:8000/api/',
  baseURL:
    // 'https://8000-5p1d32m4n-noctoolv1-bcvppwjcvrc.ws-us32.gitpod.io/api/',
    'http://127.0.0.1:8000/api/',
  headers: {
    'Content-type': 'application/json',
    xhrFields: {
      withCredentials: true,
    },
  },
})
const user = localStorage.getItem('user')
const initialState = user
export const namespaced = true
export const state = {
  user: {
    id: 0,
    password: '',
    last_login: '',
    is_superuser: { type: Boolean, default: false },
    is_staff: { type: Boolean, default: false },
    is_active: { type: Boolean, default: false },
    date_joined: '',
    username: '',
    employee_number: 0,
    email: '',
    department: '',
    first_name: '',
    last_name: '',
    groups: [],
    user_permissions: [],
  },
  access: localStorage.getItem('access') || '',
  refresh: localStorage.getItem('refresh') || '',
  key: localStorage.getItem('key') || '',
  initialState,
  isAuthenticated: false,
  loggedIn: user ? true : false,
}
export const mutations = {
  SET_USER(
    state,
    {
      id,
      password,
      last_login,
      is_superuser,
      is_staff,
      is_active,
      date_joined,
      username,
      employee_number,
      email,
      department,
      first_name,
      last_name,
      groups,
      user_permissions,
    }
  ) {
    state.user.id = id
    state.user.password = password
    state.user.last_login = last_login
    state.user.is_superuser = is_superuser
    state.user.is_staff = is_staff
    state.user.is_active = is_active
    state.user.date_joined = date_joined
    state.user.username = username
    state.user.employee_number = employee_number
    state.user.email = email
    state.user.department = department
    state.user.first_name = first_name
    state.user.last_name = last_name
    state.user.groups = groups
    state.user.user_permissions = user_permissions
    state.isAuthenticated = true
  },
  SET_AUTHENTICATED(state, auth) {
    state.isAuthenticated = auth
  },
  CLEAR_USER_DATA() {
    localStorage.removeItem('user')
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    location.reload()
  },
  SET_ACCESS_TOKEN(state, access) {
    state.access = access
    localStorage.setItem('access', access)
  },
  SET_REFRESH_TOKEN(state, refresh) {
    state.refresh = refresh
    localStorage.setItem('refresh', refresh)
  },
  LOGINSUCCESS(state, user) {
    state.status.loggedIn = true
    state.user = user
  },
  LOGINFAILURE(state, user) {
    state.loggedIn = false
    state.user = null
  },
  SET_KEY(state, key) {
    state.key = key
  },
}
export const actions = {
  async login({ commit }, { username, password }) {
    // Token Pair Obtain response
    const tokenRes = await APIService.apiClient.post('/auth/token/obtain/', {
      username,
      password,
    })
    if (tokenRes) {
      commit('SET_ACCESS_TOKEN', tokenRes.data.access)
      localStorage.setItem('access', tokenRes.data.access)
      console.log(
        'access token set in state and checking local storage: ' +
          localStorage.getItem('access')
      )
      commit('SET_REFRESH_TOKEN', tokenRes.data.refresh)
      localStorage.setItem('refresh', tokenRes.data.refresh)
      console.log(
        'refresh token set in state and checking local storage: ' +
          localStorage.getItem('refresh')
      )
    } else {
      throw new Error('Access and refresh tokens could not be set!')
    }
    // Auth login key response
    const loginRes = await cleanClient.post('auth/login/', {
      username,
      password,
    })
    if (loginRes) {
      commit('SET_KEY', loginRes.data.key)
    } else {
      throw new Error('User key auth failed!')
    }
    // Fetch user data response
    const newBase = {
      baseURL: 'http://127.0.0.1:8000/api/',
      headers: {
        Authorization: `JWT ${localStorage.getItem('access')}`,
        'Content-Type': 'application/json',
      },
    }
    const newAxios = axios.create(newBase)
    const userRes = await newAxios.get('/auth/user/')
    console.log('auth/user/ response: ' + JSON.stringify(userRes))
    if (userRes) {
      console.log('ok, how to I handle this ?' + userRes.data.id)
      commit('SET_USER', {
        id: userRes.data.id,
        password: userRes.data.password,
        last_login: userRes.data.last_login,
        is_superuser: userRes.data.is_superuser,
        is_staff: userRes.data.is_staff,
        is_active: userRes.data.is_active,
        date_joined: userRes.data.date_joined,
        username: userRes.data.username,
        employee_number: userRes.data.employee_number,
        email: userRes.data.email,
        department: userRes.data.department,
        first_name: userRes.data.first_name,
        last_name: userRes.data.last_name,
        groups: userRes.data.groups,
        user_permissions: userRes.data.user_permissions,
      })
      localStorage.setItem('user', JSON.stringify(userRes.data))
    } else {
      throw new Error('There was an error fethching user data from the API!')
    }
  },
  register(context, payload) {},
}
export const getters = {
  getUserID(state) {
    return state.userInfo.id
  },
  getUserName(state) {
    return state.user.username
  },
  getFullName(state) {
    return `${state.first_name} ${state.last_name}`
  },
  getToken(state) {
    return state.token
  },
  getRefreshToken(state) {
    return state.refresh
  },
  loggedIn(state) {
    return state.isAuthenticated
  },
}
