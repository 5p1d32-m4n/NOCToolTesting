<template>
  <div class="municipality">
    <div class="checkbox">
      <label for="{{municipality}}">
        <input
          type="checkbox"
          name="map"
          id="{{municipality.id}}"
          value="{{municipality.name}}"
          v-if="municipality"
        />{{ municipality.name }}
      </label>
    </div>
  </div>
</template>

<script>
// import * as am4core from "@amcharts/amcharts4/core";
// import * as am4maps from "@amcharts/amcharts4/maps";
// import am4themes_animated from "@amcharts/amcharts4/themes/animated";
// import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
export default {
  name: "MunicipalityList",
  props: {
    municipality: Object,
  },
};
</script>

<style scoped>
</style>