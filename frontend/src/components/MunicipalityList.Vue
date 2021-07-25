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
  props: {},
  deta() {
    return {
      selected: this.listOfMunicipalities, //this is an array reference.
    }
  },
  watch:{
      listOfMunicipalities:{
          immediate: true,
          handler(){
              this.changeValueSelection()
          }
      }
  },
  methods:{
      changeValueSelection(){
          this.selected = this.listOfMunicipalities
      }
  },
  props:{
      listOfMunicipalities: Array,
      changeStateOfMunicipality: Function,
  }
};
</script>

<style scoped>
</style>