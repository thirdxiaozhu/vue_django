<template>
  <div class="User">

  <form id="computed">
<!--     <input type="text" v-model="msg"> -->
    <input type="text" v-bind:value="getValue" @input="msgChange"> 
    <input type="number" v-bind:value="getValue" @input="msgChange"> 
    <h3>{{ msg }}</h3>
  </form>
  {{ reverseStr }}
  </div>

</template>

<script>
export default {
  name: 'User',
  data () {
    return {
      msg: "",
    }
  },
  methods:{ //事件对象绑定
    msgChange(e){ //将msgChange事件（更新input内容)绑定到getValue
      this.getValue = e.target.value;
    }
  },
  computed:{
//作为对象
    getValue:{
      set:function(newValue) { //一旦set中的内容更改，马上自动调用get
        this.msg= newValue;
      },
      get: function() {  //默认
        return this.msg;
      }
    }
  },
  created(){
    this.$axios.get("/api/test").then(response =>{
      console.log(response.data)
    })
  },
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
