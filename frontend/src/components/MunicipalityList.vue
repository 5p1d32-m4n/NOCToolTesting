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
<<<<<<< HEAD
                  id= "PR-AJ"
                  @change="$emit('update',newLocations)"
                  value="Adjuntas"
                  v-model="newSelectedLocations"
                />Adjuntas</label>
=======
                  id="PR-AJ"
                  value="Adjuntas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Adjuntas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AD"
                  @change="$emit('update',newLocations)"
                  value="Aguada"
                  v-model="newSelectedLocations"
                />Aguada</label>
=======
                  id="PR-AD"
                  value="Aguada"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguada</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AL"
                  @change="$emit('update',newLocations)"
                  value="Aguadilla"
                  v-model="newSelectedLocations"
                />Aguadilla</label>
=======
                  id="PR-AL"
                  value="Aguadilla"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguadilla</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AB"
                  @change="$emit('update',newLocations)"
                  value="Aguas Buenas"
                  v-model="newSelectedLocations"
                />Aguas Buenas</label>
=======
                  id="PR-AB"
                  value="Aguas Buenas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aguas Buenas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AI"
                  @change="$emit('update',newLocations)"
                  value="Aibonito"
                  v-model="newSelectedLocations"
                />Aibonito</label>
=======
                  id="PR-AI"
                  value="Aibonito"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Aibonito</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AN"
                  @change="$emit('update',newLocations)"
                  value="Añasco"
                  v-model="newSelectedLocations"
                />Añasco</label>
=======
                  id="PR-AN"
                  value="Añasco"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Añasco</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AC"
                  @change="$emit('update',newLocations)"
                  value="Arecibo"
                  v-model="newSelectedLocations"
                />Arecibo</label>
=======
                  id="PR-AC"
                  value="Arecibo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Arecibo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-AR"
                  @change="$emit('update',newLocations)"
                  value="Arroyo"
                  v-model="newSelectedLocations"
                />Arroyo</label>
=======
                  id="PR-AR"
                  value="Arroyo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Arroyo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-BC"
                  @change="$emit('update',newLocations)"
                  value="Barceloneta"
                  v-model="newSelectedLocations"
                />Barceloneta</label>
=======
                  id="PR-BC"
                  value="Barceloneta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Barceloneta</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-BQ"
                  @change="$emit('update',newLocations)"
                  value="Barranquitas"
                  v-model="newSelectedLocations"
                />Barranquitas</label>
=======
                  id="PR-BQ"
                  value="Barranquitas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Barranquitas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-BY"
                  @change="$emit('update',newLocations)"
                  value="Bayamón"
                  v-model="newSelectedLocations"
                />Bayamón</label>
=======
                  id="PR-BY"
                  value="Bayamón"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Bayamón</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CR"
                  @change="$emit('update',newLocations)"
                  value="Cabo Rojo"
                  v-model="newSelectedLocations"
                />Cabo Rojo</label>
=======
                  id="PR-CR"
                  value="Cabo Rojo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cabo Rojo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CG"
                  @change="$emit('update',newLocations)"
                  value="Caguas"
                  v-model="newSelectedLocations"
                />Caguas</label>
=======
                  id="PR-CG"
                  value="Caguas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Caguas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CA"
                  @change="$emit('update',newLocations)"
                  value="Camuy"
                  v-model="newSelectedLocations"
                />Camuy</label>
=======
                  id="PR-CA"
                  value="Camuy"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Camuy</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CV"
                  @change="$emit('update',newLocations)"
                  value="Canóvanas"
                  v-model="newSelectedLocations"
                />Canóvanas</label>
=======
                  id="PR-CV"
                  value="Canóvanas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Canóvanas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CN"
                  @change="$emit('update',newLocations)"
                  value="Carolina"
                  v-model="newSelectedLocations"
                />Carolina</label>
=======
                  id="PR-CN"
                  value="Carolina"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Carolina</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CT"
                  @change="$emit('update',newLocations)"
                  value="Cataño"
                  v-model="newSelectedLocations"
                />Cataño</label>
=======
                  id="PR-CT"
                  value="Cataño"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cataño</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CY"
                  @change="$emit('update',newLocations)"
                  value="Cayey"
                  v-model="newSelectedLocations"
                />Cayey</label>
=======
                  id="PR-CY"
                  value="Cayey"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cayey</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CB"
                  @change="$emit('update',newLocations)"
                  value="Ceiba"
                  v-model="newSelectedLocations"
                />Ceiba</label>
=======
                  id="PR-CB"
                  value="Ceiba"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ceiba</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CL"
                  @change="$emit('update',newLocations)"
                  value="Ciales"
                  v-model="newSelectedLocations"
                />Ciales</label>
