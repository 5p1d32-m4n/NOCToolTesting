import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Detail from "../views/Detail.vue";
import ListUpdate from '../views/ListUpdate.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/report-detail/:noc_ticket/",
    name: "detail",
    component: Detail,
    props: true,
  },
  {
    path: "/report-update-list/",
    name: "listUpdate",
    component: ListUpdate,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  base: '/',
  routes,
});

export default router;
