<template>
  <div class="title">
    {{ upper_case_state }}
  </div>
</template>

<script>
export default {
  name: "State",
  props: {
    state: String,
  },
  computed: {
    upper_case_state() {
      return this.state ? this.state.toUpperCase() : "";
    },
  },
};
</script>

<style lang="scss"></style>
