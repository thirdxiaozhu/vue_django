<template>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
        <el-form-item label="学号" prop="stu_id">
            <el-input v-model="form.stu_id" style="width: 90%;"></el-input>
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
        <el-form-item label="身份证号" prop="idnumber">
            <el-input v-model="form.idnumber" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="生日" prop="birthday">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width: 90%;">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="入学日期" prop="entryday">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.entryday" style="width: 90%;">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="政治面貌" prop="outlook">
            <el-select v-model="outlookselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in outlooks"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="所在年级" prop="grade">
            <el-select v-model="gradeselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in grades"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="* 所在组织" prop="class">
            <el-cascader
               :placeholder="defaultclass"
               style="width: 90%"
               v-model="form.classes"
               :props="cla_cas_props"
               @change="classChange"
               ></el-cascader>
        </el-form-item>
        <el-form-item label="* 籍贯" prop="location">
            <el-cascader
                :placeholder="defaultlocation"
                style="width: 90%"
                v-model="form.address"
                :props="add_cas_props"
                @change="locationChange"
                ></el-cascader>
        </el-form-item>
        <el-form-item label="绩点">
            <el-input v-model="form.credit" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="success" @click="onSave" :loading="load">保存</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { getLocation, getClass, postSubmit, postAdd} from "@/api/axioses"
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
                    idnumber: '',
                    grade: '',
                    birthday: '',
                    entryday: '',
                    credit: '',
                    outlook: '1',
                    address: [],
                    classes: [],
                },
                defaultlocation: "",
                defaultclass: "",
                //年级
                gradess: [],
                //默认值，一定要是字符串！！！！
                gradeselected: '1',

                //政治面貌
                outlooks: [],
                outlookselected: '1',
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
                cla_cas_props: {
                    lazy: true,
                    lazyLoad(node, resolve) {
                        const level = node.level;
                        //请求参数
                        const requestData = {};
                        if (level === 0) {  //学院
                            requestData.type = "college";
                        } else if (level === 1) { //专业
                            requestData.type = "major";
                            requestData.college_id = node.value;
                        } else if (level === 2) { //班级
                            requestData.type = "class";
                            requestData.major_id = node.value;
                        }
                        //接口
                        getClass(requestData).then(res => {
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
                        { required: true }
                    ],
                    idnumber: [
                        { required: true, message: '请输入身份证号', trigger: 'blur' },
                        { min: 18, max: 18, message: '身份证号长度为18位', trigger: 'blur' }
                    ],
                    birthday: [
                        { required: true, message: '请选择日期', trigger: 'change' }
                    ],
                    entryday: [
                        { required: true, message: '请选择日期', trigger: 'change' }
                    ],
                    outlook: [
                        { required: true, message: '请选择该生政治面貌', trigger: 'change' }
                    ],
                    grade: [
                        { required: true, message: '请选择该生所在年级', trigger: 'change' }
                    ],
/*                     location: [
                        { required: true }
                    ],
                    class: [
                        { required: true }
                    ], */
                }
            }
        },
        props: ['drawer', 'stu_id', 'ifadd'],
        mounted: function () {
            this.getOptions();
            this.initInfo();
            console.log(this.ifadd);
        },
        methods: {
            onSave() {
                let form = this.form;
                console.log(this.form);
                this.$refs.form.validate((valid) => {
                    this.load = true;
                    var that = this;
                    const param = {
                        outlook: this.outlookselected,
                        grade: this.gradeselected,
                        form: JSON.stringify(this.form)
                    }
                    if (valid) {
                        postSubmit(param).then(res => {
                            that.load = false
                            if (res.data.code == "1000") {
                                console.log(that.drawer);
                                this.$confirm('保存成功！')
                                    .then(_ => {
                                        //隐藏面板（由于面板是在父组件定义的，这里必须要操作父组件的ref）
                                        that.drawer.infodrawer.hide();
                                        //重新通过initList获取父组件的表格：
                                        this.$emit('initList');
                                    })
                                    .catch(_ => { });
                            }
                            else {
                                this.$alert(res.data.error, "错误", {
                                    confirmButtonText: '确定'
                                })
                            }
                        })
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

                this.$axios.request({
                    url: "/api/editstuoptions",
                    method: "GET",
                }).then(ret => {
                    if (ret.data.code == 1000) {
                        that.outlooks = ret.data.outlooklist;
                        that.grades = ret.data.gradelist;
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
                if (this.ifadd == false) {
                    var that = this;
                    this.$axios.request({
                        url: "/api/studentinfo",
                        method: "GET",
                        params: {
                            'stu_id': this.stu_id,
                        }
                    }).then(ret => {
                        if (ret.data.code === 1000) {
                            //需做一次类型转换，将number转换成string
                            that.gradeselected = ret.data.form.grade.toString();
                            that.outlookselected = ret.data.form.outlook.toString();
                            that.defaultlocation = ret.data.country + "/" + ret.data.province + "/" + ret.data.city;
                            that.defaultclass = ret.data.college + "/" + ret.data.major + "/" + ret.data.class;
                            that.form = ret.data.form;
                            console.log(that.form);
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }
            },
            locationChange(value) {
                console.log(value.join(","))
                console.log(typeof (this.form.address.join(",")))
                console.log(this.form)
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