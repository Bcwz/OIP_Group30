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
      <span>{{ runtimeTranscription }}</span>
      <span v-if="error">{{ error }}</span>
    </p>
  </div>
</template>

<script>
import { constants } from "../assets/constants";
export default {
  name: "Controls",
  props: {
    base_server_url: String,
  },
  data() {
    return {
      error: false,
      runtimeTranscription: "",

      running: false,
    };
  },
  methods: {
    // startSpeechRecognition() {
    //   let SpeechRecognition =
    //     window.SpeechRecognition || window.webkitSpeechRecognition;

    //   if (!SpeechRecognition) {
    //     this.error =
    //       "Speech Recognition is not available on this browser. Please use Chrome or Firefox";
    //     return;
    //   }

    //   let recognition = new SpeechRecognition();
    //   recognition.lang = this.lang;
    //   recognition.interimResults = true;

    //   recognition.addEventListener("result", (event) => {
    //     const text = Array.from(event.results)
    //       .map((result) => result[0])
    //       .map((result) => result.transcript)
    //       .join("");
    //     this.runtimeTranscription = text;
    //   });

    //   recognition.addEventListener("end", () => {
    //     if (this.runtimeTranscription !== "") {
    //       if (this.runtimeTranscription.includes("start")) {
    //         this.send_signal(1);
    //       }
    //       if (this.runtimeTranscription.includes("stop")) {
    //         this.send_signal(2);
    //       }
    //       console.log(this.runtimeTranscription);
    //     }
    //     this.runtimeTranscription = "";
    //     this.startSpeechRecognition();
    //   });

    //   recognition.start();
    // },
    set_state(val) {
      this.$store.state.state = val;
    },
    send_signal() {
      if (!this.running) {
        alert("Starting");
        this.set_state(constants.CLEANING);
        this.running = true;
      } else if (this.running) {
        alert("Stopping");
        this.set_state(constants.IDLE);
        this.running = false;
      }
    },
  },
  mounted() {
    // this.startSpeechRecognition();
  },
};
</script>

<style></style>
