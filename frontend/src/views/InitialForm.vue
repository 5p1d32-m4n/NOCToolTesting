<template>
  <b-container fluid>
    <form>
      <!-- First Row of Form (No more than 2 cols per row.) -->
      <b-row>
        <b-col id="report-specific">
          <!-- NOC Ticket Input -->
          <label for="noc-ticket">Taquilla del NOC:</label>
          <b-form-input
            placeholder="E.g: GD09RG8S0E97F7E"
            id="noc-ticket"
          ></b-form-input>
          <!-- NOC Ticket Input End. -->

          <!-- Third Party Ticket Input -->
          <label for="third-ticket">Taquilla de Tercero:</label>
          <b-form-input
            placeholder="E.g: G8S0E97F7E"
            id="third-ticket"
          ></b-form-input>
          <!-- Third Party Ticket Input End -->

          <!-- Event Date Input -->
          <label for="event-date">Fecha de Averia:</label>
          <b-form-input
            placeholder="E.g: 10/10/2020"
            id="event-date"
            type="date"
          ></b-form-input>
          <!-- Event Date Input End. -->

          <!-- Time of Event Input -->
          <label for="event-time">Tiempo de Averia:</label>
          <b-form-input
            placeholder="E.g: 10:10 AM"
            id="event-time"
            type="time"
          ></b-form-input>
          <!-- Time of Event Input End.  -->
        </b-col>

        <!-- Beginning of Dropdown lists. -->
        <!-- TODO: make these checkbox come from the Django Backend -->
        <!-- TODO: add the followed number input for some cases -->
        <b-col id="report-repetitive">
          <!-- Service Dropdown lists. -->
          <b-dropdown
            block
            variant="danger"
            text="Servicios Impactados"
            class="d-block mt-4"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-form-checkbox> Checkme </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
          <hr />
          <!-- Outage type dropdown -->
          <b-dropdown
            variant="danger"
            block
            text="Tipo de Averia"
            class="d-block"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-form-checkbox> Checkme </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
          <hr />

          <!-- Client dropdown -->
          <b-dropdown
            variant="danger"
            block
            text="Clientes Impactados"
            class="d-block"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-form-checkbox> Checkme </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
          <hr />

          <!-- Service Dropdown -->
          <b-dropdown
            variant="danger"
            block
            text="Causa de Averia"
            class="d-block"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-form-checkbox> Checkme </b-form-checkbox>
            </b-dropdown-form>
          </b-dropdown>
          <hr />
        </b-col>
      </b-row>
      <b-row align-h="center">
        <h4>Municipios Impactados:</h4>
      </b-row>
      <b-row>
        <!-- Beginning of Municipality Checkbox. -->
        <b-col>
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
                          id="aj"
                          v-model="selectedMunicipalities"
                          value="Adjuntas"
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
                          id="ad"
                          v-model="selectedMunicipalities"
                          value="Aguada"
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
                          id="al"
                          v-model="selectedMunicipalities"
                          value="Aguadilla"
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
                          id="ab"
                          v-model="selectedMunicipalities"
                          value="Aguas Buenas"
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
                          id="ai"
                          v-model="selectedMunicipalities"
                          value="Aibonito"
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
                          id="an"
                          v-model="selectedMunicipalities"
                          value="Añasco"
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
                          id="ac"
                          v-model="selectedMunicipalities"
                          value="Arecibo"
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
                          id="ar"
                          v-model="selectedMunicipalities"
                          value="Arroyo"
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
                          id="bc"
                          v-model="selectedMunicipalities"
                          value="Barceloneta"
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
                          id="bq"
                          v-model="selectedMunicipalities"
                          value="Barranquitas"
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
                          id="by"
                          v-model="selectedMunicipalities"
                          value="Bayamón"
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
                          id="cr"
                          v-model="selectedMunicipalities"
                          value="Cabo Rojo"
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
                          id="cg"
                          v-model="selectedMunicipalities"
                          value="Caguas"
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
                          id="ca"
                          v-model="selectedMunicipalities"
                          value="Camuy"
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
                          id="cv"
                          v-model="selectedMunicipalities"
                          value="Canóvanas"
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
                          id="cn"
                          v-model="selectedMunicipalities"
                          value="Carolina"
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
                          id="ct"
                          v-model="selectedMunicipalities"
                          value="Cataño"
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
                          id="cy"
                          v-model="selectedMunicipalities"
                          value="Cayey"
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
                          id="cb"
                          v-model="selectedMunicipalities"
                          value="Ceiba"
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
                          id="cl"
                          v-model="selectedMunicipalities"
                          value="Ciales"
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
                          id="cd"
                          v-model="selectedMunicipalities"
                          value="Cidra"
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
                          id="co"
                          v-model="selectedMunicipalities"
                          value="Coamo"
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
                          id="cm"
                          v-model="selectedMunicipalities"
                          value="Comerío"
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
                          id="cz"
                          v-model="selectedMunicipalities"
                          value="Corozal"
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
                          id="cu"
                          v-model="selectedMunicipalities"
                          value="Culebra"
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
                          id="do"
                          v-model="selectedMunicipalities"
                          value="Dorado"
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
                          id="fj"
                          v-model="selectedMunicipalities"
                          value="Fajardo"
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
                          id="fl"
                          v-model="selectedMunicipalities"
                          value="Florida"
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
                          id="gc"
                          v-model="selectedMunicipalities"
                          value="Guánica"
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
                          id="gm"
                          v-model="selectedMunicipalities"
                          value="Guayama"
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
                          id="gl"
                          v-model="selectedMunicipalities"
                          value="Guayanilla"
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
                          id="gb"
                          v-model="selectedMunicipalities"
                          value="Guaynabo"
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
                          id="gr"
                          v-model="selectedMunicipalities"
                          value="Gurabo"
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
                          id="ha"
                          v-model="selectedMunicipalities"
                          value="Hatillo"
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
                          id="ho"
                          v-model="selectedMunicipalities"
                          value="Hormigueros"
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
                          id="hu"
                          v-model="selectedMunicipalities"
                          value="Humacao"
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
                          id="is"
                          v-model="selectedMunicipalities"
                          value="Isabela"
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
                          id="jy"
                          v-model="selectedMunicipalities"
                          value="Jayuya"
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
                          id="jd"
                          v-model="selectedMunicipalities"
                          value="Juana Díaz"
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
                          id="jc"
                          v-model="selectedMunicipalities"
                          value="Juncos"
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
                          id="lj"
                          v-model="selectedMunicipalities"
                          value="Lajas"
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
                          id="lr"
                          v-model="selectedMunicipalities"
                          value="Lares"
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
                          id="lm"
                          v-model="selectedMunicipalities"
                          value="Las Marías"
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
                          id="lp"
                          v-model="selectedMunicipalities"
                          value="Las Piedras"
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
                          id="lz"
                          v-model="selectedMunicipalities"
                          value="Loíza"
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
                          id="lq"
                          v-model="selectedMunicipalities"
                          value="Luquillo"
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
                          id="mt"
                          v-model="selectedMunicipalities"
                          value="Manatí"
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
                          id="mr"
                          v-model="selectedMunicipalities"
                          value="Maricao"
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
                          id="mb"
                          v-model="selectedMunicipalities"
                          value="Maunabo"
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
                          id="mg"
                          v-model="selectedMunicipalities"
                          value="Mayagüez"
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
                          id="mc"
                          v-model="selectedMunicipalities"
                          value="Moca"
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
                          id="mv"
                          v-model="selectedMunicipalities"
                          value="Morovis"
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
                          id="ng"
                          v-model="selectedMunicipalities"
                          value="Naguabo"
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
                          id="nr"
                          v-model="selectedMunicipalities"
                          value="Naranjito"
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
                          id="or"
                          v-model="selectedMunicipalities"
                          value="Orocovis"
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
                          id="pt"
                          v-model="selectedMunicipalities"
                          value="Patillas"
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
                          id="pn"
                          v-model="selectedMunicipalities"
                          value="Peñuelas"
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
                          id="po"
                          v-model="selectedMunicipalities"
                          value="Ponce"
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
                          id="qb"
                          v-model="selectedMunicipalities"
                          value="Quebradillas"
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
                          id="rc"
                          v-model="selectedMunicipalities"
                          value="Rincón"
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
                          id="rg"
                          v-model="selectedMunicipalities"
                          value="Río Grande"
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
                          id="sb"
                          v-model="selectedMunicipalities"
                          value="Sabana Grande"
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
                          id="sa"
                          v-model="selectedMunicipalities"
                          value="Salinas"
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
                          id="sg"
                          v-model="selectedMunicipalities"
                          value="San Germán"
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
                          id="sj"
                          v-model="selectedMunicipalities"
                          value="San Juan"
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
                          id="sl"
                          v-model="selectedMunicipalities"
                          value="San Lorenzo"
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
                          id="ss"
                          v-model="selectedMunicipalities"
                          value="San Sebastián"
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
                          id="si"
                          v-model="selectedMunicipalities"
                          value="Santa Isabel"
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
                          id="ta"
                          v-model="selectedMunicipalities"
                          value="Toa Alta"
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
                          id="tb"
                          v-model="selectedMunicipalities"
                          value="Toa Baja"
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
                          id="tj"
                          v-model="selectedMunicipalities"
                          value="Trujillo Alto"
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
                          id="ut"
                          v-model="selectedMunicipalities"
                          value="Utuado"
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
                          id="va"
                          v-model="selectedMunicipalities"
                          value="Vega Alta"
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
                          id="vb"
                          v-model="selectedMunicipalities"
                          value="Vega Baja"
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
                          id="vq"
                          v-model="selectedMunicipalities"
                          value="Vieques"
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
                          id="vl"
                          v-model="selectedMunicipalities"
                          value="Villalba"
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
                          id="yb"
                          v-model="selectedMunicipalities"
                          value="Yabucoa"
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
                          id="yu"
                          v-model="selectedMunicipalities"
                          value="Yauco"
                        />Yauco</label
                      >
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </b-col>
        <!-- Beginning of Municipality CheckboxEnd. -->

        <!-- Beggingin of SVG Map. -->
        <b-col>
          <div>
            <CheckboxSvgMap
              v-model="selectedMunicipalities"
              :map="PuertoRico"
              @mouseover="pointLocation"
              @mouseout="unpointLocation"
              @focus="focusLocation"
              @blur="blurLocation"
            />
            <div>
              <p class="b-tooltip tool">
                Municipio Apuntado: {{ pointedLocation }}
              </p>
            </div>
          </div>
        </b-col>
        <!-- Portion SVG Map End. -->
      </b-row>
    </form>
  </b-container>
