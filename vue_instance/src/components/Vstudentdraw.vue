<template>
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="学号">
            <el-input v-model="form.stu_id" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="密码">
            <el-input v-model="form.passeword" style="width: 90%;"></el-input>
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
        <el-form-item label="所在年级">
            <el-select v-model="form.region" placeholder="请选择" style="width: 90%">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="籍贯">
            <el-cascader
               placeholder="搜索地名"
               :options="addresses"
               filterable style="width: 90%"></el-cascader>
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
                    birthday: '',
                    entryday: '',
                    delivery: false,
                    credit: ''
                },
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

                addresses:{},
            }
        },
        props: {
            stu_id: String,
        },
        mounted: function () {
            this.initInfo()
        },
        methods: {
            onSave() {
                console.log('submit!');
            },
            initInfo() {
                var that = this;
                let postdata = this.$qs.stringify({
                    "stu_id":this.stu_id,
                });
                console.log(postdata);
                this.$axios.request({
                    url: "/api/studentinfo",
                    method: "GET",
                    params: {
                        'stu_id':postdata,
                    }
                }).then(function (ret) {
                    //ajax(axios)发送成功后，响应的内容
                    if (ret.data.code === 1000) {
                        //this.courseList = ret.data.data
                        //为什么不能按照上面那个写？——因为这里的this指的是$axios里面的this
                        //而不是data里面的，所以要按照下面的
                        that.tableData = ret.data.students
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
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