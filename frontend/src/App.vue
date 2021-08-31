<template>
  <div class="holder has-background-warning-light">
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
      count: 0,

      states: [
        constants.START,
        constants.WASHING,
        constants.DRYING,
        constants.STERILIZING,
        constants.COMPLETE,
        constants.STOP,
      ],

      interval: null,
    };
  },
  components: {
    State,
    Controls,
  },
  mounted() {
    this.interval = setInterval(() => {
      this.state = this.states[this.count];
      this.count = (this.count + 1) % this.states.length;
    }, 1000);

    // this.$socket.on(constants.STATE, (state) => {
    //   console.log(state);
    //   this.state = state;
    // });
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
