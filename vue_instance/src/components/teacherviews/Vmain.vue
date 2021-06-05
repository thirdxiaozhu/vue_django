<template>
    <div>
        <h3>欢迎您,{{ teaname }}老师</h3>
    </div>
    </template>
    <script>
    export default {
        name:'Vmain',
        data(){
            return{
                teaname:'',
            }
        },
        mounted: function(){
            //vue刚加载时执行的
            //事件需要在vue刚加载时被拉起
            this.initPage();
        },    
        methods:{
            initPage(){
                this.teaname=this.$store.state.username
            }
        }
    }
    </script>
    
    <style scoped>
    
    </style>
    
    