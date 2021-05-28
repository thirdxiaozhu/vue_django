<template>
<div>
    <h3>这是主窗口</h3>
    <Vbutton typed="success">成功！</Vbutton>
    <Vbutton typed="danger">危险！</Vbutton>
    <ul v-for="row in courseList" :key="row">
        <li>{{row.title}}</li>
    </ul>
</div>
</template>
<script>
import Vbutton from './Vbutton'
export default {
  components: { Vbutton },
    name:'Vmain',
    data(){
        return{
            courseList:[
            ],
        }
    },
    mounted: function(){
        //vue刚加载时执行的
        //事件需要在vue刚加载时被拉起
        this.initCourse();

    },    
    methods:{
        initCourse: function(){
            //通过ajax向接口发送请求，并获取课程列表(axios)
    
            var that = this;
            this.$axios.request({
                url:"/api/v1/course",
                method: "GET"
            }).then(function(ret){
                //ajax(axios)发送成功后，响应的内容
                if(ret.data.code === 1000){
                    //this.courseList = ret.data.data
                    //为什么不能按照上面那个写？——因为这里的this指的是$axios里面的this
                    //而不是data里面的，所以要按照下面的
                    that.courseList = ret.data.data
                }else{
                    alert('获取数据失败')
                }
            }).catch(function(ret){
                //发生异常

            })
        }
    }
}
</script>

<style scoped>

</style>

