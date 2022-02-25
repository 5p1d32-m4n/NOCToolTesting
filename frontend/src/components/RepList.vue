<template>
  <b-container fluid>
    <b-table-simple id="reports" striped hover responsive="">
      <b-thead>
        <b-tr>
          <b-th>Boleto del NOC</b-th>
          <b-th>Boleto de Tercero</b-th>
          <b-th>Fecha de Averia</b-th>
          <b-th>Municipios Impactados</b-th>
          <b-th>Tipo de Averia</b-th>
          <b-th>Equipo Impactado</b-th>
          <b-th>Clientes Impactados</b-th>
          <b-th>Causas</b-th>
        </b-tr>
      </b-thead>
      <b-tbody>
        <b-tr v-for="report in reportList" :key="report.noc_ticket">
          <b-td
            ><router-link
              :to="{
                name: nextRoute,
                params: { noc_ticket: report.noc_ticket },
              }"
              >{{ report.noc_ticket }}</router-link
            ></b-td
          >
          <b-td>{{ report.third_party_ticket }}</b-td>
          <b-td>{{ report.date_of_outage }}</b-td>
          <b-td>{{ report.municipalities }}</b-td>
          <b-td>{{ report.outage_type }}</b-td>
          <b-td>
            <div
              v-for="(amount, equipment) in report.equipment"
              :key="equipment.id"
            >
              {{ equipment }}: {{ amount }}
            </div>
          </b-td>
          <b-td>
            <div v-for="(amount, client) in report.clients" :key="client">
              {{ client }}: {{ amount }}
            </div>
          </b-td>
          <b-td>{{ report.causes }}</b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
  </b-container>
</template>

<script>
export default {
  name: 'RepList',
  props: {
    reportList: Array,
    perPage: Number,
    page: Number,
  },
  data() {
    return {}
  },
  methods: {
    nocTicket(value) {
      return `${value.noc_ticket}`
    },
  },
  computed: {
    nextRoute() {
      if (this.$route.name == 'Dashboard') {
        return 'RepDetail'
      }
      if (this.$route.name == 'RepUpdateList') {
        return 'RepUpdate'
      }
      if (this.$route.name == 'RepFinalizeList') {
        return 'RepFinalize'
      }
      if (this.$route.name == 'RepArchive') {
        return 'RepDetail'
      }
      return ''
    },
  },
}
</script>

<style lang="scss" scoped></style>
