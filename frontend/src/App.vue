<template>
  <div class="holder">
    <State :state="state" />
    <Controls :state="state" />
  </div>
</template>

<script>
import { constants } from "./assets/constants";
import State from "./components/State.vue";
import Controls from "./components/Controls.vue";

export default {
  name: "App",
  data() {
    return {
      state: null,
    };
  },
  components: {
    State,
    Controls,
  },
  mounted() {
    this.$socket.on(constants.STATE, (state) => {
      console.log(state);
      this.state = state;
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
