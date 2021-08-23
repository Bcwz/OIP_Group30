<template>
  <div>
    <div>
      <button
        v-if="!running"
        class="button is-primary is-fullwidth"
        @click="send_signal(1)"
      >
        Start
      </button>
      <button
        v-else
        class="button is-danger is-fullwidth"
        @click="send_signal(2)"
      >
        Stop
      </button>
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
    startSpeechRecognition() {
      let SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

      if (!SpeechRecognition) {
        this.error =
          "Speech Recognition is not available on this browser. Please use Chrome or Firefox";
        return;
      }

      let recognition = new SpeechRecognition();
      recognition.lang = this.lang;
      recognition.interimResults = true;

      recognition.addEventListener("result", (event) => {
        const text = Array.from(event.results)
          .map((result) => result[0])
          .map((result) => result.transcript)
          .join("");
        this.runtimeTranscription = text;
      });

      recognition.addEventListener("end", () => {
        if (this.runtimeTranscription !== "") {
          if (this.runtimeTranscription.includes("start")) {
            this.send_signal(1);
          }
          if (this.runtimeTranscription.includes("stop")) {
            this.send_signal(2);
          }
          console.log(this.runtimeTranscription);
        }
        this.runtimeTranscription = "";
        this.startSpeechRecognition();
      });

      recognition.start();
    },
    set_state(val) {
      this.$store.state.state = val;
    },
    send_signal(val) {
      if (val == 1 && !this.running) {
        alert("Starting");
        this.set_state(constants.CLEANING);
        this.running = true;
      } else if (val == 2 && this.running) {
        alert("Stopping");
        this.set_state(constants.IDLE);
        this.running = false;
      } else {
        alert("Invalid command");
      }
    },
  },
  mounted() {
    this.startSpeechRecognition();
  },
};
</script>

<style></style>
