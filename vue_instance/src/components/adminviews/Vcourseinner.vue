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
                    <el-table-column prop="teacher" label="授课教师" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classroom" label="教室" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classtime" label="时间" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="student" label="选课人数" width="180" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary" @click="handleEdit(scope.$index, scope.row);drawer=true">详情
                            </el-button>
                            <el-button size="medium" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                            <!--                         <el-button size="medium" type="primary" @click="drawer=true">编辑</el-button> -->
                        </template>
                    </el-table-column>
                </el-table>
            
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Vroomdraw from './Vroomdraw'
    import { getScheduled,filterScheduled, getCourseSch } from "@/api/axioses"
    export default {
        name: 'Vroomlist',
        data() {
            return {
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
        props: ['cou_id'],
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
                const data = {
                	cou_id : this.cou_id
                };
                var that = this;
                getCourseSch(data).then(res =>{
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