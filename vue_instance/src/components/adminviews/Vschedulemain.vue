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
            </el-header>
            <el-main>
                <el-tabs type="border-card">
                    <el-tab-pane label="已排课程">
                        <Vschedule></Vschedule>
                    </el-tab-pane>
                    <el-tab-pane label="手动排课">
                        <Vschedulemanul></Vschedulemanul>
		            </el-tab-pane>
                    <el-tab-pane label="自动排课">
                        <h4>有待研究！！！</h4>
                    </el-tab-pane>
                </el-tabs>
            </el-main>
            <el-footer>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import Vschedule from './Vschedule'
    import Vschedulemanul from './Vschedulemanul'
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
            Vschedule,
            Vschedulemanul
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