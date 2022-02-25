<template>
  <div class="row mb-2">
    <label v-if="label" for="label" class="col-sm-3 col-form-label">{{
      label
    }}</label>
    <div class="col-sm-8">
      <input
        name="label"
        :value="modelValue"
        @input="updateValue"
        v-bind="$attrs"
        class="form-control"
      />
    </div>
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
    modelValue: [String, Number],
  },
  methods: {
    updateValue(event) {
      this.$emit('input', event.target.value)
    },
  },
}
</script>

<style scoped></style>
