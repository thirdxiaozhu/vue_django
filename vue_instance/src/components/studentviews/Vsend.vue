<template>
    <div>
        <el-container>
        <el-header style="height: 40px;" :span="5">
            <el-col :span="10">
                <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item>消息处理</el-breadcrumb-item>
                    <el-breadcrumb-item style="font-weight: bold;">我的发送</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
                <el-col :span="3" style="margin-top: 10px; float: right;">
                    <el-button type="success" @click="sendMessage();drawer=true">发送消息</el-button>
                </el-col>
        </el-header>
            <el-main>
                <el-table :data="tableData" style="width: 100%" ref="table">
                    <el-table-column prop="" label="#" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{scope.$index + 1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="towho" label="收件人"  align="center">
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

                <el-drawer :title="title" v-if="drawer" :visible.sync="drawer" :direction="direction"
                    :before-close="handleClose" ref="infodrawer">
                    <span>
                        <Vstudentdraw :drawer="ObjDrawer"  @judgeOptions="judgeOptions">
                        </Vstudentdraw>
                    </span>
                </el-drawer>
        </el-container>
    </div>
</template>

<script>
    import { getSendlist } from "@/api/axioses4stu"
    export default {
        name: 'Vteachercourse',
        data() {
            return {
				stu_id: "",
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
        mounted: function () {
            this.stu_id = this.$store.state.userid
            this.initSendList()
        },
        methods: {
            //初始化列表以及选项
            initSendList(){
                var that = this;
                getSendlist({ 'stu_id': this.stu_id }).then(res =>{
                    console.log(res)
                    if(res.data.code === 1000){
                        that.tableData = res.data.messages;
                        that.tableData.forEach(element => {
                            element.gettime = element.gettime.replace(/T/g, ' ').replace(/Z/g, '')
                            element.finishtime = element.finishtime.replace(/T/g, ' ').replace(/Z/g, '')
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
            sendMessage(){

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