import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import { publicPath } from "../../vue.config";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
];

const router = createRouter({
  base: publicPath,
  history: createWebHistory(process.env.BASE_URL),
  mode: "history",
  routes,
});

export default router;
