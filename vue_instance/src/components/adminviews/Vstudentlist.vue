<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>常规管理</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">学籍管理</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
                <el-col :span="3" style="margin-top: 10px; float: right;">
                    <el-button type="success" @click="addStudent">添加学生</el-button>
                </el-col>
                <el-col :span="5" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-collapse >
                    <el-collapse-item title="点击展开筛选面板" name="1" align="center" style="text-align: center;">
                        <el-row>
                            <el-col :span="7">
                                <el-select v-model="collegeselected" filterable placeholder="请选择学院" style="width: 80%;" @change="collegeChange()">
                                    <el-option v-for="item in colleges" :key="item.value" :label="item.label"
                                        :value="item.value" >
                                    </el-option>
                                </el-select>
                            </el-col>
                            <el-col :span="7">
                                <el-select v-model="majorselected" filterable placeholder="请选择专业" style="width: 80%;" @change="majorChange()">
                                    <el-option v-for="item in majors" :key="item.value" :label="item.label"
                                        :value="item.value" >
                                    </el-option>
                                </el-select>
                            </el-col>
                            <el-col :span="7">
                                <el-select v-model="classselected" filterable placeholder="请选择班级" style="width: 80%;" @change="classChange()">
                                    <el-option v-for="item in classes" :key="item.value" :label="item.label"
                                        :value="item.value">
                                    </el-option>
                                </el-select>
                            </el-col>
                            <el-col :span="3">
                                <el-button  @click="clearOptions">清空所选</el-button>
                            </el-col>
                        </el-row>
                    </el-collapse-item>
                </el-collapse>
                <el-table :data="tableData" style="width: 100%" ref="table" v-loading="loading">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                                                    <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
<!--                             <span>{{scope.$index + 1}}</span> -->
                        </template>
                    </el-table-column>
                    <el-table-column prop="stu_id" label="学号" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="姓名" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="Class" label="所在班级" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="sex" label="性别" width="180" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary"
                                @click="handleEdit(scope.$index, scope.row);drawer=true">编辑</el-button>
                            <el-button size="medium" type="danger"
                                @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            <!--                         <el-button size="medium" type="primary" @click="drawer=true">编辑</el-button> -->
                        </template>
                    </el-table-column>
                </el-table>

                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction"
                    :before-close="handleClose" ref="infodrawer">
                    <span>
                        <Vstudentdraw :stu_id="operating_id" :drawer="ObjDrawer" :ifadd="ifadd" @judgeOptions="judgeOptions">
                        </Vstudentdraw>
                    </span>
                </el-drawer>
            </el-main>
            <el-footer>
                <el-pagination
                    @current-change="handleCurrentChange"
                    :current-page.sync="pages.page"
                    :page-size="pages.size"
                    layout="prev, pager, next, jumper"
                    :total="pages.total">
                </el-pagination>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import Vstudentdraw from './Vstudentdraw'
    import { initStudentList,getOrganize, deleteStudent} from "@/api/axioses"
    export default {
        name: 'Vstudentlist',
        data() {
            return {
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                tableData: [],
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
                operating_id: 0,
                operating_name: 0,
                drawer: false,
                ifadd : false, //是否是“添加学生"选项
                direction: 'rtl',
                organization: '',
                colleges: {},
                majors: {},
                classes: {},
                pre: '0',
                collegeselected: '',
                majorselected: '',
                classselected: '',
                loading: true,
            }
        },
        mounted: function () {
            this.initOrganize()
        },
        methods: {
            //初始化学生列表
            initList() {
                var that = this;
                const param = {
                    'currentpage':this.pages.page
                };
                initStudentList(param).then(function (ret) {
                    if (ret.data.code === 1000) {
                        that.tableData = ret.data.students
                        that.pages.total = ret.data.total
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
            handleCurrentChange() {
                this.judgeOptions()
            },
            //关闭抽屉弹出
            handleClose(done) {
                this.$confirm('未进行保存的信息将丢失，是否关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => { });
            },
            handleDelete(index, row) {
                this.$confirm('删除操作不可逆', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    deleteStudent({'stuid': row.stu_id}).then(ret =>{
                        console.log(ret.data.code , typeof(ret.data.code))
                        if (ret.data.code === 1000) {
                            this.$message({
                                type: 'success',
                                message: '删除成功!'
                            });
                            that.judgeOptions();
                        }
                    })
                }).catch(() => {
                    this.$message({
                        type: 'error',
                        message: '已取消删除'
                    });
                });
            },
            //编辑学生初始化
            handleEdit(index, row) {
                this.operating_id = row.stu_id;
                this.operating_name = row.name;
                this.ifadd = false;
                this.title = "正在编辑" + this.operating_id + " " + this.operating_name +"同学的信息";
            },
            //添加学生初始化
            addStudent(){
                this.title = "正在添加学生信息";
                this.operating_id = 0;
                this.ifadd = true;
                this.drawer = true;
            },
            //初始化学院
            initOrganize(){
                const data4org  = {
                    type: 1,
                    pre: this.pre,
                    currentpage : this.pages.page
                };
                var that = this;
                getOrganize(data4org).then(res =>{
                    if(res.data.code === 1000){
                        that.colleges = res.data.data;
                        that.tableData = res.data.students;
                        that.pages.total = res.data.total;
                        that.loading = false;
                    }
                })
            },
            //当学院更改的时候，获取专业，并更新学生列表
            collegeChange(){
                this.majorselected='' //学院改变的时候，专业和班级归零
                this.classselected=''
                const data4org  = {
                    type: 2,
                    pre: this.collegeselected,
                    currentpage : this.pages.page
                };
                var that = this;
                getOrganize(data4org).then(res =>{
                    if(res.data.code === 1000){
                        that.majors = res.data.majors;
                        that.tableData = res.data.students;
                        that.pages.total = res.data.total;
                    }
                })
            },
            majorChange(){
                this.classselected=''
                const data4org  = {
                    type: 3,
                    pre: this.majorselected,
                    currentpage : this.pages.page
                };
                var that = this;
                getOrganize(data4org).then(res =>{
                    if(res.data.code === 1000){
                        that.classes = res.data.classes;
                        that.tableData = res.data.students;
                        that.pages.total = res.data.total;
                    }
                })
            },
            classChange(){
                const data4org  = {
                    type: 4,
                    pre: this.classselected,
                    currentpage : this.pages.page
                };
                var that = this;
                getOrganize(data4org).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.students;
                        that.pages.total = res.data.total;
                    }
                })
            },
            clearOptions(){
                this.collegeselected='' ;
                this.majorselected='' ;
                this.classselected='';
                this.initOrganize();
            },
            judgeOptions(){
                if(this.classselected != ''){
                    this.classChange();
                }
                else if(this.majorselected != ''){
                    this.majorChange();
                }
                else if(this.collegeselected!= ''){
                    this.collegeChange();
                }
                else{
                    this.initOrganize();
                }
            }
        },

        components: {
            Vstudentdraw,
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