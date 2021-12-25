import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";
import Home from "../views/Home.vue";
import Detail from "../views/Detail.vue";
import UpdateList from "../views/UpdateList.vue";
import InitialForm from "../views/InitialForm.vue";
import UpdateForm from "../views/UpdateForm.vue";
import FinalizeList from "../views/FinalizeList.vue";
import FinalizeForm from "../views/FinalizeForm.vue";
import Archive from "../views/Archive.vue";
import EmailList from "../views/EmailList.vue";
import EmailNotificationForm from "../views/EmailNotificationForm.vue";
import LogIn from "../views/LogIn.vue";
import LogOut from "../views/LogOut.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/email-list",
    name: "EmailList",
    component: EmailList,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/email-notification",
    name: "EmailNotificationForm",
    component: EmailNotificationForm,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-detail/:noc_ticket",
    name: "Detail",
    component: Detail,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-update-list",
    name: "UpdateList",
    component: UpdateList,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-update/:noc_ticket",
    name: "UpdateForm",
    component: UpdateForm,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-update-list",
    name: "FinalizeList",
    component: FinalizeList,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-update/:noc_ticket",
    name: "FinalizeForm",
    component: FinalizeForm,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-create",
    name: "InitialForm",
    component: InitialForm,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/report-list",
    name: "Archive",
    component: Archive,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/login",
    name: "LogIn",
    component: LogIn,
    callback: false,
    home: false,
  },
  {
    path: "/logout",
    name: "LogOut",
    component: LogOut,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      return next();
    }
    next("/login");
  } else {
    next();
  }
});

// router.safeNavigate = function(route, dest){
//   if (route.name !=dest) this.push({name:dest});
// }

export default router;
