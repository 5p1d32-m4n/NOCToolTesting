<template>
  <b-row>
    <!-- These are the text input fields (date and time included) -->
    <b-col id="report-specific">
      <!-- NOC Ticket Input -->
      <b-form-group>
        <label for="noc-ticket">Boleto del NOC:</label>
        <b-form-input
          placeholder="E.g: GD09RG8S0E97F7E"
          id="noc-ticket"
          :maxlength="15"
          v-model="reportNOCTicket"
        ></b-form-input>
        <!-- NOC Ticket Input End. -->

        <!-- Third Party Ticket Input -->
        <label for="third-ticket">Boleto de Tercero:</label>
        <b-form-input
          placeholder="E.g: G8S0E97F7E"
          id="third-ticket"
          :maxlength="15"
          v-model="reportThirdPartyTicket"
        ></b-form-input>
        <!-- Third Party Ticket Input End -->

        <!-- Event Date Input -->
        <label for="event-date">Fecha de Averia:</label>
        <b-form-input
          placeholder="E.g: 10/10/2020"
          id="event-date"
          type="date"
          v-model="reportOutageDate"
        ></b-form-input>
        <!-- Event Date Input End. -->

        <!-- Time of Event Input -->
        <label for="event-time">Tiempo de Averia:</label>
        <b-form-input
          placeholder="E.g: 10:10 AM"
          id="event-time"
          type="time"
          v-model="reportOutageTime"
        ></b-form-input>
      </b-form-group>
      <!-- Time of Event Input End.  -->
    </b-col>

    <!-- Beginning of Dropdown lists. -->
    <b-col id="report-repetitive">
      <b-form-group>
        <!-- Service Dropdown lists. -->
        <b-form-group>
          <b-dropdown
            variant="danger"
            text="Servicios Impactados"
            class="m-2 d-grid mt-4"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-row align-h="center">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Servicios</th>
                      <th scope="col">Cantidad Impactda</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(service, index) in services" :key="index">
                      <td>
                        <div>
                          <b-form-checkbox
                            v-model="selectedServices"
                            :value="service"
                            >&nbsp;{{ service }}</b-form-checkbox
                          >
                        </div>
                      </td>
                      <td>
                        <!-- Original number input for client amount -->
                        <div>
                          <input
                            type="number"
                            name="amountSlots"
                            value="0"
                            required
                            min="0"
                            :id="service"
                          />
                        </div>
                        <!-- Radio Button Implementation -->
                      </td>
                    </tr>
                  </tbody>
                </table>
              </b-row>
            </b-dropdown-form>
          </b-dropdown>
        </b-form-group>
        <!-- Cause type dropdown -->
        <b-form-group>
          <b-dropdown
            variant="danger"
            block
            text="Causa de Averia"
            class="m-2 d-grid mt-3"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-row align-h="center">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Causas de Averia:</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(cause, index) in cause" :key="index">
                      <td>
                        <div>
                          <b-form-checkbox
                            v-model="selectedCauses"
                            :value="cause"
                            :id="cause"
                            >&nbsp;{{ cause }}</b-form-checkbox
                          >
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </b-row>
            </b-dropdown-form>
          </b-dropdown>
        </b-form-group>
        <!-- Client dropdown -->
        <b-form-group>
          <b-dropdown
            variant="danger"
            block
            text="Clientes Impactados"
            class="m-2 d-grid mt-3"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-row align-h="center">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Tipo de Cliente:</th>
                      <th scope="col">Cantidad Impactada:</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(client, index) in clients" :key="index">
                      <!-- Checkbox -->
                      <td>
                        <div>
                          <b-form-checkbox
                            v-model="selectedClients"
                            :value="client"
                            >&nbsp;{{ client }}</b-form-checkbox
                          >
                        </div>
                      </td>
                      <!-- Number input. -->
                      <td>
                        <div>
                          <input
                            type="radio"
                            :name="client"
                            value="1000"
                          />1,000+
                          <input
                            type="radio"
                            :name="client"
                            value="5000"
                          />5,000+
                          <input
                            type="radio"
                            :name="client"
                            value="10000"
                          />10,000+
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </b-row>
            </b-dropdown-form>
          </b-dropdown>
        </b-form-group>
        <!-- Outage Type Dropdown -->
        <b-form-group>
          <b-dropdown
            variant="danger"
            block
            text="Tipo de Averias"
            class="m-2 d-grid mt-3"
            menu-class="w-100"
          >
            <b-dropdown-form>
              <b-row align-h="center">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">Tipos de Averias:</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(type, index) in outage_type" :key="index">
                      <td>
                        <div>
                          <b-form-checkbox
                            v-model="selectedOutageTypes"
                            :value="type"
                            >&nbsp;{{ type }}</b-form-checkbox
                          >
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </b-row>
            </b-dropdown-form>
          </b-dropdown>
        </b-form-group>
      </b-form-group>
    </b-col>
  </b-row>
</template>

<script>
import { required } from 'vuelidate/lib/validators'
export default {
  validations: {
    required,
  },
}
</script>

<style scoped></style>
