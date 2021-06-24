<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-danger">
    <!-- <a class="navbar-brand text-white" href="#">Claro NOC</a> -->
    <router-link :to="{ name: 'Home' }" class="text-white navbar-brand"
      >Claro NOC
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <div class="ml-auto btn-toolbar">
        <ul class="navbar-nav btn-toolbar">
          <li class="nav-item dropdown mr-5">
            <a
              class="nav-link text-white btn-primary btn-lg rounded"
              href="#"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Inicio
            </a>
          </li>
          <li class="nav-item dropdown mr-5">
            <a
              class="
                nav-link
                dropdown-toggle
                text-white
                btn-primary btn-lg
                rounded
              "
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Administrativo
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
          <li class="nav-item dropdown mr-5">
            <a
              class="
                nav-link
                dropdown-toggle
                text-white
                btn-primary btn-lg
                rounded
              "
              href="#"
              id="navbarDropdown"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Cuenta
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
};
</script>

<style scoped>
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}
.navbar-brand:hover {
  color: black !important;
}
</style>