</template>

<script>
import axios from "axios";
import { CheckboxSvgMap } from "vue-svg-map";
import PuertoRico from "../assets/puerto-rico";
import { getLocationName, getSelectedLocationName } from "../utilities";

export default {
  name: "InitialForm",
  components: {
    CheckboxSvgMap,
  },
  data() {
    return {
      report: {},
      selectedMunicipalities: [],
      PuertoRico,
      pointedLocation: null,
      focusedLocation: null,
    };
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
    getServices() {},
    getClients() {},
    getOutageType() {},
    getCause() {},

    // Svg map Checkbox functions for evets.
    pointLocation(event) {
      this.pointedLocation = getLocationName(event.target);
    },
    unpointLocation() {
      this.pointedLocation = null;
    },
    focusLocation(event) {
      this.focusedLocation = getLocationName(event.target);
    },
    blurLocation() {
      this.focusedLocation = null;
    },
    getSelectedLocationName,
  },
  watch: {},
  mounted() {
    document.title = "Formulario de Reporte Inicial";
  },
};

// RAW JS for amcharts because nobody works it with vue 3
</script>
<style scoped>
#municipality-table {
  height: 400px;
  overflow: auto;
  text-align: justify;
}
</style>
<style src="vue-svg-map/dist/index.css"></style>
