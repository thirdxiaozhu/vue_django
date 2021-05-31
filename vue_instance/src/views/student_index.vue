<template>
  <div id="app" style="height:100%">
    <Vheader></Vheader>
    <el-row class="tac" style="height:100%">
      <el-col :span="4" style="height:100%">
        <VSidebar></VSidebar>
      </el-col>
      <el-col :span="20">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
//第一步：引入子组件
import Vheader from '../components/studentviews/Vheader'
import 'bootstrap/dist/css/bootstrap.min.css'
import VSidebar from '../components/studentviews/Vsidebar.vue'
export default {
  name: 'admin_index',
  
  //第二步：挂载
  components:{
    Vheader:Vheader,
    VSidebar,
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
