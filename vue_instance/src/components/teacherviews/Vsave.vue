<template>
    <div>
        <el-container>
        <el-header style="height: 40px;" :span="5">
            <el-col :span="10">
                <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item>消息处理</el-breadcrumb-item>
                    <el-breadcrumb-item style="font-weight: bold;">收件箱</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
        </el-header>
            <el-main>
                <el-table :data="tableData" style="width: 100%" ref="refTable" tooltip-effect="dark" highlight-current-row row-key="id"
                    lazy @row-click="clickTable" :row-class-name="tableRowClassName">
                    <el-table-column type="expand" width="1">
                        <template slot-scope="props">
                            <div class="sub-title">标题</div>
                            <el-input type="text" v-model="currentrow.title" disabled>
                            </el-input>
                            <div class="sub-title">正文</div>
                            <el-input type="textarea" rows="4"  v-model="currentrow.content" disabled>
                            </el-input>
                            <div class="sub-title">回复</div>
                            <el-input type="textarea" rows="4"  v-model="currentrow.reply" :disabled="currentrow.disabled">
                            </el-input>
                            <el-col align="center">
                                <el-button type="success" row="" @click="onConfirm()" :disabled="currentrow.disabled">确认
                                </el-button>
                                <el-button type="danger" row="" @click="onReject()" :disabled="currentrow.disabled">驳回
                                </el-button>
                            </el-col>
                        </template>
                    </el-table-column>
                    <el-table-column prop="fromwho" label="发件人"  align="center">
                    </el-table-column>
                    <el-table-column prop="gettime" label="发送时间"  align="center">
                    </el-table-column>
                    <el-table-column prop="messagetype" label="消息类型"  align="center" >
                    </el-table-column>
                    <el-table-column prop="title" label="标题"  align="center" >
                    </el-table-column>
                    <el-table-column prop="isFinished" label="是否完成"  align="center" >
                    </el-table-column>
                    <el-table-column prop="finishtime" label="完成时间"  align="center" >
                    </el-table-column>
                    <el-table-column prop="result" label="处理结果"  align="center" >
                    </el-table-column>
                </el-table>
            
            </el-main>
            <el-footer>
                <el-pagination
                    @current-change="initSaveList()"
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
    import { getSavelist,replyMessage,rejectMessage } from "@/api/axioses4tea"
    export default {
        name: 'Vteachercourse',
        data() {
            return {
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                tableData: [],
                currentid: "",
                currentindex: "",
                pages: {
                    page: 1,
                    /*如果需要修改size,不仅要在这里面更改，在page.py里也要更改*/
                    size: 3,
                    total: 1000,
                },
                reply: "",
                tea_id: "",
            }
        },
        mounted: function () {
            this.tea_id = this.$store.state.userid
            this.initSaveList()
        },
        methods: {
            //初始化列表以及选项
            initSaveList(){
                var that = this;
                getSavelist({ 'tea_id': this.tea_id, 'currentpage': this.pages.page }).then(res =>{
                    if(res.data.code === 1000){
                        that.tableData = res.data.messages;
                        that.pages.total = res.data.total;
                        that.tableData.forEach(element => {
                            element.gettime = element.gettime.replace(/T/g, ' ').replace(/Z/g, '')
                            element.finishtime = element.finishtime.replace(/T/g, ' ').replace(/Z/g, '')
                            if(element.isFinished == "是"){
                                element.disabled = true;
                            }else{
                                element.disabled = false;
                            }
                        });
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
            },
            clickTable(row, index, e) {
                /*展开行的手风琴效果*/
                let $table = this.$refs.refTable;
                this.tableData.map((item) => {
                    if (row.id != item.id) {
                        $table.toggleRowExpansion(item, false);
                    }
                })
                $table.toggleRowExpansion(row)
                /*row.id存的是课程的id*/
                this.currentid = row.id;
                this.currentindex = row.index;
                this.currentrow = row;
            },
            tableRowClassName ({row, rowIndex}) {
                row.index = rowIndex;
            },
            onConfirm(){
                console.log(this.currentid)
                var that = this;
                const data = {
                    'reply': this.reply,
                    'id': this.currentid,
                }
                replyMessage(data).then(res => {
                    if(res.data.code === 1000){
                        this.$message({
                            message: '回复成功', 
                            type: 'success'
                        });
                        this.initSaveList();
                        this.currentrow.disabled = true
                    }
                })
            },
            onReject(){
                var that = this;
                const data = {
                    'reply': this.reply,
                    'id': this.currentid,
                }
                rejectMessage(data).then(res => {
                    if(res.data.code === 1000){
                        this.$message({
                            message: '驳回成功', 
                            type: 'success'
                        });
                        this.initSaveList();
                        this.currentrow.disabled = true
                    }
                })
            }
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