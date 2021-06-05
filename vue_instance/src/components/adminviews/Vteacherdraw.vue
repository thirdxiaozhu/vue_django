<template>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
        <el-form-item label="教师号" prop="tea_id">
            <el-input v-model="form.tea_id" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="form.password" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
            <el-input v-model="form.name" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
            <el-radio-group v-model="form.sex">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="身份证号" prop="IDnumber">
            <el-input v-model="form.IDnumber" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="生日" prop="birthday">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width: 90%;" value-format="yyyy-MM-dd">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="入职日期" prop="entrytime">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.entrytime" style="width: 90%;" value-format="yyyy-MM-dd">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="政治面貌" prop="outlook">
            <el-select v-model="outlookselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in outlooks"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="职称" prop="title">
            <el-select v-model="titleselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in titles"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="* 籍贯" prop="location">
            <el-cascader
                :placeholder="defaultlocation"
                style="width: 90%"
                v-model="form.address"
                :props="add_cas_props"
                ></el-cascader>
        </el-form-item>
        <el-form-item label="所属学院" prop="college">
            <el-select v-model="collegeselected" placeholder="请选择" style="width: 90%" @change="changeCollege">
                <el-option
                    v-for="item in colleges"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id"
                    >
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="课程组" prop="course">
            <el-select v-model="courseselected" multiple collapse-tags  placeholder="请选择" style="width: 90%;">
                <el-option v-for="item in courses" :key="item.id" :label="item.name" :value="item.id" >
                </el-option>
            </el-select>
        </el-form-item>
            <el-button type="success" @click="onSave()" :loading="load">保存</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { getLocation, getCourse , postTeacherSubmit, postAdd, postaddTea ,initTeacherinfo, editTeacherOptions, changeTeaCollege} from "@/api/axioses"
    export default {
        name: 'Vteacherdraw',
        data() {
            return {
                load: false,
                param: {},
                form: {
                    id: '',
                    tea_id: '',
                    password: '',
                    name: '',
                    sex: '',
                    IDnumber: '',
                    birthday: '',
                    entrytime: '',
                    outlook: '1',
                    address: [],
                },
                defaultlocation: "",
                //年级
                colleges: [],
                collegeselected: 1,     //默认值，一定要是字符串！！！！
                //政治面貌
                outlooks: [],
                outlookselected: 1,
                //职称
                titles: [],
                titleselected: 1,
                //教师所属课程组
                courses: [],
                courseselected: [],     //默认值，一定要是字符串！！！！
                //级联选择地区
                add_cas_props: {
                    lazy: true,
                    lazyLoad(node, resolve) {
                        const level = node.level;
                        //请求参数
                        const requestData = {};

                        if (level === 0) {  //国家
                            requestData.type = "country";
                        } else if (level === 1) { //省份
                            requestData.type = "province";
                            requestData.country_id = node.value;
                        } else if (level === 2) { //城市
                            requestData.type = "city";
                            requestData.province_id = node.value;
                        }
                        //省市区接口
                        getLocation(requestData).then(res => {
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
        props: ['drawer', 'tea_id', 'ifadd'],
        mounted: function () {
            this.getOptions();
            this.initInfo();
        },
        methods: {
            //点击保存之后
            onSave() {
                let form = this.form;
                this.$refs.form.validate((valid) => {
                    this.load = true;
                    var that = this;
                    const param = {
                        outlook: this.outlookselected,
                        college: this.collegeselected,
                        courses: this.courseselected,
                        title: this.titleselected,
                        form: JSON.stringify(this.form)
                    }
                    if (valid) {
                        that.load = false
                        if (this.ifadd == false) { //如果是修改现有
                            postTeacherSubmit(param).then(res => {
                                if (res.data.code == "1000") {
                                    this.$confirm('保存成功！')
                                        .then(_ => {
                                            //隐藏面板（由于面板是在父组件定义的，这里必须要操作父组件的ref）
                                            that.drawer.infodrawer.hide();
                                            //重新通过initList获取父组件的表格：
                                            this.$emit('judgeOptions');
                                        })
                                        .catch(_ => { });
                                }
                                else {
                                    this.$alert(res.data.error, "错误", {
                                        confirmButtonText: '确定'
                                    })
                                }
                            })
                        } else { //如果是新建
                            postaddTea(param).then(res => {
                                if (res.data.code == "1000") {
                                    this.$confirm('保存成功！')
                                        .then(_ => {
                                            that.drawer.infodrawer.hide();
                                            this.$emit('judgeOptions');
                                        })
                                        .catch(_ => { });
                                }
                                else {
                                    this.$alert(res.data.error, "错误", {
                                        confirmButtonText: '确定'
                                    })
                                }
                            })
                        }
                    } else {
                        that.load = false
                        this.$alert("请按照规定填写数据", '错误', {
                            confirmButtonText: '确定'
                        })
                    }
                })
            },
            getOptions() {
                var that = this;

                editTeacherOptions().then(ret => {
                    if (ret.data.code == 1000) {
                        that.outlooks = ret.data.outlooklist;
                        that.colleges = ret.data.collegelist;
                        that.titles = ret.data.titlelist;
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
                if (this.ifadd == false) { //如果是编辑模式，那么就初始化编辑学生的数据
                    var that = this;
                    initTeacherinfo({'tea_id': this.tea_id}).then(ret => {
                        if (ret.data.code === 1000) {
                            //需做一次类型转换，将number转换成string
                            that.collegeselected = ret.data.form.college;
                            that.outlookselected = ret.data.form.outlook;
                            that.titleselected = ret.data.form.title;
                            that.courses = ret.data.courses;
                            that.courseselected = ret.data.courseselected;
                            console.log(that.courseselected);
                            that.defaultlocation = ret.data.country + "/" + ret.data.province + "/" + ret.data.city;
                            that.form = ret.data.form;
                            console.log(that.form);
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }
            },
            changeCollege(){
                changeTeaCollege({'college':this.collegeselected}).then(res =>{
                    var that = this;
                    if( res.data.code == 1000){
                        that.courses = res.data.courses;
                        that.courseselected = []
                    }
                })
            },
        },
        components: {
        },
        couputed: {
        }
    }
</script>

<style scoped>

</style>