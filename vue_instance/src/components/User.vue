<template>
  <div class="User">
    <h1>{{ page_info }}</h1>
  </div>
</template>

<script>
export default {
  name: 'User',
  data () {
    return {
      page_info: "fuckyou"
    }
  },
  created(){
    this.$axios.get("/api/test").then(response =>{
      console.log(response.data)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
