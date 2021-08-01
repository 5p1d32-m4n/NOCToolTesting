<template>
  <div id="initial-form">
    <form>
      <div class="columns">
        <div class="column" id="report-specific">
          <label for="noc_ticket">Taquilla del NOC:</label>
          <input type="text" name="noc_ticket" id="noc_ticket" class="input" />
          <label for="third_party_ticket">Taquilla de Tercero:</label>
          <input
            type="text"
            name="has-text-white-bis"
            id="has-text-white-bis"
            class="input"
          />
          <label for="dateOfEvent">Fecha de Averia:</label>
          <input
            type="date"
            name="dateOfEvent"
            id="dateOfEvent"
            class="input"
          />
          <label for="timeOfEvent">Tiempo de Averia</label>
          <input
            type="time"
            name="timeOfEvent"
            id="timeOfEvent"
            class="input"
          />
        </div>
        <!-- Dropdowns -->
        <!-- TODO: -Add the checkbox and integer inputs -->
        <div
          class="column field is-grouped btn-group-vertical"
          id="service-specific"
        >
          <!-- Service Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Outage type dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Tipo de Averia
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Client dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Clientes Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Service Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <!-- Cause Dropdown -->
          <div class="dropdown btn btn-lg">
            <button
              class="btn btn-danger dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              style="width: 200px"
            >
              Servicios Impactados
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- AM4 Map chart -->
      <div class="columns">
        <div class="column">
          <div id="mapchart" @click="appendToMunicipalitiesList"></div>
          <!-- <MunicipalityMap /> -->
          <!-- using the mapchart as a component -->
        </div>

        <!-- List of Municipality Checkboxesw -->
        <div class="column">
          <!-- <MunicipalityList /> -->
          <!-- <div id="municipality-talbe">
            <table class="table is-bordered is-fullwidth overflow-scroll">
              <thead>
                <th>Municipios Impactados</th>
              </thead>

              <tbody>
                <tr
                  v-for="country in listOfMunicipalities"
                  v-bind:key="country"
                >
                  <div class="checkbox">
                    <label
                      ><input type="checkbox" palities"
                      :v-model="selected"
                      v-bind:selcted="selected" name="map":"country"" value="country" />{{
                        country
                      }}</label
                    >
                  </div>
                </tr>
              </tbody>
            </table>
          </div> -->

          <!-- testing portion. -->
          <!-- <div
            v-bind:listOfMunicipalities="listOfMunicipalities"
          >
            <div
              class="btn-group" 
              role="group" 
              aria-label="Selector de Municipios"
              id="municipality-checkbox"
              name= "flavour"
              @change="changeStateOfMunicipality($event)"
              >

                <ul>
                  <li v-for="(country) in listOfMunicipalities" v-bind:key="country">
                    <input type="checkbox" name="{{country}}" id="{{country}}">
                    <label for="{{country}}">{{country}}</label>
                  </li>
                </ul>
            </div>
          </div> -->
          <!-- End of testing portion. -->

          <!-- straight amcharts rip -->

          <div class="col-sm-8">
            <h2
              class="
                family-light
                size-biggerer
                underline
                section-map-list-title
              "
            >
              Selecione municipios impactados.
            </h2>
            <div class="section-map-list">
              <div class="tab-content overflow-auto" style="height: 350px">
                <div id="states" class="tab-pane active">
                  <table class="table table-hover table-striped">
                    <tbody>
                      <tr>
                        <td>
                          <div class="checkbox">
                            <label
                              ><input
                                type="checkbox"
                                :v-model="selected"
                                name="map"
                                ref="PR-YU"
                                id="PR-YU"
                                value="PR-YU"
                              />Yauco</label
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
                                :v-model="selected"
                                name="map"
                                ref="PR-YB"
                                id="PR-YB"
                                value="PR-YB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-VL"
                                id="PR-VL"
                                value="PR-VL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-VQ"
                                id="PR-VQ"
                                value="PR-VQ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-VB"
                                id="PR-VB"
                                value="PR-VB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-VA"
                                id="PR-VA"
                                value="PR-VA"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-UT"
                                id="PR-UT"
                                value="PR-UT"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-TJ"
                                id="PR-TJ"
                                value="PR-TJ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-TB"
                                id="PR-TB"
                                value="PR-TB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-TA"
                                id="PR-TA"
                                value="PR-TA"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SI"
                                id="PR-SI"
                                value="PR-SI"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SS"
                                id="PR-SS"
                                value="PR-SS"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SL"
                                id="PR-SL"
                                value="PR-SL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SJ"
                                id="PR-SJ"
                                value="PR-SJ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SG"
                                id="PR-SG"
                                value="PR-SG"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SA"
                                id="PR-SA"
                                value="PR-SA"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-SB"
                                id="PR-SB"
                                value="PR-SB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-RG"
                                id="PR-RG"
                                value="PR-RG"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-RC"
                                id="PR-RC"
                                value="PR-RC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-QB"
                                id="PR-QB"
                                value="PR-QB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-PO"
                                id="PR-PO"
                                value="PR-PO"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-PN"
                                id="PR-PN"
                                value="PR-PN"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-PT"
                                id="PR-PT"
                                value="PR-PT"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-OR"
                                id="PR-OR"
                                value="PR-OR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-NR"
                                id="PR-NR"
                                value="PR-NR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-NG"
                                id="PR-NG"
                                value="PR-NG"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MV"
                                id="PR-MV"
                                value="PR-MV"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MC"
                                id="PR-MC"
                                value="PR-MC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MG"
                                id="PR-MG"
                                value="PR-MG"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MB"
                                id="PR-MB"
                                value="PR-MB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MR"
                                id="PR-MR"
                                value="PR-MR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-MT"
                                id="PR-MT"
                                value="PR-MT"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LQ"
                                id="PR-LQ"
                                value="PR-LQ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LZ"
                                id="PR-LZ"
                                value="PR-LZ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LP"
                                id="PR-LP"
                                value="PR-LP"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LM"
                                id="PR-LM"
                                value="PR-LM"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LR"
                                id="PR-LR"
                                value="PR-LR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-LJ"
                                id="PR-LJ"
                                value="PR-LJ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-JC"
                                id="PR-JC"
                                value="PR-JC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-JD"
                                id="PR-JD"
                                value="PR-JD"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-JY"
                                id="PR-JY"
                                value="PR-JY"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-IS"
                                id="PR-IS"
                                value="PR-IS"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-HU"
                                id="PR-HU"
                                value="PR-HU"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-HO"
                                id="PR-HO"
                                value="PR-HO"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-HA"
                                id="PR-HA"
                                value="PR-HA"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-GR"
                                id="PR-GR"
                                value="PR-GR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-GB"
                                id="PR-GB"
                                value="PR-GB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-GL"
                                id="PR-GL"
                                value="PR-GL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-GM"
                                id="PR-GM"
                                value="PR-GM"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-GC"
                                id="PR-GC"
                                value="PR-GC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-FL"
                                id="PR-FL"
                                value="PR-FL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-FJ"
                                id="PR-FJ"
                                value="PR-FJ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-DO"
                                id="PR-DO"
                                value="PR-DO"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CU"
                                id="PR-CU"
                                value="PR-CU"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CZ"
                                id="PR-CZ"
                                value="PR-CZ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CM"
                                id="PR-CM"
                                value="PR-CM"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CO"
                                id="PR-CO"
                                value="PR-CO"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CD"
                                id="PR-CD"
                                value="PR-CD"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CL"
                                id="PR-CL"
                                value="PR-CL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CB"
                                id="PR-CB"
                                value="PR-CB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CY"
                                id="PR-CY"
                                value="PR-CY"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CT"
                                id="PR-CT"
                                value="PR-CT"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CN"
                                id="PR-CN"
                                value="PR-CN"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CV"
                                id="PR-CV"
                                value="PR-CV"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CA"
                                id="PR-CA"
                                value="PR-CA"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CG"
                                id="PR-CG"
                                value="PR-CG"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-CR"
                                id="PR-CR"
                                value="PR-CR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-BY"
                                id="PR-BY"
                                value="PR-BY"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-BQ"
                                id="PR-BQ"
                                value="PR-BQ"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-BC"
                                id="PR-BC"
                                value="PR-BC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AR"
                                id="PR-AR"
                                value="PR-AR"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AC"
                                id="PR-AC"
                                value="PR-AC"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AN"
                                id="PR-AN"
                                value="PR-AN"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AI"
                                id="PR-AI"
                                value="PR-AI"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AB"
                                id="PR-AB"
                                value="PR-AB"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AL"
                                id="PR-AL"
                                value="PR-AL"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AD"
                                id="PR-AD"
                                value="PR-AD"
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
                                :v-model="selected"
                                name="map"
                                ref="PR-AJ"
                                id="PR-AJ"
                                value="PR-AJ"
                              />Adjuntas</label
                            >
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- end of amcharts rinp -->
        </div>
      </div>
    </form>
  </div>
