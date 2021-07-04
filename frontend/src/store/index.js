import { createStore } from "vuex";

export default createStore({
  state: {
    report:{
      report_type:'',
      noc_ticket:'',
      third_party_ticket:'',
      date_of_outage:'',
      time_of_outage:'',
      notes:'',
      municipalities:'',
      services:[],
      clients:[],
      outage_type:[],
      causes:[],
    },
    isAuthenticated: false,
    toke:'',
    isLoading: false,
  },
  mutations: {},
  actions: {},
  modules: {},
});
