<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>常规管理</el-breadcrumb-item>
                        <el-breadcrumb-item>课程管理</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">排课信息</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
                <el-col :span="3" style="margin-top: 10px; float: right;">
                    <el-button type="success" @click="addRoom">安排课程</el-button>
                </el-col>
                <el-col :span="5" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-row style="margin-top: 2%;">
                    <el-col :span="8">
                        <el-select v-model="buildingselected" filterable placeholder="请选择教学楼" style="width: 80%;"
                            @change="filterlist">
                            <el-option v-for="item in buildings" :key="item.id" :label="item.name" :value="item.id">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="8">
                        <el-input placeholder="请输入教室" v-model="capacity" style="width: 80%;" @blur="filterlist"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <el-select v-model="dayselected" filterable placeholder="请选择日期" style="width: 80%;"
                            @change="filterlist">
                            <el-option v-for="item in days" :key="item.id" :label="item.name" :value="item.id">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="8">
                        <el-select v-model="dayselected" filterable placeholder="请选择时间段" style="width: 80%;"
                            @change="filterlist">
                            <el-option v-for="item in days" :key="item.id" :label="item.name" :value="item.id">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="8">
                        <el-input placeholder="请输入教师姓名" v-model="capacity" style="width: 80%;" @blur="filterlist"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <el-button @click="clearOptions">清空输入</el-button>
                    </el-col>
                </el-row>
                </el-collapse>
                <el-table :data="tableData" style="width: 100%" ref="table">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="name" label="教室位置" width="230" align="center">
                    </el-table-column>
                    <el-table-column prop="capacity" label="教室容量" width="230" align="center">
                    </el-table-column>
                    <el-table-column prop="function" label="教室类型" width="230" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary" @click="handleEdit(scope.$index, scope.row);drawer=true">编辑
                            </el-button>
                            <el-button size="medium" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            <!--                         <el-button size="medium" type="primary" @click="drawer=true">编辑</el-button> -->
                        </template>
                    </el-table-column>
                </el-table>
            
                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction" :before-close="handleClose"
                    ref="infodrawer">
                    <span>
                        <Vroomdraw :roomname="operating_name" :drawer="ObjDrawer" :ifadd="ifadd" @judgeOptions="judgeOptions">
                        </Vroomdraw>
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
    import Vroomdraw from './Vroomdraw'
    import { getRooms,filterroomlist } from "@/api/axioses"
    export default {
        name: 'Vroomlist',
        data() {
            return {
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                tableData: [],
                pages: {
                    page: 1,
                    size: 3,
                    total: 1000,
                },
                operating_id: 0,
                operating_name: 0,
                drawer: false,
                ifadd : false, //是否是“添加学生"选项
                direction: 'rtl',
                buildings: {},
                functions: {},
                buildingselected: '',
                functionselected: '',
                capacity: '',
            }
        },
        mounted: function () {
            this.initList()
        },
        methods: {
            //初始化学生列表
            handleCurrentChange() {
                this.filterlist()
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
                this.operating_name = row.name;
                this.ifadd = false;
                this.title = "正在编辑 " + this.operating_name +" 教室的信息";
            },
            //添加学生初始化
            addRoom(){
                this.title = "正在添加学生信息";
                this.operating_id = 0;
                this.ifadd = true;
                this.drawer = true;
            },
            //初始化列表以及选项
            initList(){
                const data4room  = {
                    type: 1,
                    currentpage : this.pages.page
                };
                var that = this;
                getRooms(data4room).then(res =>{
                    console.log(res)
                    if(res.data.code === 1000){
                        that.buildings = res.data.buildings;
                        that.functions = res.data.functions;
                        that.tableData = res.data.roomlist;
                        that.pages.total = res.data.total;
                    }
                })
            },
            clearOptions(){
                this.buildingselected='' ;
                this.functionselected='' ;
                this.capacity='';
                this.initList();
            },
            filterlist(){
                const param = {
                    'building': this.buildingselected,
                    'function': this.functionselected,
                    'capacity': this.capacity,
                    'currentpage': this.pages.page
                }
                var that = this;
                filterroomlist(param).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.roomlist;
                        that.pages.total = res.data.total;
                    }
                })
            }
        },

        components: {
            Vroomdraw
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