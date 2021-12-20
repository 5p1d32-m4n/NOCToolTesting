<template>
  <div>
    <div id="login-bg" class="container">
      <div class="login-form-container bg-light">
        <div class="container-fluid justify-content-center card">
          <div class="card-body">
            <h1 class="text-center card-title">Login</h1>
            <div class="row col justify-content-center">
              <p v-if="incorrectAuth">Incorrect username or password - please try again.</p>
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
      incorrectAuth: false,
    };
  },
  methods: {
    login() {
      axios.defaults.headers.common['Authorization'] =''
      localStorage.removeItem("access")

      const formData = {
        username : this.username,
        password : this.password
      }

      axios
      .post('/api/v1/jwt/create/', formData)
      .then(response => {
        console.log(response)

        const accessToken = response.data.accessToken
        const refreshToken = response.data.refreshToken
        this.$store.commit('setAccessToken', accessToken)
        this.$store.commit('setRefreshToken', refreshToken)
        axios.defaults.headers.common['Authorization'] = 'JWT' + accessToken
        localStorage.setItem("accessToken", accessToken)
        localStorage.setItem("refreshToken", refreshToken)
        this.$router.push('/')
      })
      .catch(error => {
        console.log(error)
      })
    },
  },
};
</script>

<style scoped>
</style>