=======
                  id="PR-CL"
                  value="Ciales"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ciales</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CD"
                  @change="$emit('update',newLocations)"
                  value="Cidra"
                  v-model="newSelectedLocations"
                />Cidra</label>
=======
                  id="PR-CD"
                  value="Cidra"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Cidra</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CO"
                  @change="$emit('update',newLocations)"
                  value="Coamo"
                  v-model="newSelectedLocations"
                />Coamo</label>
=======
                  id="PR-CO"
                  value="Coamo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Coamo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CM"
                  @change="$emit('update',newLocations)"
                  value="Comerío"
                  v-model="newSelectedLocations"
                />Comerío</label>
=======
                  id="PR-CM"
                  value="Comerío"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Comerío</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CZ"
                  @change="$emit('update',newLocations)"
                  value="Corozal"
                  v-model="newSelectedLocations"
                />Corozal</label>
=======
                  id="PR-CZ"
                  value="Corozal"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Corozal</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-CU"
                  @change="$emit('update',newLocations)"
                  value="Culebra"
                  v-model="newSelectedLocations"
                />Culebra</label>
=======
                  id="PR-CU"
                  value="Culebra"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Culebra</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-DO"
                  @change="$emit('update',newLocations)"
                  value="Dorado"
                  v-model="newSelectedLocations"
                />Dorado</label>
=======
                  id="PR-DO"
                  value="Dorado"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Dorado</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-FJ"
                  @change="$emit('update',newLocations)"
                  value="Fajardo"
                  v-model="newSelectedLocations"
                />Fajardo</label>
=======
                  id="PR-FJ"
                  value="Fajardo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Fajardo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-FL"
                  @change="$emit('update',newLocations)"
                  value="Florida"
                  v-model="newSelectedLocations"
                />Florida</label>
=======
                  id="PR-FL"
                  value="Florida"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Florida</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-GC"
                  @change="$emit('update',newLocations)"
                  value="Guánica"
                  v-model="newSelectedLocations"
                />Guánica</label>
=======
                  id="PR-GC"
                  value="Guánica"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guánica</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-GM"
                  @change="$emit('update',newLocations)"
                  value="Guayama"
                  v-model="newSelectedLocations"
                />Guayama</label>
=======
                  id="PR-GM"
                  value="Guayama"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guayama</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-GL"
                  @change="$emit('update',newLocations)"
                  value="Guayanilla"
                  v-model="newSelectedLocations"
                />Guayanilla</label>
=======
                  id="PR-GL"
                  value="Guayanilla"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guayanilla</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-GB"
                  @change="$emit('update',newLocations)"
                  value="Guaynabo"
                  v-model="newSelectedLocations"
                />Guaynabo</label>
=======
                  id="PR-GB"
                  value="Guaynabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Guaynabo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-GR"
                  @change="$emit('update',newLocations)"
                  value="Gurabo"
                  v-model="newSelectedLocations"
                />Gurabo</label>
=======
                  id="PR-GR"
                  value="Gurabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Gurabo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-HA"
                  @change="$emit('update',newLocations)"
                  value="Hatillo"
                  v-model="newSelectedLocations"
                />Hatillo</label>
=======
                  id="PR-HA"
                  value="Hatillo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Hatillo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-HO"
                  @change="$emit('update',newLocations)"
                  value="Hormigueros"
                  v-model="newSelectedLocations"
                />Hormigueros</label>
=======
                  id="PR-HO"
                  value="Hormigueros"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Hormigueros</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-HU"
                  @change="$emit('update',newLocations)"
                  value="Humacao"
                  v-model="newSelectedLocations"
                />Humacao</label>
=======
                  id="PR-HU"
                  value="Humacao"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Humacao</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-IS"
                  @change="$emit('update',newLocations)"
                  value="Isabela"
                  v-model="newSelectedLocations"
                />Isabela</label>
=======
                  id="PR-IS"
                  value="Isabela"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Isabela</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-JY"
                  @change="$emit('update',newLocations)"
                  value="Jayuya"
                  v-model="newSelectedLocations"
                />Jayuya</label>
=======
                  id="PR-JY"
                  value="Jayuya"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Jayuya</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-JD"
                  @change="$emit('update',newLocations)"
                  value="Juana Díaz"
                  v-model="newSelectedLocations"
                />Juana Díaz</label>
=======
                  id="PR-JD"
                  value="Juana Díaz"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Juana Díaz</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-JC"
                  @change="$emit('update',newLocations)"
                  value="Juncos"
                  v-model="newSelectedLocations"
                />Juncos</label>
