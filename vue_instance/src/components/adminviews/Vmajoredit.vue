<template>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
        <el-form-item label="专业名称" prop="name">
            <el-input v-model="form.name" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="所属学院" prop="college">
            <el-select v-model="form.college" placeholder="请选择" style="width: 90%" @change="changeCollege">
                <el-option
                    v-for="item in colleges"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id"
                    >
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="先修课" prop="pre">
            <el-transfer
              filterable
              filter-placeholder="请输入课程代号"
              :filter-method="filterMethod"
              v-model="form.course"
              :data="data"
              style="text-align: left;margin-left: 8%;"
              >
            </el-transfer>
        </el-form-item>
        <el-form-item>
            <el-button type="success" @click="onSave()" :loading="load">保存</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import {postMajorSubmit, postAdd, postaddTea ,initMajorInfo, editMajorOptions} from "@/api/axioses"
    export default {
        name: 'Vteacherdraw',
        data() {
            return {
                form: {
                },
				course_id: [],
				course_cou_id: [],
				course_name: []
            }
        },
        props: ['drawer', 'maj_id', 'ifadd','col_id'],
        mounted: function () {
            this.getOptions();
        },
        methods: {
            //点击保存之后
            onSave() {
                let form = this.form;
                this.$refs.form.validate((valid) => {
                    this.load = true;
                    var that = this;
                    const param = {
                        form: JSON.stringify(this.form)
                    }
                    if (valid) {
                        that.load = false
                        if (this.ifadd == false) { //如果是修改现有
                            postMajorSubmit(param).then(res => {
                                if (res.data.code == "1000") {
                                    this.$confirm('保存成功！')
                                        .then(_ => {
                                            //隐藏面板（由于面板是在父组件定义的，这里必须要操作父组件的ref）
                                            that.drawer.infodrawer.hide();
                                            //重新通过initList获取父组件的表格：
                                            this.$emit('initMajorList');
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

                editMajorOptions({'col_id': this.col_id}).then(ret => {
                    if (ret.data.code == 1000) {
                        that.colleges = ret.data.colleges;
                        that.course_id = ret.data.course_id;
                        that.course_cou_id = ret.data.course_cou_id;
                        that.course_name = ret.data.course_name;
						this.initInfo()
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
            },
            initInfo() {
                if (this.ifadd == false) {
                    var that = this;
                    initMajorInfo({'maj_id': this.maj_id}).then(ret => {
                        if (ret.data.code === 1000) {
                            that.form = ret.data.majordata;
                            //需做一次类型转换，将number转换成string
                            this.generateData()
                        } else {
                            alert('获取数据失败')
                        }
                    }).catch(function (ret) {
                    })
                }
            },
            generateData(){
                var data = [];
                this.course_name.forEach((name, index) => {
                    data.push({
                        label: name,
                        key: this.course_id[index],
                        id: this.course_cou_id[index]
                    });
                });
                this.data = data
                console.log(this.data);
			},
            filterMethod(query, item) {
                return item.id.indexOf(query) > -1;
            },
            changeCollege(){
                var that = this;
                editMajorOptions({'col_id': this.form.college}).then(ret => {
                    if (ret.data.code == 1000) {
                        that.colleges = ret.data.colleges;
                        that.course_id = ret.data.course_id;
                        that.course_cou_id = ret.data.course_cou_id;
                        that.course_name = ret.data.course_name;
                    } else {
                        alter('获取数据失败')
                    }
                }).catch(ret => {
                })
				this.form.course = []
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