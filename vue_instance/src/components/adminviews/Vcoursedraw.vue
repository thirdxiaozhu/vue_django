<template>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
        <el-form-item label="课程号" prop="stu_id">
            <el-input v-model="form.cou_id" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="课程名称" prop="name">
            <el-input v-model="form.name" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="是否选修" prop="elective">
            <el-radio-group v-model="form.elective">
                <el-radio :label="true">是</el-radio>
                <el-radio :label="false">否</el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="学分" prop="IDnumber">
            <el-input v-model="form.credit" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="总课时" prop="IDnumber">
            <el-input v-model="form.classhour" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="周课时" prop="IDnumber">
            <el-input v-model="form.hourperweek" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="建议修读年份" prop="betyear">
            <el-select v-model="betyearselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in betyear"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开课学院" prop="college">
            <el-select v-model="collegeselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in colleges"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="课程类型" prop="function">
            <el-select v-model="functionselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in functions"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="先修课" prop="pre">
            <el-transfer
              filterable
              filter-placeholder="请输入城市拼音"
              v-model="value"
              :data="data"
              style="text-align: left;"
              >
            </el-transfer>
        </el-form-item>
        <el-form-item>
            <el-button type="success" @click="onSave" :loading="load">保存</el-button>
            <el-button @click="getClick">取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { getLocation, getClass, postSubmit, postAdd, postaddStu, initCourseInfo, getCourse, getCourseOption } from "@/api/axioses"
    export default {
        name: 'Vstudentdraw',
        data() {
            return {
                load: false,
                param: {},
                form: {
                    id: '',
                    stu_id: '',
                    password: '',
                    name: '',
                    sex: '',
                    IDnumber: '',
                    grade: '',
                    birthday: '',
                    entrytime: '',
                    credit: '',
                    outlook: '1',
                    address: [],
                    classes: [],
                },
                betyearselected: 1,
                betyear:{},
                collegeselected: 1,
                colleges:{},
                preselected: 1,
                pre_courses:{},
                functionselected: 1,
                functions:{},
                //级联选择地区
                pre_course_id: [],
                pre_course_name: [],
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
                },
                data: [],
                value: [],
            };
        },
        props: ['drawer', 'cou_id', 'ifadd'],
        mounted: function () {
            this.getOptions();
        },
        methods: {
            //点击保存之后
            onSave() {
                let form = this.form;
                console.log(this.outlookselected , this.gradeselected);
                this.$refs.form.validate((valid) => {
                    this.load = true;
                    var that = this;
                    const param = {
                        outlook: this.outlookselected,
                        grade: this.gradeselected,
                        form: JSON.stringify(this.form)
                    }
                    if (valid) {
                        that.load = false
                        if (this.ifadd == false) { //如果是修改现有
                            postSubmit(param).then(res => {
                                if (res.data.code == "1000") {
                                    console.log(that.drawer);
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
                            postaddStu(param).then(res => {
                                if (res.data.code == "1000") {
                                    console.log(that.drawer);
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
                getCourseOption().then(ret => {
                    if (ret.data.code == 1000) {
                        that.betyear = ret.data.betyear;
                        that.colleges = ret.data.colleges;
                        that.functions = ret.data.functions;
                        that.pre_courses = ret.data.pre_courses;
                        that.pre_course_id = ret.data.pre_course_id;
                        that.pre_course_name = ret.data.pre_course_name;
                        this.initInfo()
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
                if (this.ifadd == false) { //如果是编辑模式，那么就初始化编辑学生的数据
                    var that = this;
                        initCourseInfo({
                            'cou_id': this.cou_id,
                        }).then(ret => {
                        console.log(ret.data)
                        if (ret.data.code === 1000) {
                            //需做一次类型转换，将number转换成string
                            that.betyearselected = ret.data.form.betyear,
                            that.collegeselected = ret.data.form.college,
                            that.preselected = ret.data.form.pre_course
                            that.functionselecte = ret.data.form.function,
                            that.form = ret.data.form;
                            console.log(that.preselected);
                            this.generateData()
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }
            },
            generateData() {
                var data = [];
                this.pre_course_name.forEach((name, index) => {
                    data.push({
                        label: name,
                        key: index,
                        id: this.pre_course_id[index]
                    });
                });
                this.data = data
                console.log(this.data);
            },
            filterMethod(query, item) {
                pre_courses_id = this.pre_courses_id;
                return item.pre_courses_id.indexOf(query) > -1;
            },
            getClick(){
                console.log(this.value);
            }
        },
        components: {
        },
        couputed: {
        }
    }
</script>

<style scoped>

</style>