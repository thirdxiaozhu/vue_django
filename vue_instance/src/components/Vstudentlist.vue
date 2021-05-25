<template>
    <div>
        <h3>学籍界面</h3>
        <template>
            <el-table :data="tableData" style="width: 100%">
                <el-table-column prop="" label="#" width="180">
                </el-table-column>
                <el-table-column prop="stu_id" label="学号" width="180">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="180">
                </el-table-column>
                <el-table-column prop="class" label="所在班级" width="180">
                </el-table-column>
                <el-table-column prop="sex" label="性别" width="180">
                </el-table-column>
                <el-table-column prop="operate" label="操作">
                </el-table-column>
            </el-table>
        </template>
    </div>
</template>

<script>
export default {
    name: 'Vstudentlist',
    data(){
        return {
            tableData: []
        }
    },
    mounted: function(){
        this.initList()
    },
    methods:{
        initList: function(){

            var that = this;
            this.$axios.request({
                url:"/api/studentlist",
                method:"GET"
            }).then(function(ret){
                //ajax(axios)发送成功后，响应的内容
                if(ret.data.code === 1000){
                    //this.courseList = ret.data.data
                    //为什么不能按照上面那个写？——因为这里的this指的是$axios里面的this
                    //而不是data里面的，所以要按照下面的
                    that.tableData = ret.data.students
                }else{
                    alert('获取数据失败')
                }
            }).catch(function(ret){

            })
        }
    }
}
</script>

<style scoped>

</style>