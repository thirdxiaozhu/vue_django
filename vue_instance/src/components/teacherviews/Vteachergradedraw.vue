<template>
    <div>
        <el-container>
            <el-main>
                <el-table :data="tableData" style="width: 100%" ref="table" >
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="stu_id" label="学号" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="姓名" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="Class" label="所在班级" width="150" align="center">
                    </el-table-column>
                    <el-table-column label="成绩" align="center" prop="grade">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.grade" placeholder="请输入" @change="onInputChange(scope.row)"></el-input>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
            <el-footer>
                <el-button size="medium" type="success" @click="checkNull();">确认
                </el-button>
            </el-footer>
        </el-container>

    </div>
</template>

<script>
    import { initStudentList, updateGrade } from "@/api/axioses4tea"
    export default {
        name: 'Vstudentlist',
        data() {
            return {
                tableData: [],
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
                operating_id: 0,
                operating_name: 0,
                grade: '',
            }
        },
        mounted: function () {
            this.initList()
        },
        props: ['relation_id', 'drawer'],
        methods: {
            //初始化学生列表
            initList() {
                var that = this;
                const param = {
					relation_id: this.relation_id
                };
                initStudentList(param).then(ret => {
                    if (ret.data.code === 1000) {
                        that.tableData = ret.data.students
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
            handleUpdate(){
                var that = this;
                const param = {
                    'tableData': JSON.stringify(this.tableData),
                    'relation': this.relation_id
                }
                updateGrade(param).then(res => {
                    if(res.data.code === 1000){
                        this.$message({
                            type: 'success',
                            message: '录入成功!'
                        });
                    }else{
                        this.$message.error({
                            message: '录入失败!' + res.data.error
                        });
                    }
                })
            },
            onInputChange(row){
                if(row.grade > 100 || row.grade < 0){
                    this.$message.error({
                        message: '仅接受位于0-100的正数'
                    });
                    row.grade = ""
                }
            },
            checkNull(){
                for(let i in this.tableData){
                    if(!this.tableData[i].grade){
                        this.$message.error({
                            message: '存在未赋予成绩的学生'
                        });
                        return
                    }
                }
                this.handleUpdate()
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