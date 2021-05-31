<template>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      style="height:100%"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>常规管理</span>
        </template>
          <el-menu-item index="1-1"><router-link to="/admin/studentlist">学籍管理</router-link></el-menu-item>
          <el-menu-item index="1-2"><router-link to="/admin/teacherlist">教籍管理</router-link></el-menu-item>
          <el-menu-item index="1-3"><router-link to="/admin/course">课程管理</router-link></el-menu-item>
          <el-menu-item index="1-4"><router-link to="/admin/test">考试管理</router-link></el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>消息处理</span>
        </template>
          <el-menu-item index="2-1">收信箱</el-menu-item>
          <el-menu-item index="2-2">发送信息</el-menu-item>
          <el-menu-item index="2-3">广播</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>更多功能</span>
        </template>
        <el-submenu index="3-1">
          <template slot="title">
            <span>教学机构变更</span>
          </template>
          <el-menu-item index="3-1-1">可招生学院增加</el-menu-item>
          <el-menu-item index="3-1-2">可招生学院删除</el-menu-item>
          <el-menu-item index="3-1-3">不可招生学院增加</el-menu-item>
          <el-menu-item index="3-1-4">不可招生学院删除</el-menu-item>
        </el-submenu>
        <el-submenu index="3-2">
          <template slot="title">
            <span>专业变更</span>
          </template>
          <el-menu-item index="3-2-1">专业增加</el-menu-item>
          <el-menu-item index="3-2-2">专业删除</el-menu-item>
        </el-submenu>
        <el-submenu index="3-3">
          <template slot="title">
            <span>班级变更</span>
          </template>
          <el-menu-item index="3-3-1">班级增加</el-menu-item>
          <el-menu-item index="3-3-2">班级删除</el-menu-item>
        </el-submenu>
        <el-submenu index="3-4">
          <template slot="title">
            <span>教学地点变更</span>
          </template>
          <el-menu-item index="3-4-1">教学楼变更</el-menu-item>
          <el-menu-item index="3-4-2">教师变更</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">导航四</span>
      </el-menu-item>

    </el-menu>
</template>

<script>
export default {
    name:'Vheader',
    data(){
        return{
          routes:[
            {url:'/', title:'我的首页'},
            {url:'/note', title:'我的笔记'},
          ],
          currentIndex:0,
        }
    },
    methods:{  
      activeHandler(index){   
        //当点击导航栏不同按钮的时候，监听到v-for中的index值，并设置其为currentIndex
        //这样的设置可以用来做class="active"功能
        this.currentIndex = index;
      }
    },

    created(){
      console.log(this.$route) //在console中打印当前的路由信息，

      //刷新页面时，和路由信息中的path属性做比对，如果一致，则将当前遍历赋给currentIndex
      //用以做路由保持
      for(var i = 0; i < this.routes.length ; i++){
        if(this.routes[i].url == this.$route.path){
          this.currentIndex = i;
          return;
        }
      }
    }
}
</script>

<style scoped>
.router-link-active {
  text-decoration: none;
  color:dodgerblue;
}
a{
  text-decoration: none;
  color:black;
}

</style>