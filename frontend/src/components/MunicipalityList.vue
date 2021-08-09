<template>
  <table class="table is-bordered is-fullwidth overflow-scroll">
    <thead>
      Municipios Impactados:
    </thead>
    <tbody>
      <tr
        v-for="municipality in municipalities.slice().reverse()"
        :key="municipality.id"
      >
        <td>
          <div class="checkbox">
            <label for="{{municipality.id}}">
              <input
                type="checkbox"
                name="map"
                id="{{municipality.id}}"
                value="{{municipality.name}}"
                ref="{{municipality.id}}"
              />{{ municipality.name }}
            </label>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
// import * as am4core from "@amcharts/amcharts4/core";
// import * as am4maps from "@amcharts/amcharts4/maps";
// import am4themes_animated from "@amcharts/amcharts4/themes/animated";
// import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
export default {
  name: "MunicipalityList",
  props: {
    municipalities: Array,
  },
  data() {
    return {
      selectedMunicipalities: [],
    };
  },
};
</script>

<style scoped>
</style>