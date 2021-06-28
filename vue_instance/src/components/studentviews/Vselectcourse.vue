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
            </el-header>
            <el-main>
                <el-tabs type="border-card" @tab-click="handleClick">
                    <el-tab-pane label="必修课">
                        <Vcompulsory ref="compulsory"></Vcompulsory>
                        <div style="margin-top: 20px">
                            <el-button type="warning" @click="selectOnly()">一键查看必修课</el-button>
                            <el-button type="primary" @click="selectAll()" style="width: 12%;">查看全部</el-button>
                        </div>
                    </el-tab-pane>
                    <el-tab-pane label="选修课">
                        <div style="margin-top: 20px">
                            <el-button @click="toggleSelection()">取消选择</el-button>
                        </div>
		            </el-tab-pane>
                    <el-tab-pane label="我的已选">
                        <Vschedule ref="schedule" ></Vschedule>
		            </el-tab-pane>
                </el-tabs>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Vcompulsory from './Vcompulsory'
    import Vschedule from './Vschedule'
    export default {
        name: 'Vselectcourse',
        data() {
            return {
                ObjDrawer: this.$refs,
                search_text: '',
                title: "",
                innertitle: "",
                tableData: [],
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
        },
        methods: {
            toggleSelection(){

            },
            handleClick(tab,event){
                if(tab.index == 0){
                    this.$refs.compulsory.collegeselected = ''
                    this.$refs.compulsory.initCourse(2)
                }else if(tab.index == 2){
                    this.$refs.schedule.initList()
                }
            },
			selectOnly(){
                this.$refs.compulsory.collegeselected = ''
                this.$refs.compulsory.pages.page = 1
				this.$refs.compulsory.initCourse(1)
			},
			selectAll(){
                this.$refs.compulsory.collegeselected = ''
				this.$refs.compulsory.initCourse(2)
			},
        },

        components: {
            Vcompulsory,
            Vschedule,
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