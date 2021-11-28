<template>
    <div>
        <el-form ref="form" :model="form" label-width="120px" :rules="rules">
            <el-form-item label="选择课程/教师" prop="course">
                <el-cascader style="width: 90%" v-model="form.course" :props="cou_cas_props"></el-cascader>
            </el-form-item>
            <el-form-item label="期望人数">
                <el-input v-model="form.capacity" style="width: 90%;"></el-input>
            </el-form-item>
            <el-form-item label="选择时间" prop="timeselected">
                <el-select v-model="form.time" placeholder="请选择" style="width: 90%" multiple>
                    <el-option v-for="item in timelist" :key="item.id" :label="item.name" :value="item.id">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="所在教学楼" prop="buildingselected">
                <el-select v-model="form.building" placeholder="请选择" style="width: 90%">
                    <el-option v-for="item in buildings" :key="item.id" :label="item.name" :value="item.id">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="选择教室" prop="roomselected">
                <el-select v-model="form.rooms" placeholder="仅展示该教学楼在该时间段有空闲的教室！" style="width: 90%"
                    @click.native="getValidRoom()">
                    <el-option v-for="item in rooms" :key="item.id" :label="item.name" :value="item.id">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="success" @click="onSave" :loading="load">保存</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    import { getValidRooms, getCol_Cou, getSchBuilding, postCreateSchedule } from "@/api/axioses"
	export default {
		data() {
			return {
				room: 1,
                buildings: {},
                timelist: {},
                rooms: {},
                load: false,
                param: {},
                form: {
                    course: [],
                },
                defaultlocation: "",
                defaultclass: "",
                //年级
                grades: [],
                gradeselected: 1,     //默认值，一定要是字符串！！！！

                //政治面貌
                outlooks: [],
                outlookselected: 1,
                cou_cas_props: {
                    lazy: true,
                    lazyLoad(node, resolve) {
                        const level = node.level;
                        //请求参数
                        const requestData = {};
                        if (level === 0) {  //学院
                            requestData.type = "college";
                        } else if (level === 1) { //专业
                            requestData.type = "course";
                            requestData.college_id = node.value;
                        } else if (level === 2) { //专业
                            requestData.type = "teacher";
                            requestData.course_id = node.value;
                        }
                        //接口
                        getCol_Cou(requestData).then(res => {
                            resolve(res.data.data)
                        })
                    }
                },
                rules: {
                    stu_id: [
                        { required: true, min: 9, max: 9, message: '学生学号长度需为9位', trigger: 'blur' }
                    ],
                    name: [
                        { required: true, message: '请输入学生姓名', trigger: 'blur' },
                        { min: 2, max: 6, message: '长度在 2 到 6 个字符', trigger: 'blur' }
                    ],
                    sex: [
                        { required: true , message:"请选择性别"}
                    ],
                    IDnumber: [
                        { required: true, message: '请输入身份证号', trigger: 'blur' },
                        { min: 18, max: 18, message: '身份证号长度为18位', trigger: 'blur' }
                    ],
                    birthday: [
                        { required: true, message: '请选择日期', trigger: 'change' }
                    ],
                    entrytime: [
                        { required: true, message: '请选择日期', trigger: 'change' }
                    ],
                }
			}
		},
		mounted() {
            this.initlist();
		},
		methods: {
            initlist(){
                var that = this;
                getSchBuilding().then(res =>{
					if(res.data.code === 1000){
						that.buildings = res.data.buildinglist
                        that.timelist = res.data.timelist
                        console.log(that.buildinglist);
					}
                })
            },
            //获取空闲教室
            getValidRoom(){
                const params = {
                    form: JSON.stringify(this.form)
                }
                var that = this;
				getValidRooms(params).then( res => {
					if(res.data.code === 1000){
						that.rooms = res.data.roomlist
					}
				})
            },
            onSave(){
                const params = {
                    form: JSON.stringify(this.form)
                }
                var that = this;
				postCreateSchedule(params).then( res => {
                    if (res.data.code === 1000) {
                        this.$confirm('保存成功！')
                            .then(_ => {
                                this.$refs['form'].resetFields()
                            })
                            .catch(_ => { });
                    }
                    else{
                        this.$confirm('该教师在此时间段已有排课，请检查！')
                            .then(_ => {
                            })
                            .catch(_ => { });
                    }
				})
            },
		}
	}
</script>
<style>
	.tabletitle-timeline {
		line-height: 18px !important;
	}
</style>