import { createApp } from "vue";
import { createStore } from "vuex";
import router from "./router";

// import { io } from "socket.io-client";

import App from "./App.vue";
const store = createStore({
  state() {
    return {
      state: null,
    };
  },
});
const app = createApp(App);

app.use(store);
app.use(router);
// app.config.globalProperties.$socket = io("https://services.peikai.pii.at/", {
//   path: "/OIP-Server/",
// });
app.mount("#app");
