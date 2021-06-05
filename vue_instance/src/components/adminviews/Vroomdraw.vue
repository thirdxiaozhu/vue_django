<template>
    <el-form label-width="80px" :rules="rules">
        <el-form-item label="容量" prop="capacity">
            <el-input v-model="capacity" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="教室类型" prop="function">
            <el-select v-model="functionselected" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in functions"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
            <el-button type="success" @click="onSave" :loading="load">保存</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { getFunctions,getRoomInfo} from "@/api/axioses"
    export default {
        name: 'Vstudentdraw',
        data() {
            return {
                load: false,
                capacity: '',
                functions: [],
                functionselected: 1,
                rules: {
                    capacity: [
                        { required: true, message: '请输入教室可容纳人数', trigger: 'blur' },
                    ],
                }
            }
        },
        props: ['drawer', 'roomname', 'ifadd'],
        mounted: function () {
            this.getOptions();
            this.initInfo();
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

                getFunctions().then(ret => {
                    if (ret.data.code == 1000) {
                        that.functions = ret.data.functions;
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
                if (this.ifadd == false) { //如果是编辑模式，那么就初始化编辑学生的数据
                    var that = this;
                    getRoomInfo({'roomname': that.roomname}).then(ret => {
                        console.log(ret.data)
                        if (ret.data.code === 1000) {
                            //需做一次类型转换，将number转换成string
                            that.functionselected = ret.data.function;
                            that.capacity = ret.data.capacity;
                            console.log(typeof(that.functionselected) , that.capacity);
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }
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