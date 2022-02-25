import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import RepArchive from '../views/RepArchive.vue'
import RepCreate from '../views/RepCreate.vue'
import RepUpdate from '../views/RepUpdate.vue'
import RepUpdateList from '../views/RepUpdateList.vue'
import RepFinalize from '../views/RepFinalize.vue'
import RepFinalizeList from '../views/RepFinalizeList.vue'
import NotFound from '../views/NotFound.vue'
import RepDetail from '../views/RepDetail.vue'
import Auth from '../views/Auth.vue'
import NetworkIssue from '../views/NetworkIssue'

import NProgress from 'nprogress'
import store from '../store'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
  {
    path: '/report-create',
    name: 'RepCreate',
    component: RepCreate,
    meta: { requiresAuth: true },
  },
  {
    path: '/report-archive',
    name: 'RepArchive',
    component: RepArchive,
    meta: { requiresAuth: true },
  },
  {
    path: '/report-detail/:noc_ticket',
    name: 'RepDetail',
    component: RepDetail,
    props: true,
    beforeEnter(routeTo, routeFrom, next) {
      store
        .dispatch('report/fetchReport', routeTo.params.noc_ticket)
        .then((report) => {
          routeTo.params.report = report
          next()
        })
        .catch((error) => {
          if (error.response && error.response.status == 404) {
            next({ name: '404', params: { resource: 'reporte' } })
          } else {
            next({ name: 'NetworkIssue' })
          }
        })
    },
    meta: { requiresAuth: true },
  },
  {
    path: '/report-update/:noc_ticket',
    name: 'RepUpdate',
    component: RepUpdate,
    props: true,
    beforeEnter(routeTo, routeFrom, next) {
      store
        .dispatch('report/fetchReport', routeTo.params.noc_ticket)
        .then((report) => {
          routeTo.params.report = report
          next()
        })
        .catch((error) => {
          if (error.response && error.response.status == 404) {
            next({ name: '404', params: { resource: 'reporte' } })
          } else {
            next({ name: 'NetworkIssue' })
          }
        })
    },
    meta: { requiresAuth: true },
  },
  {
    path: '/report-finalize-list/',
    name: 'RepFinalizeList',
    component: RepFinalizeList,
    meta: { requiresAuth: true },
  },
  {
    path: '/report-finalize/:noc_ticket',
    name: 'RepFinalize',
    component: RepFinalize,
    props: true,
    beforeEnter(routeTo, routeFrom, next) {
      store
        .dispatch('report/fetchReport', routeTo.params.noc_ticket)
        .then((report) => {
          routeTo.params.report = report
          next()
        })
        .catch((error) => {
          if (error.response && error.response.status == 404) {
            next({ name: '404', params: { resource: 'reporte' } })
          } else {
            next({ name: 'NetworkIssue' })
          }
        })
    },
    meta: { requiresAuth: true },
  },
  {
    path: '/report-update-list/',
    name: 'RepUpdateList',
    component: RepUpdateList,
    meta: { requiresAuth: true },
  },
  // This is meant to be the 404 not found component.
  {
    path: '*',
    component: NotFound,
    redirect: { name: '404', params: { resource: 'page' } },
  },
  {
    path: '/404',
    name: '404',
    component: NotFound,
    props: true,
  },
  {
    path: '/network-issue',
    name: 'NetworkIssue',
    component: NetworkIssue,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((routeTo, routeFrom, next) => {
  NProgress.start()
  const loggedIn = localStorage.getItem('user')

  if (routeTo.matched.some((record) => record.meta.requiresAuth)) {
    console.log('route guard isAuth: ' + loggedIn)
    if (loggedIn) {
      next()
    } else {
      next('/auth')
    }
  }
  next()
})
router.afterEach(() => {
  NProgress.done()
})

export default router
