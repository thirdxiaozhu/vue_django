<template>
    <div>
        <el-table :data="tableData" style="width: 100%" row-key="id"  lazy >
            <el-table-column prop="" label="#" width="90" type="index" align="center">
                <template slot-scope="scope">
                    <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
                    <!--                             <span>{{scope.$index + 1}}</span> -->
                </template>
            </el-table-column>
            <el-table-column prop="class_id" label="班级编号" width="360" align="center">
            </el-table-column>
            <el-table-column label="操作" align="center">
                <template slot-scope="scope">
                    <el-button size="medium" type="danger" @click="handleDeleteClass(scope.$index, scope.row)">删除该班级
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    import { getClasses } from "@/api/axioses"
    export default {
        name: 'Vcollege',
        data() {
            return {
                currentid: 1,
                tableData: [],
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
            }
        },
        props: ['content'],
        mounted: function () {
            this.initClassList()
        },
        methods: {
            //初始化学院
            initClassList(){
                const data = {
                    major_id: this.content
                };
                console.log(this.content);
                var that = this;
                getClasses(data).then(res =>{
                    if(res.data.code === 1000){
                        console.log(res.data)
                        that.tableData = res.data.classes;
                    }
                })
            },
            handleDeleteClass(){

            }
        },
    }
</script>

<style scoped>

</style>


<style lang="scss">
    /*1.显示滚动条：当内容超出容器的时候，可以拖动：*/
    .el-drawer__body {
        overflow: auto;
        /* overflow-x: auto; */
    }
     
    /*2.隐藏滚动条，太丑了*/
    .el-drawer__container ::-webkit-scrollbar{
        display: none;
    }
</style>
