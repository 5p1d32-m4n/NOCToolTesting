export default {
  totalImpactedClients(clientObject) {
    return Object.keys(clientObject).reduce(
      (sum, values) => sum + parseInt(clientObject[values] || 0),
      0
    )
  },
}
