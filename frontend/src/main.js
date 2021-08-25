import { createApp } from "vue";
import { io } from "socket.io-client";

import App from "./App.vue";

const app = createApp(App);

app.config.globalProperties.$socket = io("http://localhost:5000/");
app.mount("#app");
