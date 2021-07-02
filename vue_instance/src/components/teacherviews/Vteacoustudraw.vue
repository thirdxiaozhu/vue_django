<template>
    <div>
        <el-container>
            <el-main>
                <el-table :data="tableData" style="width: 100%" ref="table">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="stu_id" label="学号" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="姓名" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="Class" label="所在班级" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="sex" label="性别" width="120" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary"
                                @click="handleEdit(scope.$index, scope.row);drawer=true">发送信息</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import { initStudentList } from "@/api/axioses4tea"
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
            }
        },
        mounted: function () {
            this.initList()
        },
        props: ['relation_id'],
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
    .el-drawer__container ::-webkit-scrollbar {
        display: none;
    }
</style>