=======
                  id="PR-JC"
                  value="Juncos"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Juncos</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LJ"
                  @change="$emit('update',newLocations)"
                  value="Lajas"
                  v-model="newSelectedLocations"
                />Lajas</label>
=======
                  id="PR-LJ"
                  value="Lajas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Lajas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LR"
                  @change="$emit('update',newLocations)"
                  value="Lares"
                  v-model="newSelectedLocations"
                />Lares</label>
=======
                  id="PR-LR"
                  value="Lares"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Lares</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LM"
                  @change="$emit('update',newLocations)"
                  value="Las Marías"
                  v-model="newSelectedLocations"
                />Las Marías</label>
=======
                  id="PR-LM"
                  value="Las Marías"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Las Marías</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LP"
                  @change="$emit('update',newLocations)"
                  value="Las Piedras"
                  v-model="newSelectedLocations"
                />Las Piedras</label>
=======
                  id="PR-LP"
                  value="Las Piedras"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Las Piedras</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LZ"
                  @change="$emit('update',newLocations)"
                  value="Loíza"
                  v-model="newSelectedLocations"
                />Loíza</label>
=======
                  id="PR-LZ"
                  value="Loíza"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Loíza</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-LQ"
                  @change="$emit('update',newLocations)"
                  value="Luquillo"
                  v-model="newSelectedLocations"
                />Luquillo</label>
=======
                  id="PR-LQ"
                  value="Luquillo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Luquillo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MT"
                  @change="$emit('update',newLocations)"
                  value="Manatí"
                  v-model="newSelectedLocations"
                />Manatí</label>
=======
                  id="PR-MT"
                  value="Manatí"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Manatí</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MR"
                  @change="$emit('update',newLocations)"
                  value="Maricao"
                  v-model="newSelectedLocations"
                />Maricao</label>
=======
                  id="PR-MR"
                  value="Maricao"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Maricao</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MB"
                  @change="$emit('update',newLocations)"
                  value="Maunabo"
                  v-model="newSelectedLocations"
                />Maunabo</label>
=======
                  id="PR-MB"
                  value="Maunabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Maunabo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MG"
                  @change="$emit('update',newLocations)"
                  value="Mayagüez"
                  v-model="newSelectedLocations"
                />Mayagüez</label>
=======
                  id="PR-MG"
                  value="Mayagüez"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Mayagüez</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MC"
                  @change="$emit('update',newLocations)"
                  value="Moca"
                  v-model="newSelectedLocations"
                />Moca</label>
=======
                  id="PR-MC"
                  value="Moca"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Moca</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-MV"
                  @change="$emit('update',newLocations)"
                  value="Morovis"
                  v-model="newSelectedLocations"
                />Morovis</label>
=======
                  id="PR-MV"
                  value="Morovis"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Morovis</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-NG"
                  @change="$emit('update',newLocations)"
                  value="Naguabo"
                  v-model="newSelectedLocations"
                />Naguabo</label>
=======
                  id="PR-NG"
                  value="Naguabo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Naguabo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-NR"
                  @change="$emit('update',newLocations)"
                  value="Naranjito"
                  v-model="newSelectedLocations"
                />Naranjito</label>
=======
                  id="PR-NR"
                  value="Naranjito"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Naranjito</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-OR"
                  @change="$emit('update',newLocations)"
                  value="Orocovis"
                  v-model="newSelectedLocations"
                />Orocovis</label>
=======
                  id="PR-OR"
                  value="Orocovis"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Orocovis</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-PT"
                  @change="$emit('update',newLocations)"
                  value="Patillas"
                  v-model="newSelectedLocations"
                />Patillas</label>
=======
                  id="PR-PT"
                  value="Patillas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Patillas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-PN"
                  @change="$emit('update',newLocations)"
                  value="Peñuelas"
                  v-model="newSelectedLocations"
                />Peñuelas</label>
=======
                  id="PR-PN"
                  value="Peñuelas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Peñuelas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-PO"
                  @change="$emit('update',newLocations)"
                  value="Ponce"
                  v-model="newSelectedLocations"
                />Ponce</label>
=======
                  id="PR-PO"
                  value="Ponce"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Ponce</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-QB"
                  @change="$emit('update',newLocations)"
                  value="Quebradillas"
                  v-model="newSelectedLocations"
                />Quebradillas</label>
=======
                  id="PR-QB"
                  value="Quebradillas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Quebradillas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-RC"
                  @change="$emit('update',newLocations)"
                  value="Rincón"
                  v-model="newSelectedLocations"
                />Rincón</label>
=======
                  id="PR-RC"
                  value="Rincón"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Rincón</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-RG"
                  @change="$emit('update',newLocations)"
                  value="Río Grande"
                  v-model="newSelectedLocations"
                />Río Grande</label>
