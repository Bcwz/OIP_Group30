<template>
  <div class="values columns is-mobile">
    <gauge label="Humidity" :value="humidity" units="%" :max="100" />
    <gauge label="Temperature" :value="temperature" units="°" :max="100" />
  </div>
</template>

<script>
import axios from "axios";
import Gauge from "../components/Gauge.vue";

export default {
  name: "Values",
  components: { Gauge },
  data() {
    return {
      humidity: 0,
      temperature: 0,

      timer: null,
    };
  },
  props: { fps: Number, base_server_url: String },
  methods: {
    get_values() {
      axios.get(this.base_server_url + "/values").then((response) => {
        this.humidity = response.data.humidity;
        this.temperature = response.data.temperature;
      });
    },
  },
  watch: {
    fps: function () {
      clearInterval(this.timer);
      this.timer = setInterval(this.get_values, 1000 / this.fps);
    },
  },
  mounted() {
    this.timer = setInterval(this.get_values, 1000 / this.fps);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.values {
  height: 100%;
}
</style>
