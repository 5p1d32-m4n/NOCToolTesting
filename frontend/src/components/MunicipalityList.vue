<template>
  <div class="overflow-auto" id="municipality-table">
    <table class="table table-hover table-striped table-bordered">
      <tbody>
        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-YU"
                  id="PR-AJ"
                  value="Adjuntas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Adjuntas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-YB"
                  id="PR-AD"
                  value="Aguada"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguada</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-VL"
                  id="PR-AL"
                  value="Aguadilla"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguadilla</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-VQ"
                  id="PR-AB"
                  value="Aguas Buenas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguas Buenas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-VB"
                  id="PR-AI"
                  value="Aibonito"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aibonito</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-VA"
                  id="PR-AN"
                  value="Añasco"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Añasco</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-UT"
                  id="PR-AC"
                  value="Arecibo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Arecibo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-TJ"
                  id="PR-AR"
                  value="Arroyo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Arroyo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-TB"
                  id="PR-BC"
                  value="Barceloneta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Barceloneta</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-TA"
                  id="PR-BQ"
                  value="Barranquitas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Barranquitas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SI"
                  id="PR-BY"
                  value="Bayamón"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Bayamón</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SS"
                  id="PR-CR"
                  value="Cabo Rojo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cabo Rojo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SL"
                  id="PR-CG"
                  value="Caguas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Caguas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SJ"
                  id="PR-CA"
                  value="Camuy"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Camuy</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SG"
                  id="PR-CV"
                  value="Canóvanas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Canóvanas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SA"
                  id="PR-CN"
                  value="Carolina"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Carolina</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-SB"
                  id="PR-CT"
                  value="Cataño"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cataño</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-RG"
                  id="PR-CY"
                  value="Cayey"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cayey</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-RC"
                  id="PR-CB"
                  value="Ceiba"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ceiba</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-QB"
                  id="PR-CL"
                  value="Ciales"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ciales</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-PO"
                  id="PR-CD"
                  value="Cidra"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cidra</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-PN"
                  id="PR-CO"
                  value="Coamo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Coamo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-PT"
                  id="PR-CM"
                  value="Comerío"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Comerío</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-OR"
                  id="PR-CZ"
                  value="Corozal"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Corozal</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-NR"
                  id="PR-CU"
                  value="Culebra"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Culebra</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-NG"
                  id="PR-DO"
                  value="Dorado"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Dorado</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MV"
                  id="PR-FJ"
                  value="Fajardo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Fajardo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MC"
                  id="PR-FL"
                  value="Florida"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Florida</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MG"
                  id="PR-GC"
                  value="Guánica"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guánica</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MB"
                  id="PR-GM"
                  value="Guayama"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guayama</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MR"
                  id="PR-GL"
                  value="Guayanilla"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guayanilla</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-MT"
                  id="PR-GB"
                  value="Guaynabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guaynabo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LQ"
                  id="PR-GR"
                  value="Gurabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Gurabo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LZ"
                  id="PR-HA"
                  value="Hatillo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Hatillo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LP"
                  id="PR-HO"
                  value="Hormigueros"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Hormigueros</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LM"
                  id="PR-HU"
                  value="Humacao"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Humacao</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LR"
                  id="PR-IS"
                  value="Isabela"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Isabela</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-LJ"
                  id="PR-JY"
                  value="Jayuya"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Jayuya</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-JC"
                  id="PR-JD"
                  value="Juana Díaz"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Juana Díaz</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-JD"
                  id="PR-JC"
                  value="Juncos"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Juncos</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-JY"
                  id="PR-LJ"
                  value="Lajas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Lajas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-IS"
                  id="PR-LR"
                  value="Lares"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Lares</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-HU"
                  id="PR-LM"
                  value="Las Marías"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Las Marías</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-HO"
                  id="PR-LP"
                  value="Las Piedras"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Las Piedras</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-HA"
                  id="PR-LZ"
                  value="Loíza"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Loíza</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-GR"
                  id="PR-LQ"
                  value="Luquillo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Luquillo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-GB"
                  id="PR-MT"
                  value="Manatí"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Manatí</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-GL"
                  id="PR-MR"
                  value="Maricao"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Maricao</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-GM"
                  id="PR-MB"
                  value="Maunabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Maunabo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-GC"
                  id="PR-MG"
                  value="Mayagüez"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Mayagüez</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-FL"
                  id="PR-MC"
                  value="Moca"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Moca</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-FJ"
                  id="PR-MV"
                  value="Morovis"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Morovis</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-DO"
                  id="PR-NG"
                  value="Naguabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Naguabo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CU"
                  id="PR-NR"
                  value="Naranjito"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Naranjito</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CZ"
                  id="PR-OR"
                  value="Orocovis"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Orocovis</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CM"
                  id="PR-PT"
                  value="Patillas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Patillas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CO"
                  id="PR-PN"
                  value="Peñuelas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Peñuelas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CD"
                  id="PR-PO"
                  value="Ponce"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ponce</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CL"
                  id="PR-QB"
                  value="Quebradillas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Quebradillas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CB"
                  id="PR-RC"
                  value="Rincón"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Rincón</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CY"
                  id="PR-RG"
                  value="Río Grande"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Río Grande</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CT"
                  id="PR-SB"
                  value="Sabana Grande"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Sabana Grande</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CN"
                  id="PR-SA"
                  value="Salinas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Salinas</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CV"
                  id="PR-SG"
                  value="San Germán"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Germán</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CA"
                  id="PR-SJ"
                  value="San Juan"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Juan</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CG"
                  id="PR-SL"
                  value="San Lorenzo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Lorenzo</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-CR"
                  id="PR-SS"
                  value="San Sebastián"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Sebastián</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-BY"
                  id="PR-SI"
                  value="Santa Isabel"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Santa Isabel</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-BQ"
                  id="PR-TA"
                  value="Toa Alta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Toa Alta</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-BC"
                  id="PR-TB"
                  value="Toa Baja"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Toa Baja</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AR"
                  id="PR-TJ"
                  value="Trujillo Alto"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Trujillo Alto</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AC"
                  id="PR-UT"
                  value="Utuado"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Utuado</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AN"
                  id="PR-VA"
                  value="Vega Alta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vega Alta</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AI"
                  id="PR-VB"
                  value="Vega Baja"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vega Baja</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AB"
                  id="PR-VQ"
                  value="Vieques"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vieques</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AL"
                  id="PR-VL"
                  value="Villalba"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Villalba</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AD"
                  id="PR-YB"
                  value="Yabucoa"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Yabucoa</label
              >
            </div>
          </td>
        </tr>

        <tr>
          <td>
            <div class="checkbox">
              <label
                ><input
                  type="checkbox"
                  name="map"
                  ref="PR-AJ"
                  id="PR-YU"
                  value="Yauco"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Yauco</label
              >
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "MunicipalityList",
  props: {selectedLocations: Array},
    
  data() {
    return {
    };
  },
  computed:{
    setLocations: function(){
      return this.selectedLocations
    }
  },
  methods:{
    updateLocations(event){
      this.$emit('updateLocations', !event.target.checked);
    }
  },
};
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>