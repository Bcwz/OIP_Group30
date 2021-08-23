<template>
  <div class="video">
    <img v-bind:src="'data:image/jpeg;base64,' + video_feed" />
    <div class="subtitle">Live Feed</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Values",
  data() {
    return {
      video_feed: null,

      timer: null,
    };
  },
  props: { fps: Number, base_server_url: String },
  methods: {
    update_video() {
      axios.get(this.base_server_url + "/video_feed", {}).then((response) => {
        this.video_feed = response.data.image;
      });
    },
  },
  watch: {
    fps: function () {
      clearInterval(this.timer);
      this.timer = setInterval(this.update_video, 1000 / this.fps);
    },
  },
  mounted() {
    this.timer = setInterval(this.update_video, 1000 / this.fps);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.video {
  height: 100%;
}
</style>
