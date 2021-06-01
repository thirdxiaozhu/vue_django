<template>
<div>
    <h3>欢迎您,{{ stuname }}同学</h3>
</div>
</template>
<script>
export default {
    name:'Vmain',
    data(){
        return{
            stuname:'',
        }
    },
    mounted: function(){
        //vue刚加载时执行的
        //事件需要在vue刚加载时被拉起
        this.initPage();
    },    
    methods:{
        initPage(){
            this.stuname=this.$store.state.username
        }
    }
}
</script>

<style scoped>

</style>

