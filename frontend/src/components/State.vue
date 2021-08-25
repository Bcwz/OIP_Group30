<template>
  <div class="title">
    {{ upper_case_state }}
  </div>
</template>

<script>
export default {
  name: "State",
  props: {
    state: null,
  },
  computed: {
    upper_case_state() {
      return state ? state.toUpperCase() : "";
    },
  },
};
</script>

<style lang="scss"></style>
