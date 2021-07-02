<template>
    <div id="app" style="height:100%" class="login-container">
        <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm" label-position="left" label-width="0px"
            class="demo-ruleForm login-page">
            <h2 class="title" style="margin-bottom: 20px; margin-top: 3px;">登录</h2>
            <el-form-item prop="userid">
                <p style="float: left; margin-bottom: 0px; font-size: small;">请输入学号/教工号:</p>
                <el-input type="text" v-model="ruleForm.userid" auto-complete="off" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <p style="float: left; margin-bottom: 0px; font-size: small;">请输入密码:</p>
                <el-input type="password" v-model="ruleForm.password" auto-complete="off" placeholder="密码"></el-input>
            </el-form-item>
            <p style="float: left; margin-bottom: 0px; font-size: small;">请选择用户类型:</p>
            <el-radio-group v-model="ruleForm.radio">
                <el-row :gutter="80" >
                    <el-col :span="6">
                    <el-radio :label="1"  style="border-radius: 4px;" border :span="4">学生</el-radio>
                    </el-col>
                    <el-col :span="6">
                    <el-radio :label="2"  style="border-radius: 4px;" border :spam="4">教师</el-radio>
                    </el-col>
                    <el-col :span="6">
                    <el-radio :label="3"  style="border-radius: 4px;" border>管理员</el-radio>
                    </el-col>
                </el-row>
            </el-radio-group>`
            <el-checkbox v-model="checked" class="rememberme">七天免登录</el-checkbox>
            <el-form-item style="width:100%;">
                <el-button type="primary" style="width:100%;" @click="handleSubmit" :loading="logining">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    import { postLogin } from "@/api/axioses"
    import 'bootstrap/dist/css/bootstrap.min.css'
    export default {
        name: 'login',

        data() {
            return {
                logining: false,
                ruleForm: {
                    userid: '',
                    password: '',
                    radio: 1,
                },
                rules: {
                    userid: [{ required: true, message: '学号/教工号不能为空', trigger: 'blur' }],
                    password: [{ required: true, message: '密码不能为空', trigger: 'blur' }],
                },
                checked: false,
                isRight: false,
            }
        },
        mounted: function(){
            console.log(this.$store);
            this.isChecked()
        },
        methods: {
            handleSubmit(event) {
                var that = this;
                this.$refs.ruleForm.validate((valid) => {
                    if (valid) {
                        this.logining = true;
                        postLogin(this.ruleForm).then(res => {
                            console.log(res)

                            if (res.data.code == "1000") {
                                this.logining = false;

                                if(that.checked == true){
                                    that.$store.commit('saveToken',{token: res.data.token,userid: that.ruleForm.userid,
                                        username: res.data.name, usertype: that.ruleForm.radio, ischecked: true})
                                }else{
                                    that.$store.commit('saveToken',{token: res.data.token,userid: that.ruleForm.userid,
                                        username: res.data.name, usertype: that.ruleForm.radio, ischecked: false})
                                }

                                if(that.ruleForm.radio == 1)
                                    this.$router.push({ path: '/student' });
                                else if(that.ruleForm.radio == 2)
                                    this.$router.push({ path: '/teacher' });
                                else
                                    this.$router.push({ path: '/admin' });

                            } else {
                                this.logining = false;
                                this.$alert(res.data.error, '错误', {
                                    confirmButtonText: '确定'
                                })
                            }
                        })

                    } else {
                        console.log('error submit!');
                        return false;
                    }
                })
            },
            isChecked(){
                if(this.$store.state.ischecked){
                    const type = this.$store.state.usertype
                    if(type == 1)
                        this.$router.push({ path: '/student' });
                    else if(type == 2)
                        this.$router.push({ path: '/teacher' });
                    else
                        this.$router.push({ path: '/admin' });

                }
            }

        }
    };
</script>

<style>
html,body,#app {
  text-align: center;
  color: #2c3e50;
  height:100%;
}
.login-container {
    width: 100%;
    height: 100%;
}
.login-page {
    -webkit-border-radius: 5px;
    border-radius: 20px;
    margin: 150px auto;
    width: 350px;
    height: auto;
    padding: 20px 35px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}
label.el-checkbox.rememberme {
    margin: 0px 0px 15px;
    text-align: left;
}
</style>
