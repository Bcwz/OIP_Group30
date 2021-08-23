<template>
  <div class="Gauge column has-text-centered">
    <div class="mask">
      <div class="semi-circle"></div>
      <div :id="label" class="semi-circle--mask"></div>
      <div class="value subtitle">{{ value }} {{ units }}</div>
    </div>
    <div class="label">{{ label }}</div>
  </div>
</template>

<script>
export default {
  name: "Gauge",
  components: {},
  props: {
    label: String,
    value: Number,
    units: String,
    max: Number,
  },
  data() {
    return {};
  },
  watch: {
    value: function () {
      let newVal = (this.value / this.max) * 180;
      // let newVal = ((this.humidity % this.max) / this.max) * 180;
      document.getElementById(this.label).style =
        "-webkit-transform: rotate(" +
        newVal +
        "deg);" +
        "-moz-transform: rotate(" +
        newVal +
        "deg);" +
        "transform: rotate(" +
        newVal +
        "deg);";
    },
  },
  computed: {},
  methods: {},
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
$green: #1abc9c;
$yellow: #f1c40f;
$red: #c0392b;
$blue: #3498db;
$grey: #f2f2f2;

// Gauge
.Gauge {
  height: 60vh;
  margin: 5vmax auto;
}
.mask {
  position: relative;
  overflow: hidden;

  width: 100%;
  height: 100%;
}
.value {
  position: absolute;
  z-index: 10;

  bottom: 0%;
  width: 100%;
}
.semi-circle {
  position: relative;

  display: block;
  width: 98%;
  height: 98%;
  margin-top: 1%;
  margin-left: 1%;

  background: linear-gradient(to right, $green 0%, $yellow 50%, $red 100%);

  border-radius: 50% 50% 50% 50% / 100% 100% 0% 0%;

  &::before {
    content: "";

    position: absolute;
    bottom: 0;
    left: 50%;
    z-index: 2;

    display: block;
    width: 70%;
    height: 70%;
    margin-left: -35%;

    background: #fff;

    border-radius: 50% 50% 50% 50% / 100% 100% 0% 0%;
  }
}

.semi-circle--mask {
  position: absolute;
  top: 0;
  left: 0;

  width: 100%;
  height: 100%;

  background: transparent;

  transform: rotate(0deg) translate3d(0, 0, 0);
  transform-origin: center bottom;
  backface-visibility: hidden;
  transition: all 0.3s ease-in-out;

  &::before {
    content: "";

    position: absolute;
    top: 0;
    left: 0%;
    z-index: 2;

    display: block;
    width: 100%;
    height: 100%;

    background: #f2f2f2;

    border-radius: 50% 50% 50% 50% / 100% 100% 0% 0%;
  }
}
</style>
