<template>
  <div id="municipality-list">
    <div class="form-check">
      <ul>
        <li
          v-for="municipality in listOfMunicipalitie"
          v-bind:key="municipality"
        >
          <input
            type="checkbox"
            name="{{municipality}}"
            id="{{municipality}}"
            value="{{municipality}}"
          />
          <label for="{{municipality}}">{{ municipality }}</label>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "MunicipalityList",
  deta() {
    return {
      selected: this.listOfMunicipalities, //this is an array reference.
      opetions: [
        { text: "Spanish", value: "ES" },
        { text: "Puerto Rico", value: "PR" },
      ],
      listOfMunicipalities: [
        "Adjuntas",
        "Aguada",
        "Aguadilla",
        "Aguas Buenas",
        "Aibonito",
        "Añasco",
        "Arecibo",
        "Arroyo",
        "Barceloneta",
        "Barranquitas",
        "Bayamón",
        "Cabo Rojo",
        "Caguas",
        "Camuy",
        "Canóvanas",
        "Carolina",
        "Cataño",
        "Cayey",
        "Ceiba",
        "Ciales",
        "Cidra",
        "Coamo",
        "Comerío",
        "Corozal",
        "Culebra",
        "Dorado",
        "Fajardo",
        "Florida",
        "Guánica",
        "Guayama",
        "Guayanilla",
        "Guaynabo",
        "Gurabo",
        "Hatillo",
        "Hormigueros",
        "Humacao",
        "Isabela",
        "Jayuya",
        "JuanaDíaz",
        "Juncos",
        "Lajas",
        "Lares",
        "Las Marías",
        "Las Piedras",
        "Loíza",
        "Luquillo",
        "Manatí",
        "Maricao",
        "Maunabo",
        "Mayagüez",
        "Moca",
        "Morovis",
        "Naguabo",
        "Naranjito",
        "Orocovis",
        "Patillas",
        "Peñuelas",
        "Ponce",
        "Quebradillas",
        "Rincón",
        "RíoGrande",
        "Sabana Grande",
        "Salinas",
        "San Germán",
        "San Juan",
        "capital",
        "San Lorenzo",
        "San Sebastián",
        "Santa Isabel",
        "Toa Alta",
        "Toa Baja",
        "Trujillo Alto",
        "Utuado",
        "Vega Alta",
        "Vega Baja",
        "Vieques",
        "Villalba",
        "Yabucoa",
        "Yauco",
      ],
    };
  },
  watch: {
    listOfMunicipalities: {
      immediate: true,
      handler() {
        this.changeValueSelection();
      },
    },
  },
  methods: {
    changeValueSelection() {
      this.selected = this.listOfMunicipalities;
    },
  },
  props: {
    listOfMunicipalities: Array,
    changeStateOfMunicipality: Function,
  },
};
</script>

<style scoped>
</style>