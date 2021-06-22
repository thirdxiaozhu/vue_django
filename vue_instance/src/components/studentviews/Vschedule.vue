<template>
    <div>
        <el-container>
            <el-main>
                <el-row>
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
                    <el-table-column prop="course" label="课程名称" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="teacher" label="授课教师" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classroom" label="教室" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="classtime" label="时间" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="student" label="选课人数" width="150" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="danger" @click="handleDelete(scope.$index, scope.row)">退选</el-button>
                            <!--                         <el-button size="medium" type="primary" @click="drawer=true">编辑</el-button> -->
                        </template>
                    </el-table-column>
                </el-table>
            
                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction" :before-close="handleClose"
                    ref="infodrawer">
                    <span>
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
    import { getScheduled,filterScheduled,deleteScheduled } from "@/api/axioses4stu"
    export default {
        name: 'Vroomlist',
        data() {
            return {
                stu_id:this.$store.state.userid,
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
            //初始化列表以及选项
            initList(){
                const data = {
                    type: 1,
                    currentpage : this.pages.page,
                    stu_id: this.stu_id
                };
                var that = this;
                getScheduled(data).then(res =>{
                    console.log(res)
                    if(res.data.code === 1000){
                        that.tableData = res.data.scheduledlist;
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
                    capacity: this.capacity,
                    currentpage: this.pages.page,
                    stu_id: this.stu_id
                }
                var that = this;
                filterScheduled(param).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.scheduledlist;
                        that.pages.total = res.data.total;
                    }
                })
            },
            handleDelete(index, row){
                var that = this;
                const params = {
                    'id':row.id,
                    'stu_id': this.stu_id
                }
                deleteScheduled(params).then(res => {
                    if(res.data.code === 1000){
                        this.$confirm('退选成功！')
                            .then(_ => { this.filterlist() })
                            .catch(_ => { });
                    }
                })
            },
            handleCurrentChange(){
                this.filterlist()
            }
        },

        components: {
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