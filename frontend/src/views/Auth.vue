<template>
  <div>
    <div id="login-bg" class="container">
      <div class="login-form-container bg-light mt-4">
        <div class="container-fluid justify-content-center card">
          <div class="card-body">
            <h1 class="text-center card-title">{{ authCaption }}</h1>
            <div class="row col justify-content-center">
              <!-- <p v-if="incorrectAuth">Incorrect username or password - please try again.</p> -->
              <form v-on:submit.prevent="handleLogin">
                <div class="form-group">
                  <input
                    type="text"
                    name="username"
                    id="user"
                    v-model.trim="username"
                    class="form-control"
                    placeholder="Username"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="password"
                    name="password"
                    id="pass"
                    v-model.trim="password"
                    class="form-control"
                    placeholder="Password"
                  />
                </div>
                <button type="submit" class="btn btn-lg btn-primary btn-block">
                  {{ submitButtonCaption }}
                </button>
                <b-button
                  variant="outline-primary"
                  class="btn btn-lg btn-block"
                  @click="switchAuthMode"
                >
                  {{ switchModeButtonCaption }}
                </b-button>
              </form>
            </div>
            <b-alert
              dismissible
              v-model="formIsValid"
              variant="danger"
              class="mt-4"
            >
              Favor de entrar nombre de usuario y contaseña valida.
            </b-alert>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Auth',
  data() {
    return {
      username: '',
      password: '',
      mode: 'login',
    }
  },
  computed: {
    formIsValid() {
      return false
    },
    submitButtonCaption() {
      if (this.mode === 'login') {
        return 'Ingresar'
      } else {
        return 'Crear Cuenta'
      }
    },
    switchModeButtonCaption() {
      if (this.mode === 'login') {
        return 'Crear cuenta nueva?'
      } else {
        return 'Ingresar a su cuenta?'
      }
    },
    authCaption() {
      if (this.mode === 'login') {
        return 'Ingresar'
      } else {
        return 'Crear Cuenta'
      }
    },
    loggedIn() {
      return this.$store.loggedIn
    },
  },
  methods: {
    submitForm() {
      this.formIsValid = true
      if (this.username === '' || this.password.length < 6) {
        this.formIsValid = false
        return
      }
      // send http request
    },
    async handleLogin() {
      try {
        const payload = {
          username: this.username,
          password: this.password,
        }
        await this.$store.dispatch('user/login', payload)
      } catch (err) {
        console.log('error detected: ' + err)
      }
      this.moveAlong()
    },
    async moveAlong() {
      try {
        console.log(
          'just trying to move alonge: ' + localStorage.getItem('user')
        )
        if (localStorage.getItem('user')) {
          this.$router.push({ name: 'Dashboard' })
        }
      } catch (err) {
        console.log('annoying ass route gurad: ' + err)
      }
    },
    switchAuthMode() {
      if (this.mode === 'login') {
        this.mode = 'signup'
      } else {
        this.mode = 'login'
      }
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/')
    } else {
    }
  },
}
</script>

<style scoped></style>
