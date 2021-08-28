<template>
  <div class=" overflow-auto" id="municipality-table">
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
                  id= "PR-AJ"
                  @change="$emit('update',newLocations)"
                  value="Adjuntas"
                  v-model="newSelectedLocations"
                />Adjuntas</label>
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
                  id= "PR-AD"
                  @change="$emit('update',newLocations)"
                  value="Aguada"
                  v-model="newSelectedLocations"
                />Aguada</label>
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
                  id= "PR-AL"
                  @change="$emit('update',newLocations)"
                  value="Aguadilla"
                  v-model="newSelectedLocations"
                />Aguadilla</label>
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
                  id= "PR-AB"
                  @change="$emit('update',newLocations)"
                  value="Aguas Buenas"
                  v-model="newSelectedLocations"
                />Aguas Buenas</label>
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
                  id= "PR-AI"
                  @change="$emit('update',newLocations)"
                  value="Aibonito"
                  v-model="newSelectedLocations"
                />Aibonito</label>
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
                  id= "PR-AN"
                  @change="$emit('update',newLocations)"
                  value="Añasco"
                  v-model="newSelectedLocations"
                />Añasco</label>
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
                  id= "PR-AC"
                  @change="$emit('update',newLocations)"
                  value="Arecibo"
                  v-model="newSelectedLocations"
                />Arecibo</label>
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
                  id= "PR-AR"
                  @change="$emit('update',newLocations)"
                  value="Arroyo"
                  v-model="newSelectedLocations"
                />Arroyo</label>
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
                  id= "PR-BC"
                  @change="$emit('update',newLocations)"
                  value="Barceloneta"
                  v-model="newSelectedLocations"
                />Barceloneta</label>
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
                  id= "PR-BQ"
                  @change="$emit('update',newLocations)"
                  value="Barranquitas"
                  v-model="newSelectedLocations"
                />Barranquitas</label>
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
                  id= "PR-BY"
                  @change="$emit('update',newLocations)"
                  value="Bayamón"
                  v-model="newSelectedLocations"
                />Bayamón</label>
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
                  id= "PR-CR"
                  @change="$emit('update',newLocations)"
                  value="Cabo Rojo"
                  v-model="newSelectedLocations"
                />Cabo Rojo</label>
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
                  id= "PR-CG"
                  @change="$emit('update',newLocations)"
                  value="Caguas"
                  v-model="newSelectedLocations"
                />Caguas</label>
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
                  id= "PR-CA"
                  @change="$emit('update',newLocations)"
                  value="Camuy"
                  v-model="newSelectedLocations"
                />Camuy</label>
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
                  id= "PR-CV"
                  @change="$emit('update',newLocations)"
                  value="Canóvanas"
                  v-model="newSelectedLocations"
                />Canóvanas</label>
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
                  id= "PR-CN"
                  @change="$emit('update',newLocations)"
                  value="Carolina"
                  v-model="newSelectedLocations"
                />Carolina</label>
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
                  id= "PR-CT"
                  @change="$emit('update',newLocations)"
                  value="Cataño"
                  v-model="newSelectedLocations"
                />Cataño</label>
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
                  id= "PR-CY"
                  @change="$emit('update',newLocations)"
                  value="Cayey"
                  v-model="newSelectedLocations"
                />Cayey</label>
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
                  id= "PR-CB"
                  @change="$emit('update',newLocations)"
                  value="Ceiba"
                  v-model="newSelectedLocations"
                />Ceiba</label>
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
                  id= "PR-CL"
                  @change="$emit('update',newLocations)"
                  value="Ciales"
                  v-model="newSelectedLocations"
                />Ciales</label>
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
                  id= "PR-CD"
                  @change="$emit('update',newLocations)"
                  value="Cidra"
                  v-model="newSelectedLocations"
                />Cidra</label>
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
                  id= "PR-CO"
                  @change="$emit('update',newLocations)"
                  value="Coamo"
                  v-model="newSelectedLocations"
                />Coamo</label>
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
                  id= "PR-CM"
                  @change="$emit('update',newLocations)"
                  value="Comerío"
                  v-model="newSelectedLocations"
                />Comerío</label>
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
                  id= "PR-CZ"
                  @change="$emit('update',newLocations)"
                  value="Corozal"
                  v-model="newSelectedLocations"
                />Corozal</label>
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
                  id= "PR-CU"
                  @change="$emit('update',newLocations)"
                  value="Culebra"
                  v-model="newSelectedLocations"
                />Culebra</label>
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
                  id= "PR-DO"
                  @change="$emit('update',newLocations)"
                  value="Dorado"
                  v-model="newSelectedLocations"
                />Dorado</label>
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
                  id= "PR-FJ"
                  @change="$emit('update',newLocations)"
                  value="Fajardo"
                  v-model="newSelectedLocations"
                />Fajardo</label>
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
                  id= "PR-FL"
                  @change="$emit('update',newLocations)"
                  value="Florida"
                  v-model="newSelectedLocations"
                />Florida</label>
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
                  id= "PR-GC"
                  @change="$emit('update',newLocations)"
                  value="Guánica"
                  v-model="newSelectedLocations"
                />Guánica</label>
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
                  id= "PR-GM"
                  @change="$emit('update',newLocations)"
                  value="Guayama"
                  v-model="newSelectedLocations"
                />Guayama</label>
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
                  id= "PR-GL"
                  @change="$emit('update',newLocations)"
                  value="Guayanilla"
                  v-model="newSelectedLocations"
                />Guayanilla</label>
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
                  id= "PR-GB"
                  @change="$emit('update',newLocations)"
                  value="Guaynabo"
                  v-model="newSelectedLocations"
                />Guaynabo</label>
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
                  id= "PR-GR"
                  @change="$emit('update',newLocations)"
                  value="Gurabo"
                  v-model="newSelectedLocations"
                />Gurabo</label>
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
                  id= "PR-HA"
                  @change="$emit('update',newLocations)"
                  value="Hatillo"
                  v-model="newSelectedLocations"
                />Hatillo</label>
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
                  id= "PR-HO"
                  @change="$emit('update',newLocations)"
                  value="Hormigueros"
                  v-model="newSelectedLocations"
                />Hormigueros</label>
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
                  id= "PR-HU"
                  @change="$emit('update',newLocations)"
                  value="Humacao"
                  v-model="newSelectedLocations"
                />Humacao</label>
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
                  id= "PR-IS"
                  @change="$emit('update',newLocations)"
                  value="Isabela"
                  v-model="newSelectedLocations"
                />Isabela</label>
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
                  id= "PR-JY"
                  @change="$emit('update',newLocations)"
                  value="Jayuya"
                  v-model="newSelectedLocations"
                />Jayuya</label>
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
                  id= "PR-JD"
                  @change="$emit('update',newLocations)"
                  value="Juana Díaz"
                  v-model="newSelectedLocations"
                />Juana Díaz</label>
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
                  id= "PR-JC"
                  @change="$emit('update',newLocations)"
                  value="Juncos"
                  v-model="newSelectedLocations"
                />Juncos</label>
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
                  id= "PR-LJ"
                  @change="$emit('update',newLocations)"
                  value="Lajas"
                  v-model="newSelectedLocations"
                />Lajas</label>
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
                  id= "PR-LR"
                  @change="$emit('update',newLocations)"
                  value="Lares"
                  v-model="newSelectedLocations"
                />Lares</label>
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
                  id= "PR-LM"
                  @change="$emit('update',newLocations)"
                  value="Las Marías"
                  v-model="newSelectedLocations"
                />Las Marías</label>
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
                  id= "PR-LP"
                  @change="$emit('update',newLocations)"
                  value="Las Piedras"
                  v-model="newSelectedLocations"
                />Las Piedras</label>
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
                  id= "PR-LZ"
                  @change="$emit('update',newLocations)"
                  value="Loíza"
                  v-model="newSelectedLocations"
                />Loíza</label>
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
                  id= "PR-LQ"
                  @change="$emit('update',newLocations)"
                  value="Luquillo"
                  v-model="newSelectedLocations"
                />Luquillo</label>
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
                  id= "PR-MT"
                  @change="$emit('update',newLocations)"
                  value="Manatí"
                  v-model="newSelectedLocations"
                />Manatí</label>
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
                  id= "PR-MR"
                  @change="$emit('update',newLocations)"
                  value="Maricao"
                  v-model="newSelectedLocations"
                />Maricao</label>
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
                  id= "PR-MB"
                  @change="$emit('update',newLocations)"
                  value="Maunabo"
                  v-model="newSelectedLocations"
                />Maunabo</label>
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
                  id= "PR-MG"
                  @change="$emit('update',newLocations)"
                  value="Mayagüez"
                  v-model="newSelectedLocations"
                />Mayagüez</label>
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
                  id= "PR-MC"
                  @change="$emit('update',newLocations)"
                  value="Moca"
                  v-model="newSelectedLocations"
                />Moca</label>
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
                  id= "PR-MV"
                  @change="$emit('update',newLocations)"
                  value="Morovis"
                  v-model="newSelectedLocations"
                />Morovis</label>
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
                  id= "PR-NG"
                  @change="$emit('update',newLocations)"
                  value="Naguabo"
                  v-model="newSelectedLocations"
                />Naguabo</label>
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
                  id= "PR-NR"
                  @change="$emit('update',newLocations)"
                  value="Naranjito"
                  v-model="newSelectedLocations"
                />Naranjito</label>
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
                  id= "PR-OR"
                  @change="$emit('update',newLocations)"
                  value="Orocovis"
                  v-model="newSelectedLocations"
                />Orocovis</label>
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
                  id= "PR-PT"
                  @change="$emit('update',newLocations)"
                  value="Patillas"
                  v-model="newSelectedLocations"
                />Patillas</label>
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
                  id= "PR-PN"
                  @change="$emit('update',newLocations)"
                  value="Peñuelas"
                  v-model="newSelectedLocations"
                />Peñuelas</label>
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
                  id= "PR-PO"
                  @change="$emit('update',newLocations)"
                  value="Ponce"
                  v-model="newSelectedLocations"
                />Ponce</label>
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
                  id= "PR-QB"
                  @change="$emit('update',newLocations)"
                  value="Quebradillas"
                  v-model="newSelectedLocations"
                />Quebradillas</label>
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
                  id= "PR-RC"
                  @change="$emit('update',newLocations)"
                  value="Rincón"
                  v-model="newSelectedLocations"
                />Rincón</label>
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
                  id= "PR-RG"
                  @change="$emit('update',newLocations)"
                  value="Río Grande"
                  v-model="newSelectedLocations"
                />Río Grande</label>
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
                  id= "PR-SB"
                  @change="$emit('update',newLocations)"
                  value="Sabana Grande"
                  v-model="newSelectedLocations"
                />Sabana Grande</label>
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
                  id= "PR-SA"
                  @change="$emit('update',newLocations)"
                  value="Salinas"
                  v-model="newSelectedLocations"
                />Salinas</label>
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
                  id= "PR-SG"
                  @change="$emit('update',newLocations)"
                  value="San Germán"
                  v-model="newSelectedLocations"
                />San Germán</label>
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
                  id= "PR-SJ"
                  @change="$emit('update',newLocations)"
                  value="San Juan"
                  v-model="newSelectedLocations"
                />San Juan</label>
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
                  id= "PR-SL"
                  @change="$emit('update',newLocations)"
                  value="San Lorenzo"
                  v-model="newSelectedLocations"
                />San Lorenzo</label>
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
                  id= "PR-SS"
                  @change="$emit('update',newLocations)"
                  value="San Sebastián"
                  v-model="newSelectedLocations"
                />San Sebastián</label>
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
                  id= "PR-SI"
                  @change="$emit('update',newLocations)"
                  value="Santa Isabel"
                  v-model="newSelectedLocations"
                />Santa Isabel</label>
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
                  id= "PR-TA"
                  @change="$emit('update',newLocations)"
                  value="Toa Alta"
                  v-model="newSelectedLocations"
                />Toa Alta</label>
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
                  id= "PR-TB"
                  @change="$emit('update',newLocations)"
                  value="Toa Baja"
                  v-model="newSelectedLocations"
                />Toa Baja</label>
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
                  id= "PR-TJ"
                  @change="$emit('update',newLocations)"
                  value="Trujillo Alto"
                  v-model="newSelectedLocations"
                />Trujillo Alto</label>
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
                  id= "PR-UT"
                  @change="$emit('update',newLocations)"
                  value="Utuado"
                  v-model="newSelectedLocations"
                />Utuado</label>
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
                  id= "PR-VA"
                  @change="$emit('update',newLocations)"
                  value="Vega Alta"
                  v-model="newSelectedLocations"
                />Vega Alta</label>
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
                  id= "PR-VB"
                  @change="$emit('update',newLocations)"
                  value="Vega Baja"
                  v-model="newSelectedLocations"
                />Vega Baja</label>
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
                  id= "PR-VQ"
                  @change="$emit('update',newLocations)"
                  value="Vieques"
                  v-model="newSelectedLocations"
                />Vieques</label>
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
                  id= "PR-VL"
                  @change="$emit('update',newLocations)"
                  value="Villalba"
                  v-model="newSelectedLocations"
                />Villalba</label>
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
                  id= "PR-YB"
                  @change="$emit('update',newLocations)"
                  value="Yabucoa"
                  v-model="newSelectedLocations"
                />Yabucoa</label>
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
                  id= "PR-YU"
                  @change="$emit('update',newLocations)"
                  value="Yauco"
                  v-model="newSelectedLocations"
                />Yauco</label>
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
  props:{
    selectedLocation: Array,
    },
  data() {
    return {
    };
  },
  methods:{
    update(){
      return this.selectedLocation
    }
  },
  computed:{
    newSelectedLocations: function(){
      return this.selectedLocation
    }
  }
};
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>