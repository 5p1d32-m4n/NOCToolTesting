<template>
  <div class="icon-wrapper">
    <b-icon
      icon="exclamation-circle-fill"
      :variant="variant(report.state)"
    ></b-icon>
  </div>
</template>

<script>
export default {
  data() {
    return {
      report: null,
    }
  },
  computed: {
    variant(state) {
      if (state == 'Initial') {
        return 'danger'
      }
      if (state == 'Update') {
        return 'warning'
      } else {
        return 'success'
      }
    },
  },
}
</script>

<style lang="scss" scoped></style>
