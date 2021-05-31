<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5" >
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>常规管理</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">学籍管理</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
                <el-col :span="3" style="margin-top: 10px; float: right;">
                    <el-button type="success">添加学生</el-button>
                </el-col>
                <el-col :span="5" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-collapse v-model="activeNames" @change="handleChange">
                    <el-collapse-item title="点击展开筛选面板" name="1" align="center">
                    </el-collapse-item>
                </el-collapse>
                <el-table :data="tableData" style="width: 100%">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <!--                         <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span> -->
                            <span>{{scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="stu_id" label="学号" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="姓名" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="class" label="所在班级" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="sex" label="性别" width="180" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary"
                                @click="handleEdit(scope.$index, scope.row);drawer=true">编辑</el-button>
                            <!--                         <el-button size="medium" type="primary" @click="drawer=true">编辑</el-button> -->
                        </template>
                    </el-table-column>
                </el-table>

                <el-drawer :title="`正在编辑${operating_id} ${operating_name}同学的信息`" v-if="drawer" :visible.sync="drawer"
                    :direction="direction" :before-close="handleClose">
                    <span>
                        <Vstudentdraw :stu_id="operating_id"></Vstudentdraw>
                    </span>
                </el-drawer>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Vstudentdraw from './Vstudentdraw'
    export default {
        name: 'Vstudentlist',
        data() {
            return {
                tableData: [],
                pages: {
                    page: 1,
                    size: 10,
                    total: 100
                },
                operating_id: 0,
                operating_name: 0,
                drawer: false,
                direction: 'rtl',
            }
        },
        mounted: function () {
            this.initList()
        },
        methods: {
            initList: function () {
                var that = this;
                this.$axios.request({
                    url: "/api/studentlist",
                    method: "GET"
                }).then(function (ret) {
                    //ajax(axios)发送成功后，响应的内容
                    if (ret.data.code === 1000) {
                        //this.courseList = ret.data.data
                        //为什么不能按照上面那个写？——因为这里的this指的是$axios里面的this
                        //而不是data里面的，所以要按照下面的
                        that.tableData = ret.data.students
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
            handleClose(done) {
                this.$confirm('未进行保存的信息将丢失，是否关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => { });
            },
            handleEdit(index, row) {
                this.operating_id = row.stu_id;
                this.operating_name = row.name;
                console.log(this.operating_id, row);
            },
        },

        components: {
            Vstudentdraw,
        }
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