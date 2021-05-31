<template>
    <button class="btn" :class='currentType'>
        <!-- 插槽分发 -->
        <slot>按钮</slot>
    </button>
</template>

<script>
export default {
    name:"Vbutton",
    data(){
        return{

        }
    },
    props:{
        typed: String
    },
    computed:{
        currentType(){
            return {
                "btn-success":this.typed == "success"? true:false,
                "btn-danger":this.typed == "danger"? true:false
            }
        }
    }
}
</script>

<style scoped>

</style>