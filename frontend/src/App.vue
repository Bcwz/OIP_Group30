<template>
  <div class="holder">
    <div class="title">
      {{ current_state }}
    </div>
    <router-view />
    <Controls />
  </div>
</template>

<script>
import { constants } from "./assets/constants";
import Controls from "./components/Controls.vue";

export default {
  name: "App",
  components: {
    Controls,
  },
  computed: {
    current_state() {
      return this.$store.state.state
        ? this.$store.state.state.toUpperCase()
        : "";
    },
  },
  mounted() {
    this.$socket.on(constants.STATE, (state) => {
      console.log(state);
      this.$store.state.state = state;
    });
  },
};
</script>

<style lang="scss">
@import "bulma";

html {
  height: 100vh;
  width: 100vw;
  position: fixed;
}

.holder {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  padding: 10%;
}
</style>