</template>

<script>
// axios imports
import axios from "axios";
// amcharts imports

import * as am4core from "@amcharts/amcharts4/core";
import * as am4maps from "@amcharts/amcharts4/maps";
// import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import am4geodata_puertoRicoHigh from "@amcharts/amcharts4-geodata/puertoRicoHigh";
// am4core.useTheme(am4themes_animated)
// Free SVG stand alone component
// import MunicipalityMap from "../components/MunicipalityMap";
// import MunicipalityList from "../components/MunicipalityList.vue";
// default exports

// RAW JS for amcharts because nobody works it with vue 3

let map = am4core.create("mapchart", am4maps.MapChart);
map.geodata = am4geodata_puertoRicoHigh;
map.projection = new am4maps.projections.Miller();
let polygonSeries = map.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;

// Configure Template
let polygonTemplate = polygonSeries.mapPolygons.template;
polygonTemplate.tooltipText = "{name}";
polygonTemplate.fill = am4core.color("#74B266");

// Create hover state for the map
let hoverState = polygonTemplate.states.create("hover");
hoverState.properties.fill = am4core.color("#367B25");

// Zooom Controls for the map
map.seriesContainer.wheelable = false;
map.seriesContainer.draggable = false;
map.maxZoomLevel = 1;

// configuration for active state in map.
let activeState = polygonTemplate.states.create("active");
activeState.properties.fill = am4core.color("#FF0000");
let tempArray = [];

