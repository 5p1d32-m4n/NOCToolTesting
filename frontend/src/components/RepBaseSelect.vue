<template>
  <div class="row mb-2">
    <b-form-group>
      <b-dropdown
        variant="danger"
        block
        :text="computedLabel"
        class="m-2 d-grid mt-3"
        menu-class="w-100"
      >
        <b-dropdown-form>
          <b-row align-h="center">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">{{ computedLabel }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(entry, index) in modelValue" :key="index">
                  <td>
                    <div>
                      <b-form-checkbox
                        v-model="modelValue"
                        :value="modelValue"
                        :id="modelValue"
                        >&nbsp;{{ modelValue }}</b-form-checkbox
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
  </div>
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    label: {
      type: String,
      default: '',
    },
    modelValue: Array,
  },
  methods: {
    updateValue(event) {
      this.$emit('input', event.target.value)
    },
  },
  computed: {
    computedLabel() {
      return `${this.label} de Averia`
    },
  },
  mounted() {},
}
</script>

<style lang="scss" scoped></style>
