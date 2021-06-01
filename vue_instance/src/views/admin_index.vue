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
  import Vheader from '../components/adminviews/Vheader'
  import 'bootstrap/dist/css/bootstrap.min.css'
  import VSidebar from '../components/adminviews/Vsidebar.vue'
  export default {
    name: 'admin_index',
    date() {
      return {
        usertype: '',
      }
    },

    //第二步：挂载
    components: {
      Vheader: Vheader,
      VSidebar,
    },
    created() {
      if (this.$store.state.usertype != "3") {
        this.$alert('当前用户无法操作该页面，请返回登录', '错误', {
          confirmButtonText: '确定',
        })
        this.$router.push({ path: '/login' });
      }
    },
    methods: {
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
