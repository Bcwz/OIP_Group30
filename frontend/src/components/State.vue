<template>
  <div class="title">
    {{ upper_case_state }}
  </div>
</template>

<script>
import { constants } from "../assets/constants";
export default {
  name: "State",
  props: {
    state: String,
  },
  computed: {
    upper_case_state() {
      if (this.state) {
        if (this.state == constants.STOP) return "";
        return this.state.toUpperCase();
      }
      return "";
    },
  },
};
</script>

<style lang="scss"></style>
