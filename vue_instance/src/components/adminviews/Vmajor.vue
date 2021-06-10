<template>
    <div>
        <el-table highlight-current-row :data="tableData" style="width: 100%" row-key="id" ref="refTable" lazy @row-click="clickTable"  >
            <el-table-column type="expand" width="1">
                <template slot-scope="props">
                    <Vclass :content="currentid"></Vclass>
                </template>
            </el-table-column>
            <el-table-column prop="" label="#" width="90" type="index" align="center">
                <template slot-scope="scope">
                    <span>{{(pages.page - 1) * pages.size + scope.$index + 1}}</span>
                    <!--                             <span>{{scope.$index + 1}}</span> -->
                </template>
            </el-table-column>
            <el-table-column prop="major_id" label="专业编号" width="180" align="center">
            </el-table-column>
            <el-table-column prop="name" label="专业名称" width="180" align="center">
            </el-table-column>
            <el-table-column label="操作" align="center">
                <template slot-scope="scope">
                    <el-button size="small" type="success"
                        @click="handleEditMajor(scope.$index, scope.row);drawer=true" style="width: 15%;">管理</el-button>
                    <el-button size="small" type="primary"
                        @click="handleAddMajor(scope.$index, scope.row);drawer=true">增加下属班级</el-button>
                    <el-button size="small" type="danger" @click="handleDeleteCollege(scope.$index, scope.row)">删除该专业
                    </el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    import Vclass from './Vclass'
    import { getMajors } from "@/api/axioses"
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
        props: ['content'],
        mounted: function () {
            this.initMajorList()
        },
        methods: {
            //初始化学院
            initMajorList(){
                const data = {
                    college_id: this.content
                };
                console.log(this.content);

                var that = this;
                getMajors(data).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.majors;
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

                this.currentid = row.major_id
            },
            handleAddMajor(){

            },
            handleDeleteCollege(){

            }
        },

        components: {
            Vclass,
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
