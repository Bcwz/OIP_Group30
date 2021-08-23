<template>
  <div class="holder has-text-centered">
    <router-view />
    <Controls />
  </div>
</template>

<script>
import { constants } from "./assets/constants";
import Controls from "./components/Controls.vue";

export default {
  name: "App",
  data() {
    return {
      title: constants.TITLE,
    };
  },
  components: {
    Controls,
  },
  methods: {},
  computed: {},
  mounted() {},
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
}
</style>
