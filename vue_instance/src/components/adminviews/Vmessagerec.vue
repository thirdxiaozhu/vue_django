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
                    <el-table-column prop="cou_id" label="课程号" align="center" width="140">
                    </el-table-column>
                    <el-table-column prop="name" label="课程名称" align="center" width="140">
                    </el-table-column>
                    <el-table-column prop="classhour" label="总学时" align="center" width="140">
                    </el-table-column>
                    <el-table-column prop="college" label="开课学院" align="center" width="140">
                    </el-table-column>
                    <el-table-column prop="function" label="课程类型" align="center" width="140">
                    </el-table-column>
                    <el-table-column prop="testtime" label="考试时间" align="center" width="150">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button type="info" @click="operating_id = scope.row.id; dialogVisible=true" >重新排考
                            </el-button>
                            <el-button type="danger" @click="operating_id = scope.row.id;  dialogVisible_1=true">取消排考
                            </el-button>
                        </template>
                    </el-table-column>

                    <el-dialog title="选择时间" :visible.sync="dialogVisible" width="30%" :before-close="handleClose" >
                        <span>
                            <el-date-picker v-model="value" type="datetime" placeholder="选择日期时间" value-format="yyyy-MM-dd HH:mm:ss">
                            </el-date-picker>
                        </span>
                        <span slot="footer" class="dialog-footer">
                            <el-button @click="dialogVisible = false">取消</el-button>
                            <el-button type="primary" @click="onChoose();dialogVisible = false">确定</el-button>
                        </span>
                    </el-dialog>

                    <el-dialog
  title="提示"
  :visible.sync="dialogVisible_1"
  width="30%"
  :before-close="handleClose">
  <span>这是一段信息</span>
  <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible_1 = false">取 消</el-button>
    <el-button type="primary" @click="dialogVisible_1 = false">确 定</el-button>
  </span>
</el-dialog>
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

    import { initCourseList4testarr, getRelations,updateChoice,getCollegelist4test, getCoursesAsCollege4arr } from '@/api/axioses'
    export default {
        data() {
            return {
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
                colleges: [],
                dialogVisible: false,
                value: '',
                operating_id: '',
                dialogVisible_1: false,
            }
        },
        mounted: function () {
            this.initCollegelist()
            this.initCourse(1)
        },
        methods: {
            initCourse(mod) {
                this.mod = mod
                var that = this;
                const params = {
                    'mod': this.mod,
                    'college':this.collegeselected,
                    'currentpage' : this.pages.page,
                }
                initCourseList4testarr(params).then(res => {
                    if (res.data.code === 1000) {
                        that.form = res.data.form
                        that.pages.total = res.data.total;
                        that.form.forEach(element => {
                            element.testtime = element.testtime.replace(/T/g,' ').replace(/Z/g,'')
                        });
                    }
                })
            },
            onChoose(){
                const data = {
                    'id': this.operating_id,
                    'time': this.value
                }
                updateChoice(data).then(res =>{
                    if(res.data.code === 1000){
                        this.$confirm('安排成功！时间为'+this.value)
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

            handleCurrentChange(){
                this.initCourse(this.mod)
            },
            initCollegelist(){
                getCollegelist4test().then(res =>{
                    if(res.data.code === 1000){
                        this.colleges = res.data.colleges
                    }
                })
            },
            collegeChange(){
                this.mod = 2
                const params = {
                    'mod': this.mod,
                    'college':this.collegeselected,
                    'currentpage': 1,
                }
                var that = this;
                getCoursesAsCollege4arr(params).then(res =>{
                    if(res.data.code === 1000){
                        that.form = res.data.form;
                        that.pages.total = res.data.total;
                    }
                })
            },
            handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      }
        }
    }
</script>

<style scoped>
    .el-table-column {
        width: 120
    }
</style>