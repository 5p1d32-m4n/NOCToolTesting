<template>
  <div>
    <div id="login-bg" class="container">
      <div class="login-form-container bg-light">
        <div class="container-fluid justify-content-center card">
          <div class="card-body">
            <h1 class="text-center card-title">Login</h1>
            <div class="row col justify-content-center">
              <!-- <p v-if="incorrectAuth">Incorrect username or password - please try again.</p> -->
              <form v-on:submit.prevent="login">
                <div class="form-group">
                  <input
                    type="text"
                    name="username"
                    id="user"
                    v-model="username"
                    class="form-control"
                    placeholder="Username"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="password"
                    name="password"
                    id="pass"
                    v-model="password"
                    class="form-control"
                    placeholder="Password"
                  />
                </div>
                <button type="submit" class="btn btn-lg btn-primary btn-block">
                  Login
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      const payload = {
        username: this.username,
        password: this.password,
      }

      axios
        .post(this.$store.state.endpoints.accessToken, payload)
        .then((response)=>{
          this.$store.commit('updateToken', response.data.access)

          // get and set the authUser.
          const base = {
            baseUrl: this.$store.state.endpoints.baseUrl,
            headers:{
              /**
               * This is where we set our @Authorization to @JWT
               */
              Authorization: `JWT ${this.$store.state.access}`,
              'Content-Type': 'application/json'
            },
            xhrFields:{
              withCredentials: true,
            },
          }

          /**
           * Even though the authentication returned a user object that can be
            decoded, we fetch it again. This way we aren't super dependant on
            JWT and can plug in something else.
          */
         const axiosInstance = axios.create(base)
         axiosInstance({
           url:'/api/v1/users/me/',
           method: 'get',
           params:{},
         }).then((response)=>{
           this.$store.commit('SET_AUTH_USER',{
             authUser: response.data,
             isAuthenticated: true
           })
           this.$router.push({name: 'Home'})
         }).catch((error)=>{
           console.log(error)
         })
        })
    },
  },
};
</script>

<style scoped>
</style>