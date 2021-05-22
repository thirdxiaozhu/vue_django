<template>
<div>
    <h3>这是主窗口</h3>
    <Vbutton typed="success">成功！</Vbutton>
    <Vbutton typed="danger">危险！</Vbutton>
</div>
</template>
<script>
import Vbutton from './Vbutton'
export default {
  components: { Vbutton },
    name:'Vmain',
    data(){
        return{

        }
    }    
}
</script>

<style scoped>

</style>