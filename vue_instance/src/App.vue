<template>
  <div id="app" style="height:100%">
    <router-view></router-view>
  </div>
</template>

<script>
//第一步：引入子组件
export default {
  name: 'App',
  
  //第二步：挂载
  components:{
  }
}
</script>

<style>
html,body,#app {
  text-align: center;
  color: #2c3e50;
  height:100%;
}
</style>
