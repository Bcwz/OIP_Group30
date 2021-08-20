const vm = {
  delimiters: ["[[", "]]"],
  data() {
    return {
      values: NaN,
    };
  },
  created() {
    setInterval(() => {
      fetch("/pi3/values")
        .then((res) => res.json())
        .then((res) => this.values = res);
    }, 5000);
  },
};

Vue.createApp(vm).mount("#values");