=======
                  id="PR-RG"
                  value="Río Grande"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Río Grande</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SB"
                  @change="$emit('update',newLocations)"
                  value="Sabana Grande"
                  v-model="newSelectedLocations"
                />Sabana Grande</label>
=======
                  id="PR-SB"
                  value="Sabana Grande"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Sabana Grande</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SA"
                  @change="$emit('update',newLocations)"
                  value="Salinas"
                  v-model="newSelectedLocations"
                />Salinas</label>
=======
                  id="PR-SA"
                  value="Salinas"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Salinas</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SG"
                  @change="$emit('update',newLocations)"
                  value="San Germán"
                  v-model="newSelectedLocations"
                />San Germán</label>
=======
                  id="PR-SG"
                  value="San Germán"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Germán</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SJ"
                  @change="$emit('update',newLocations)"
                  value="San Juan"
                  v-model="newSelectedLocations"
                />San Juan</label>
=======
                  id="PR-SJ"
                  value="San Juan"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Juan</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SL"
                  @change="$emit('update',newLocations)"
                  value="San Lorenzo"
                  v-model="newSelectedLocations"
                />San Lorenzo</label>
=======
                  id="PR-SL"
                  value="San Lorenzo"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Lorenzo</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SS"
                  @change="$emit('update',newLocations)"
                  value="San Sebastián"
                  v-model="newSelectedLocations"
                />San Sebastián</label>
=======
                  id="PR-SS"
                  value="San Sebastián"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />San Sebastián</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-SI"
                  @change="$emit('update',newLocations)"
                  value="Santa Isabel"
                  v-model="newSelectedLocations"
                />Santa Isabel</label>
=======
                  id="PR-SI"
                  value="Santa Isabel"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Santa Isabel</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-TA"
                  @change="$emit('update',newLocations)"
                  value="Toa Alta"
                  v-model="newSelectedLocations"
                />Toa Alta</label>
=======
                  id="PR-TA"
                  value="Toa Alta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Toa Alta</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-TB"
                  @change="$emit('update',newLocations)"
                  value="Toa Baja"
                  v-model="newSelectedLocations"
                />Toa Baja</label>
=======
                  id="PR-TB"
                  value="Toa Baja"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Toa Baja</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-TJ"
                  @change="$emit('update',newLocations)"
                  value="Trujillo Alto"
                  v-model="newSelectedLocations"
                />Trujillo Alto</label>
=======
                  id="PR-TJ"
                  value="Trujillo Alto"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Trujillo Alto</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-UT"
                  @change="$emit('update',newLocations)"
                  value="Utuado"
                  v-model="newSelectedLocations"
                />Utuado</label>
=======
                  id="PR-UT"
                  value="Utuado"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Utuado</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-VA"
                  @change="$emit('update',newLocations)"
                  value="Vega Alta"
                  v-model="newSelectedLocations"
                />Vega Alta</label>
=======
                  id="PR-VA"
                  value="Vega Alta"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vega Alta</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-VB"
                  @change="$emit('update',newLocations)"
                  value="Vega Baja"
                  v-model="newSelectedLocations"
                />Vega Baja</label>
=======
                  id="PR-VB"
                  value="Vega Baja"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vega Baja</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-VQ"
                  @change="$emit('update',newLocations)"
                  value="Vieques"
                  v-model="newSelectedLocations"
                />Vieques</label>
=======
                  id="PR-VQ"
                  value="Vieques"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Vieques</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-VL"
                  @change="$emit('update',newLocations)"
                  value="Villalba"
                  v-model="newSelectedLocations"
                />Villalba</label>
=======
                  id="PR-VL"
                  value="Villalba"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Villalba</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-YB"
                  @change="$emit('update',newLocations)"
                  value="Yabucoa"
                  v-model="newSelectedLocations"
                />Yabucoa</label>
=======
                  id="PR-YB"
                  value="Yabucoa"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Yabucoa</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
                  id= "PR-YU"
                  @change="$emit('update',newLocations)"
                  value="Yauco"
                  v-model="newSelectedLocations"
                />Yauco</label>
=======
                  id="PR-YU"
                  value="Yauco"
                  @change="$emit(updateLocations)"
                  v-model="selectedLocations"
                />Yauco</label
              >
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
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
<<<<<<< HEAD
  props:{
    selectedLocation: Array,
    },
=======
  props: {selectedLocations: Array},
    
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
  data() {
    return {
    };
  },
<<<<<<< HEAD
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
=======
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
>>>>>>> 9eaceaca66e1f8048872922005e5db2ae09a018a
};
</script>

<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>