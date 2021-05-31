<template>
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="学号">
            <el-input v-model="form.stu_id" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="密码">
            <el-input v-model="form.password" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
            <el-input v-model="form.name" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="性别">
            <el-radio-group v-model="form.sex">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="身份证号">
            <el-input v-model="form.idnumber" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="生日">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width: 90%;">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="入学日期">
            <el-date-picker type="date" placeholder="选择日期" v-model="form.entryday" style="width: 90%;">
            </el-date-picker>
        </el-form-item>
        <el-form-item label="政治面貌">
            <el-select v-model="outlookselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in outlooks"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="所在年级">
            <el-select v-model="optionselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="所在机构">
            <el-cascader
               :placeholder="defaultclass"
               style="width: 90%"
               v-model="form.classes"
               :props="cla_cas_props"
               @change="classChange"
               ></el-cascader>
        </el-form-item>
        <el-form-item label="籍贯">
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
            <el-button type="success" @click="onSave">保存</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import {getLocation, getClass} from "@/api/axioses"
    export default {
        name: 'Vstudentdraw',
        data() {
            return {
                form: {
                    stu_id: '',
                    password: '',
                    name: '',
                    sex: '',
                    idnumber: '',
                    grade: '',
                    birthday: '',
                    entryday: '',
                    credit: '',
                    outlook: '',
                    address: [],
                    classes: [],
/*                     address: '', */
                },
                defaultlocation: "",
                defaultclass: "",
                //年级
                options: [{
                    value: '1',
                    label: '本科一年级'
                }, {
                    value: '2',
                    label: '本科二年级'
                }, {
                    value: '3',
                    label: '本科三年级'
                }, {
                    value: '4',
                    label: '本科四年级'
                }, {
                    value: '5',
                    label: '研究生一年级'
                }, {
                    value: '6',
                    label: '研究生二年级'
                }, {
                    value: '7',
                    label: '研究生三年级'
                }],
                //默认值，一定要是字符串！！！！
                optionselected: '1',

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

                        if(level === 0){  //国家
                            requestData.type = "country";
                        }else if(level === 1){ //省份
                            requestData.type = "province";
                            requestData.country_id = node.value;
                        }else if(level === 2){ //城市
                            requestData.type = "city";
                            requestData.province_id = node.value;
                        } 
                        //省市区接口
                        getLocation(requestData).then(res=>{
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
                        if(level === 0){  //学院
                            requestData.type = "college";
                        }else if(level === 1){ //专业
                            requestData.type = "major";
                            requestData.college_id = node.value;
                        }else if(level === 2){ //班级
                            requestData.type = "class";
                            requestData.major_id = node.value;
                        } 
                        //接口
                        getClass(requestData).then(res=>{
                            resolve(res.data.data)
                        })
                    }
                }
            }
        },
        props: {
            stu_id: String,
        },
        mounted: function () {
            this.getOptions();
            this.initInfo();
        },
        methods: {
            onSave() {
                console.log('submit!');
            },
            getOptions() {
                var that = this;

                this.$axios.request({
                    url: "/api/editstuoptions",
                    method: "GET",
                }).then(ret => {
                    if (ret.data.code == 1000) {
                        that.outlooks = ret.data.outlooklist;
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
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
                        that.optionselected = ret.data.form.grade.toString();
                        that.outlookselected = ret.data.form.outlook.toString();
                        that.defaultlocation = ret.data.country + "/" + ret.data.province + "/" + ret.data.city;
                        that.defaultclass = ret.data.college + "/" + ret.data.major + "/" + ret.data.class;
                        that.form = ret.data.form;
                        console.log(this.form)
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
            locationChange(value) {
                console.log(value.join(","))
                console.log(typeof(this.form.address.join(",")))
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