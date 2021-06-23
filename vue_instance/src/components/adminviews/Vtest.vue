<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>常规管理</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">考试管理</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
                <el-col :span="3" style="margin-top: 10px; float: right;">
                    <el-button type="success" @click="addCourse">添加课程</el-button>
                </el-col>
                <el-col :span="5" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-tabs type="border-card" @tab-click="handleClick">
                    <el-tab-pane label="未安排考试课程">
                        <Vschedule  ref="schedule"></Vschedule>
                    </el-tab-pane>
                    <el-tab-pane label="已安排考试课程" >
                        <Vschedulemanul ref="manul"></Vschedulemanul>
		                </el-tab-pane>
                </el-tabs>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Vcoursedraw from './Vcoursedraw'
    import Vcourseinner from './Vcourseinner'
    import { filterCourseList,initStudentList,getOrganize, deleteCourse, getCourseList} from "@/api/axioses"
    export default {
        name: 'Vcourselist',
        data() {
            return {
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                innertitle: "",
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
                innerDrawer: false,
                ifadd : false, //是否是“添加学生"选项
                direction: 'rtl',
                organization: '',
                colleges: {},
                functions: {},
                collegeselected: '',
                functionselected: '',
                elecitveselected: '',
                iselective: [
                    {
                        'value': 1,
                        'label': '是'
                    },
                    {
                        'value': 0,
                        'label': '否'
                    }
                ]
            }
        },
        mounted: function () {
            this.initList()
        },
        methods: {
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
                    deleteCourse({'cou_id': row.cou_id}).then(ret =>{
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
            judgeOptions(){
                const param = {
                    'college':this.collegeselected,
                    'function': this.functionselected,
                    'iselecitve': this.electiveselected,
                    'currentpage': this.pages.page
                };
                var that = this;
                filterCourseList(param).then(res => {
                    if(res.data.code === 1000){
                        that.tableData = res.data.courselist;
                        that.pages.total = res.data.total;
                    }
                })
            },
            handleClick(tab,event){
                if(tab.index == 0){
                    this.$refs.compulsory.initCourse(2)
                }else if(tab.index == 2){
                    this.$refs.schedule.initList()
                }
            },
			      selectOnly(){
			      	this.$refs.compulsory.initCourse(1)
			      },
			      selectAll(){
			      	this.$refs.compulsory.initCourse(2)
			      },
        },

        components: {
            Vcoursedraw,
            Vcourseinner,
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