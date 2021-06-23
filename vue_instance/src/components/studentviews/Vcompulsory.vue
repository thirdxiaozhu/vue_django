<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-select v-model="collegeselected" filterable placeholder="请选择开课学院" style="width: 80%;" @change="collegeChange()">
                        <el-option v-for="item in colleges" :key="item.id" :label="item.name"
                            :value="item.id" >
                        </el-option>
                    </el-select>
                </el-col>
                <el-col :span="10" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-table :data="form" tooltip-effect="dark" highlight-current-row style="width: 100%" row-key="id"
                    ref="refTable" lazy @row-click="clickTable" :row-class-name="tableRowClassName">
                    <el-table-column type="expand" width="1">
                        <template slot-scope="props">
                            <el-table :data="tableData" style="width: 100%" ref="innerTable" :showHeader="false">
                                <el-table-column prop="teacher" label="授课教师" width="200" align="center">
                                </el-table-column>
                                <el-table-column prop="classroom" label="教室" width="200" align="center">
                                </el-table-column>
                                <el-table-column prop="classtime" label="时间" width="200" align="center">
                                </el-table-column>
                                <el-table-column prop="student" label="选课人数" width="200" align="center">
                                </el-table-column>
                                <el-table-column>
                                    <template slot-scope="scope">
                                        <el-button type="success" @click="onChoose(scope.row)" :loading="load">选择该课
                                        </el-button>
                                    </template>
                                </el-table-column>
                            </el-table>
                        </template>
                    </el-table-column>
                    <el-table-column prop="cou_id" label="课程号" align="center" width="220">
                    </el-table-column>
                    <el-table-column prop="name" label="课程名称" align="center" width="220">
                    </el-table-column>
                    <el-table-column prop="classhour" label="总学时" align="center" width="220">
                    </el-table-column>
                    <el-table-column prop="college" label="开课学院" align="center" width="220">
                    </el-table-column>
                    <el-table-column prop="function" label="课程类型" align="center">
                    </el-table-column>
            </el-table>
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
    import { initCourseList, getRelations,updateChoice,getCollegelist } from '@/api/axioses4stu'
    export default {
        data() {
            return {
                stu_id:this.$store.state.userid,
                form: [],
                tableData: [],
                mod: 1,
                selected_rel:[],
                selected_cou:[],
                rel_id: [],
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
                collegeselected: '',
            }
        },
        mounted: function () {
            this.initCollegelist()
            this.initCourse()
        },
        methods: {
            initCourse(mod) {
                this.mod = mod
                var that = this;
                const params = {
                    'mod': this.mod,
                    'stu_id': this.stu_id,
                    'currentpage' : this.pages.page,
                }
                initCourseList(params).then(res => {
                    if (res.data.code === 1000) {
                        this.form = res.data.form
                        that.pages.total = res.data.total;
                    }
                })
            },
            clickTable(row, index, e) {
                /*展开行的手风琴效果*/
                let $table = this.$refs.refTable;
                this.form.map((item) => {
                    if (row.id != item.id) {
                        $table.toggleRowExpansion(item, false)
                    }
                })
                $table.toggleRowExpansion(row)
                /*row.id存的是课程的id*/
                this.currentid = row.id
                this.currentindex = row.index
                console.log(row.id,this.currentindex);
                this.currentrow = row
                const params = {
                    'id':row.id,
                    'currentpage' : this.pages.page,
                }
                var that = this;
                getRelations(params).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.tableData
                        that.rel_id = res.data.rel_id
                        that.pages.total = res.data.total;
                    }
                })
            },
            onChoose(row){
                this.selected_rel.push(row.id)
                this.selected_cou.push(this.currentid)

                const data = {
                    'stu_id':this.stu_id,
                    'id': row.id
                }
                updateChoice(data).then(res =>{
                    if(res.data.code === 1000){
                        this.$confirm('选课成功！')
                            .then(_ => { this.initCourse(this.mod) })
                            .catch(_ => { });
                    }
                    else{
                        this.$confirm('选课失败！')
                            .then(_ => { })
                            .catch(_ => { });
                    }
                })
            },

            //把每一行的索引放进row,这样在row_click的时候，就可以获取到每一行的索引了
            tableRowClassName ({row, rowIndex}) {
                row.index = rowIndex;
            },
            handleCurrentChange(){
                this.initCourse(this.mod)
            },
            initCollegelist(){
                getCollegelist().then(res =>{
                    if(res.data.code === 1000){
                        this.colleges = res.data.colleges
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .el-table-column {
        width: 120
    }
</style>