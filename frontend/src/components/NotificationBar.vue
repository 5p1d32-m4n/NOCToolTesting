<template>
  <div class="notification-bar" :class="notificationTypeClass">
    <p>{{ notification.message }}</p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  props: {
    notification: {
      type: Object,
      required: true,
    },
  },
  computed: {
    notificationTypeClass() {
      return `-text-${this.notification.type}`
    },
  },
  data() {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
      timeout: null,
    }
  },
  methods: {
    ...mapActions('notification', ['remove']),
    showAlert() {
      if (this.notification != null) {
        this.dismissCountDown = this.dismissSecs
      }
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
  },
  mounted() {
    this.showAlert()
    this.timeout = setTimeout(() => this.remove(this.notification), 5000)
  },
  beforeDestroy() {
    clearTimeout(this.timeout)
  },
}
</script>

<style scoped>
.notification-bar {
  margin: 1em 0 1em;
}
</style>
