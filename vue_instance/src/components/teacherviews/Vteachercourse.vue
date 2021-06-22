<template>
    <div>
        <el-container>
        <el-header style="height: 40px;" :span="5">
            <el-col :span="10">
                <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item>常规信息</el-breadcrumb-item>
                    <el-breadcrumb-item style="font-weight: bold;">课程信息</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-header>
            <el-main>
                <el-table :data="tableData" style="width: 100%" ref="table">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="course" label="课程名称" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classroom" label="教室" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classtime" label="时间" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="student" label="选课人数" width="180" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary" @click="handleEdit(scope.$index, scope.row);drawer=true">查看选修该课学生
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            
                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction" :before-close="handleClose"
                    ref="infodrawer" size="50%">
                    <span>
                        <Vteacoustudraw :relation_id="operating_id" :drawer="ObjDrawer"  @judgeOptions="judgeOptions">
                        </Vteacoustudraw>
                    </span>
                </el-drawer>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Vteacoustudraw from './Vteacoustudraw'
    import { getScheduled } from "@/api/axioses4tea"
    export default {
        name: 'Vteachercourse',
        data() {
            return {
				tea_id: "",
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                tableData: [],
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
            this.tea_id = this.$store.state.userid
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
                this.operating_id = row.id;
                this.title = "正在查看选修该课程的学生";
            },
            //初始化列表以及选项
            initList(){
                var that = this;
                getScheduled({ 'tea_id': this.tea_id }).then(res =>{
                    console.log(res)
                    if(res.data.code === 1000){
                        that.tableData = res.data.relationlist;
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
                    'capacity': this.capacity,
                    'currentpage': this.pages.page
                }
                var that = this;
                filterScheduled(param).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.scheduledlist;
                        that.pages.total = res.data.total;
                    }
                })
            }
        },

        components: {
            Vteacoustudraw
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