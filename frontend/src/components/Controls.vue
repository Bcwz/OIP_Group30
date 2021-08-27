<template>
  <div>
    <div>
      <div>
        <p class="subtitle" v-if="running">Press button to stop</p>
        <p class="subtitle" v-else>Press button to start</p>
      </div>
      <button
        class="button is-primary is-fullwidth"
        :class="{ 'is-primary': !running, 'is-danger': running }"
        @click="send_signal()"
      ></button>
    </div>
    <p>
      <span v-if="error">{{ error }}</span>
    </p>
  </div>
</template>

<script>
import { constants } from "../assets/constants";
export default {
  name: "Controls",
  props: {
    state: String,
  },
  data() {
    return {
      error: false,
    };
  },
  computed: {
    running() {
      return this.state != constants.STOP;
    },
  },
  methods: {
    send_signal() {
      let message = this.running ? constants.STOP : constants.START;
      this.$socket.emit(constants.INSTRUCTION, message);
    },
  },
  mounted() {},
};
</script>

<style></style>
