<template>
  <div class="hello">Testing</div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {},
  mounted() {
    axios
      .get("http://192.168.0.139:5000/values")
      .then((response) => console.log(response));
    console.log("Test");
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
