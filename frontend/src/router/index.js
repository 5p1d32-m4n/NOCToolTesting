import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Detail from "../views/Detail.vue"
import UpdateList from "../views/UpdateList.vue"
import InitialForm from "../views/InitialForm.vue"
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
    path: "/report-create/",
    name: "InitialForm",
    component: InitialForm,
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