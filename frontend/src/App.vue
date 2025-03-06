<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  setup() {
    
    return {};
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:rgb(80, 9, 23);
  margin-top: 20px;
  margin-left: 30px;
  margin-right: 20px;
  background-color:cadetblue;
  width: 100%;
}
</style>
