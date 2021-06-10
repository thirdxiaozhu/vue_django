<template>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
        <el-form-item label="课程号" prop="cou_id">
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
        <el-form-item label="学分" prop="credit">
            <el-input v-model="form.credit" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="总课时" prop="classhour">
            <el-input v-model="form.classhour" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="周课时" prop="hourperweek">
            <el-input v-model="form.hourperweek" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="建议修读年份" prop="betyear">
            <el-select v-model="form.betyear" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in betyear"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开课学院" prop="college">
            <el-select v-model="form.college" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in colleges"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="课程类型" prop="function">
            <el-select v-model="form.function" placeholder="请选择" style="width: 90%">
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
              filter-placeholder="请输入课程代号"
              :filter-method="filterMethod"
              v-model="form.pre_course"
              :data="data"
              style="text-align: left;margin-left: 8%;"
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
    import { getLocation, getClass, postCourseSubmit, postAdd, postaddCou, initCourseInfo, getCourse, getCourseOption } from "@/api/axioses"
    export default {
        name: 'Vstudentdraw',
        data() {
            return {
                load: false,
                param: {},
                form: {
                    priority: 1
                },
                betyearselected: 1,
                betyear:{},
                collegeselected: 1,
                colleges:{},
                preselected: [],
                pre_courses:{},
                functionselected: 1,
                functions:{},
                //级联选择地区
                pre_course_id: [],
                pre_course_cou_id: [],
                pre_course_name: [],
                rules: {
                    cou_id: [
                        { required: true, min: 8, max:8, message: '课程号长度需为8位', trigger: 'blur' }
                    ],
                    name: [
                        { required: true, message: '请输入课程名', trigger: 'blur' },
                    ],
                    sex: [
                        { required: true , message:"请选择是否选修"}
                    ],
                    credit: [
                        { required: true, message: '请输入该课程学分', trigger: 'blur' },
                    ],
                    classhour: [
                        { required: true, message: '请输入该课程总学时', trigger: 'blur' },
                    ],
                    hourperweek: [
                        { required: true, message: '请输入该课程周学时', trigger: 'blur' },
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
                        form: JSON.stringify(this.form)
                    }
                    if (valid) {
                        that.load = false
                        if (this.ifadd == false) { //如果是修改现有
                            postCourseSubmit(param).then(res => {
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
                            postaddCou(param).then(res => {
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
                        that.pre_course_cou_id = ret.data.pre_course_cou_id;
                        that.pre_course_name = ret.data.pre_course_name;
                        console.log(that.pre_course_name);
                        console.log(that.pre_course_id);
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
                            that.form = ret.data.form;
                            console.log(that.form);
                            this.generateData()
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }else{
                    this.generateData()
                }
            },
            generateData() {
                var data = [];
                this.pre_course_name.forEach((name, index) => {
                    data.push({
                        label: name,
                        key: this.pre_course_id[index],
                        id: this.pre_course_cou_id[index]
                    });
                });
                this.data = data
                console.log(this.data);
            },
            filterMethod(query, item) {
                return item.id.indexOf(query) > -1;
            },
            getClick(){
                console.log(this.form.pre_course);
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