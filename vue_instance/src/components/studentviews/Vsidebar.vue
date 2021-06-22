<template>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      style="height:100%"
     >
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>常规信息</span>
        </template>
          <el-menu-item index="1-1"><router-link to="/student/info">学籍信息</router-link></el-menu-item>
          <el-menu-item index="1-3"><router-link to="/student/selectcourse">课程信息</router-link></el-menu-item>
          <el-menu-item index="1-4"><router-link to="/student/test">考试信息</router-link></el-menu-item>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>消息处理</span>
        </template>
          <el-menu-item index="2-1">收信箱</el-menu-item>
          <el-menu-item index="2-2">发送信息</el-menu-item>
      </el-submenu>

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