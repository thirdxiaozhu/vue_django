<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>常规管理</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">课程管理</el-breadcrumb-item>
                    </el-breadcrumb>
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
                                <el-select v-model="functionselected" filterable placeholder="请选择课程类型" style="width: 80%;" @change="filterlist">
                                    <el-option v-for="item in functions" :key="item.id" :label="item.name"
                                        :value="item.id" >
                                    </el-option>
                                </el-select>
                            </el-col>
                            <el-col :span="7">
                                <el-select v-model="electiveselected" filterable placeholder="是否选修" style="width: 80%;" @change="classChange()">
                                    <el-option v-for="item in iselective" :key="item.value" :label="item.label"
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
                <el-table :data="tableData" style="width: 100%" ref="table">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                                                    <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
<!--                             <span>{{scope.$index + 1}}</span> -->
                        </template>
                    </el-table-column>
                    <el-table-column prop="cou_id" label="课程号" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="课程名称" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="classhour" label="总学时" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="college" label="开课学院" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="function" label="课程类型" width="150" align="center">
                    </el-table-column>
                    <el-table-column prop="elective" label="是否选修" width="150" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="primary"
                                @click="handleEdit(scope.$index, scope.row);drawer=true">详细</el-button>
                        </template>
                    </el-table-column>
                </el-table>

                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction"
                    :before-close="handleClose" ref="infodrawer" size="50%">
                    <span style>
                        <Vcoursedraw style="margin-top: 5%;" :cou_id="operating_id" :drawer="ObjDrawer" :ifadd="ifadd" @judgeOptions="judgeOptions">
                        </Vcoursedraw>
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
    import Vcoursedraw from './Vcoursedraw'
    import { filterCourses, getCourses} from "@/api/axioses4stu"
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
            this.stu_id = this.$store.state.userid
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
            //编辑学生初始化
            handleEdit(index, row) {
                this.operating_id = row.cou_id;
                this.operating_name = row.name;
                this.title = "正在浏览" + this.operating_id + " " + this.operating_name +"的课程信息";
            },
            initList(){
                const data4cou  = {
                    type: 1,
					stu_id: this.stu_id,
                    currentpage : this.pages.page
                };
                var that = this;
                getCourses(data4cou).then(res =>{
                    if(res.data.code === 1000){
                        that.functions = res.data.functions;
                        that.tableData = res.data.courselist;
						that.functions = res.data.functions;
                        that.pages.total = res.data.total;
						console.log(that.tableData);
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
                const param = {
                    'function': this.functionselected,
                    'iselecitve': this.electiveselected,
                    'currentpage': this.pages.page,
					'stu_id': this.stu_id,
                };
                var that = this;
                filterCourses(param).then(res => {
                    if(res.data.code === 1000){
                        that.tableData = res.data.courselist;
                        that.pages.total = res.data.total;
                    }
                })
            }
        },

        components: {
            Vcoursedraw,
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