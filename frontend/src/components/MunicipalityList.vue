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
                  value="Adjuntas"
                  v-model="selected"
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
                  value="Aguada"
                  v-model="selected"
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
                  value="Aguadilla"
                  v-model="selected"
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
                  value="Aguas Buenas"
                  v-model="selected"
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
                  value="Aibonito"
                  v-model="selected"
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
                  value="Añasco"
                  v-model="selected"
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
                  value="Arecibo"
                  v-model="selected"
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
                  value="Arroyo"
                  v-model="selected"
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
                  value="Barceloneta"
                  v-model="selected"
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
                  value="Barranquitas"
                  v-model="selected"
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
                  value="Bayamón"
                  v-model="selected"
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
                  value="Cabo Rojo"
                  v-model="selected"
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
                  value="Caguas"
                  v-model="selected"
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
                  value="Camuy"
                  v-model="selected"
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
                  value="Canóvanas"
                  v-model="selected"
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
                  value="Carolina"
                  v-model="selected"
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
                  value="Cataño"
                  v-model="selected"
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
                  value="Cayey"
                  v-model="selected"
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
                  value="Ceiba"
                  v-model="selected"
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
                  value="Ciales"
                  v-model="selected"
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
                  value="Cidra"
                  v-model="selected"
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
                  value="Coamo"
                  v-model="selected"
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
                  value="Comerío"
                  v-model="selected"
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
                  value="Corozal"
                  v-model="selected"
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
                  value="Culebra"
                  v-model="selected"
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
                  value="Dorado"
                  v-model="selected"
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
                  value="Fajardo"
                  v-model="selected"
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
                  value="Florida"
                  v-model="selected"
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
                  value="Guánica"
                  v-model="selected"
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
                  value="Guayama"
                  v-model="selected"
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
                  value="Guayanilla"
                  v-model="selected"
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
                  value="Guaynabo"
                  v-model="selected"
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
                  value="Gurabo"
                  v-model="selected"
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
                  value="Hatillo"
                  v-model="selected"
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
                  value="Hormigueros"
                  v-model="selected"
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
                  value="Humacao"
                  v-model="selected"
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
                  value="Isabela"
                  v-model="selected"
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
                  value="Jayuya"
                  v-model="selected"
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
                  value="Juana Díaz"
                  v-model="selected"
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
                  value="Juncos"
                  v-model="selected"
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
                  value="Lajas"
                  v-model="selected"
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
                  value="Lares"
                  v-model="selected"
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
                  value="Las Marías"
                  v-model="selected"
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
                  value="Las Piedras"
                  v-model="selected"
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
                  value="Loíza"
                  v-model="selected"
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
                  value="Luquillo"
                  v-model="selected"
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
                  value="Manatí"
                  v-model="selected"
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
                  value="Maricao"
                  v-model="selected"
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
                  value="Maunabo"
                  v-model="selected"
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
                  value="Mayagüez"
                  v-model="selected"
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
                  value="Moca"
                  v-model="selected"
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
                  value="Morovis"
                  v-model="selected"
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
                  value="Naguabo"
                  v-model="selected"
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
                  value="Naranjito"
                  v-model="selected"
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
                  value="Orocovis"
                  v-model="selected"
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
                  value="Patillas"
                  v-model="selected"
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
                  value="Peñuelas"
                  v-model="selected"
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
                  value="Ponce"
                  v-model="selected"
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
                  value="Quebradillas"
                  v-model="selected"
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
                  value="Rincón"
                  v-model="selected"
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
                  value="Río Grande"
                  v-model="selected"
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
                  value="Sabana Grande"
                  v-model="selected"
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
                  value="Salinas"
                  v-model="selected"
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
                  value="San Germán"
                  v-model="selected"
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
                  value="San Juan"
                  v-model="selected"
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
                  value="San Lorenzo"
                  v-model="selected"
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
                  value="San Sebastián"
                  v-model="selected"
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
                  value="Santa Isabel"
                  v-model="selected"
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
                  value="Toa Alta"
                  v-model="selected"
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
                  value="Toa Baja"
                  v-model="selected"
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
                  value="Trujillo Alto"
                  v-model="selected"
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
                  value="Utuado"
                  v-model="selected"
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
                  value="Vega Alta"
                  v-model="selected"
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
                  value="Vega Baja"
                  v-model="selected"
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
                  value="Vieques"
                  v-model="selected"
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
                  value="Villalba"
                  v-model="selected"
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
                  value="Yabucoa"
                  v-model="selected"
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
                  value="Yauco"
                  v-model="selected"
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
  props: {
    selected: []
  },
  data() {
    return {
      // selected: [],
    };
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