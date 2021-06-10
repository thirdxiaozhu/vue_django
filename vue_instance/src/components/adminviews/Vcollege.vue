<template>
    <div>
        <el-container>
            <el-header style="height: 40px;" :span="5">
                <el-col :span="10">
                    <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                        <el-breadcrumb-item>首页</el-breadcrumb-item>
                        <el-breadcrumb-item>更多功能</el-breadcrumb-item>
                        <el-breadcrumb-item style="font-weight: bold;">可招生学院管理</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
                <el-col :span="5" style="float: right; margin-top: 10px;">
                    <el-input placeholder="请输入内容" v-model="search_text">
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
            </el-header>
            <el-main>
                <el-table highlight-current-row :data="tableData" style="width: 100%" row-key="id"  ref="refTable" lazy @row-click="clickTable" >
                    <el-table-column type="expand" width="1">
                        <template slot-scope="props">
                            <Vmajor :content="currentid"></Vmajor>
                        </template>
                    </el-table-column>
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
                            <!--                             <span>{{scope.$index + 1}}</span> -->
                        </template>
                    </el-table-column>
                    <el-table-column prop="college_id" label="学院编号" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="学院名称" width="180" align="center">
                    </el-table-column>
                    <el-table-column label="操作" align="center">
                        <template slot-scope="scope">
                            <el-button size="medium" type="success" @click="handleEditCollege(scope.$index, scope.row);drawer=true" style="width: 15%;">管理</el-button>
                            <el-button size="medium" type="primary" @click="handleAddMajor(scope.$index, scope.row);drawer=true">增加下属专业
                            </el-button>
                            <el-button size="medium" type="danger" @click="handleDeleteCollege(scope.$index, scope.row)">删除该学院
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
            <el-footer>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    import Vmajor from './Vmajor'
    import { getColleges } from "@/api/axioses"
    export default {
        name: 'Vcollege',
        data() {
            return {
                currentid: 1,
                tableData: [],
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
            }
        },
        mounted: function () {
            this.initCollegeList()
        },
        methods: {
            //初始化学院
            initCollegeList(){
                const data = {
                    type: 1,
                };
                var that = this;
                getColleges(data).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.colleges;
                        console.log(res.data.colleges);
                    }
                })
            },
            clickTable(row, index, e) {
                /*展开行的手风琴效果*/
                let $table = this.$refs.refTable;
                this.tableData.map((item) => {
                    if (row.id != item.id) {
                        $table.toggleRowExpansion(item, false)
                    }
                })
                $table.toggleRowExpansion(row)

                this.currentid = row.id
            },
            handleAddMajor(){

            },
            handleDeleteCollege(){

            }
        },

        components: {
            Vmajor,
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