// event to switch active state.
// polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);
polygonTemplate.events.on("hit", function (ev) {
  let clickedMapID = ev.target.dataItem.dataContext;
  // Create an event to toggle "active" state
  ev.target.isActive = !ev.target.isActive;
  console.log(clickedMapID.id + " " + ev.target.isActive);
  if (ev.target.isActive === true) {
    console.log("The checkbox for " + clickedMapID.name);
    // fucnction call with clickedMapID.id as an argument
    tempArray.push(clickedMapID.id);
    console.log("So far you've selected: " + tempArray);
    document.getElementById(clickedMapID.id).checked = true;
  } else {
    console.log("deactivated" + clickedMapID.name);
    // selected[clickedMapID.name]
    for (let index = 0; index < tempArray.length; index++) {
      if (tempArray[index] === clickedMapID.id) {
        tempArray.splice(index, 1);
      }
    }
    console.log("So far you've selected: " + tempArray);
    document.getElementById(clickedMapID.id).checked = false;
  }
});
// Endo of struggle-o

export default {
  name: "InitialForm",
  components: {
    // MunicipalityMap,
    // MunicipalityList,
  },
  data() {
    return {
      report: {},
      selected: this.tempArray,
      municipality: String,
      map: am4core.create("other-map", am4maps.MapChart),
    };
  },
  computed: {
    selectedMunicipalitiesComp() {
      let selectedMunicipalitiesComp = [];
      selectedMunicipalitiesComp = this.tempArray;
      return selectedMunicipalitiesComp;
    },
    mapData() {
      return this.map;
    },
  },
  watch: {
    // selected(newArray, oldArray){
    // }
  },
  methods: {
    // TODO: Make sure that this has the parts it needs to process report objects properly
    postReport(report) {
      axios
        .post(`/api/report-create/`, report)
        .then((report) => {
          this.response = report;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    mapConfig() {
      this.map.geodata = am4geodata_puertoRicoHigh;
      this.map.projection = new am4maps.projections.Miller();
      let polygonSeries = this.map.series.push(new am4maps.MapPolygonSeries());
      polygonSeries.useGeodata = true;

      // Configure Template
      let polygonTemplate = polygonSeries.mapPolygons.template;
      polygonTemplate.tooltipText = "{name}";
      polygonTemplate.fill = am4core.color("#74B266");

      // Create hover state for the map
      let hoverState = polygonTemplate.states.create("hover");
      hoverState.properties.fill = am4core.color("#367B25");

      // Zooom Controls for the map
      this.map.seriesContainer.wheelable = false;
      this.map.seriesContainer.draggable = false;
      this.map.maxZoomLevel = 1;

      // configuration for active state in this.map.
      let activeState = polygonTemplate.states.create("active");
      activeState.properties.fill = am4core.color("#FF0000");
      let tempArray = [];

      // event to switch active state.
      // polygonTemplate.events.on("hit", this.appendToMunicipalitiesList);
      polygonTemplate.events.on("hit", function (ev) {
        let clickedMapID = ev.target.dataItem.dataContext;
        // Create an event to toggle "active" state
        ev.target.isActive = !ev.target.isActive;
        console.log(clickedMapID.id + " " + ev.target.isActive);
        if (ev.target.isActive === true) {
          console.log("The checkbox for " + clickedMapID.name);
          // fucnction call with clickedMapID.id as an argument
          tempArray.push(clickedMapID.id);
          console.log("So far you've selected: " + tempArray);
          document.getElementById(clickedMapID.id).checked = true;
        } else {
          console.log("deactivated" + clickedMapID.name);
          // selected[clickedMapID.name]
          for (let index = 0; index < tempArray.length; index++) {
            if (tempArray[index] === clickedMapID.id) {
              tempArray.splice(index, 1);
            }
          }
          console.log("So far you've selected: " + tempArray);
          document.getElementById(clickedMapID.id).checked = false;
        }
      });
    },
  },

  mounted: function () {
    // Setting the Doc Tittle
    document.title = "Formulario de Reporte Inicial";
  },
};

// dropdown configurations
</script>
<style scoped>
#mapchart {
  width: 100%;
  height: 400px;
}

#municipality-talbe {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
