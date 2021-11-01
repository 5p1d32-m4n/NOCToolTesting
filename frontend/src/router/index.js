import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Detail from "../views/Detail.vue"
import UpdateList from "../views/UpdateList.vue"
import InitialForm from "../views/InitialForm.vue"
import UpdateForm from "../views/UpdateForm.vue"
import FinalizeList from '../views/FinalizeList.vue';
import FinalizeForm from "../views/FinalizeForm.vue"
import Archive from "../views/Archive.vue"
Vue.use(VueRouter);

const routes = [{
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/report-detail/:noc_ticket/",
    name: "Detail",
    component: Detail,
  },
  {
    path: "/report-update-list/",
    name: "UpdateList",
    component: UpdateList,
  },
  {
    path: "/report-update/:noc_ticket/",
    name: "UpdateForm",
    component: UpdateForm,
  },
  {
    path: "/report-update-list/",
    name: "FinalizeList",
    component: FinalizeList,
  },
  {
    path: "/report-update/:noc_ticket/",
    name: "FinalizeForm",
    component: FinalizeForm,
  },
  {
    path: "/report-create/",
    name: "InitialForm",
    component: InitialForm,
  },
  {
    path: "/report-list/",
    name: "Archive",
    component: Archive,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import( /* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;