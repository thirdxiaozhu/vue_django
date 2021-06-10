<template>
    <div>
        <el-header style="height: 40px;" :span="5">
            <el-col :span="10">
                <el-breadcrumb separator="/" style="margin-top: 20px; font-size:large;">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item>学籍信息</el-breadcrumb-item>
                    <el-breadcrumb-item style="font-weight: bold;">教籍信息</el-breadcrumb-item>
                </el-breadcrumb>
            </el-col>
            <el-col :span="3" style="margin-top: 10px; float: right;">
                <el-button type="success">添加学生</el-button>
            </el-col>
        </el-header>
        <el-main>
            <el-form ref="form" :model="form" label-width="80px" >
                <el-form-item label="学号" prop="stu_id">
                    <el-input v-model="form.stu_id" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-row>
                        <el-col :span="21">
                            <el-input v-model="form.password" style="width: 89%;" disabled></el-input>
                        </el-col>
                        <el-col :span="3">
                            <el-button type="success" style="width: 80%;">申请修改</el-button>
                        </el-col>
                    </el-row>
                </el-form-item>
                <el-form-item label="姓名" prop="name">
                    <el-input v-model="form.name" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <el-radio-group v-model="form.sex" disabled>
                        <el-radio label="男"></el-radio>
                        <el-radio label="女"></el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="身份证号" prop="IDnumber">
                    <el-input v-model="form.IDnumber" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="生日" prop="birthday">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.birthday" style="width: 90%;" disabled
                        value-format="yyyy-MM-dd">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="入职日期" prop="entrytime">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.entrytime" style="width: 90%;" disabled
                        value-format="yyyy-MM-dd">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="政治面貌" prop="outlook">
                    <el-input v-model="form.outlook" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="籍贯" prop="location">
                    <el-input v-model="defaultlocation" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="所属组织" prop="college">
                    <el-input v-model="defaultorganize" style="width: 90%;" disabled></el-input>
                </el-form-item>
                <el-form-item label="绩点" prop="course">
                    <el-input v-model="form.credit" style="width: 90%;" disabled></el-input>
                </el-form-item>
            </el-form>
        </el-main>
    </div>
</template>

<script>
    import { initStudentinfo } from "@/api/axioses4stu"
    export default {
        name: 'Vstudentinfo',
        data() {
            return {
                stu_id:'',
                //级联选择地区
                param: {},
                form: {},
                defaultlocation: "",
                defaultorganize: "",
            }
        },
        mounted: function () {
            this.stu_id = this.$store.state.userid
            this.initInfo();
        },
        methods: {
            //点击保存之后
            initInfo() {
                var that = this;
                initStudentinfo({ 'stu_id': this.stu_id }).then(ret => {
                    if (ret.data.code === 1000) {
                        //需做一次类型转换，将number转换成string
                        console.log(ret.data);
                        that.defaultlocation = ret.data.form.country + "/" + ret.data.form.province + "/" + ret.data.form.city;
                        that.defaultorganize = ret.data.form.College + "/" + ret.data.form.Major + "/" + ret.data.form.Class;
                        that.form = ret.data.form;
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
        },
    }
</script>

<style scoped>

</style>