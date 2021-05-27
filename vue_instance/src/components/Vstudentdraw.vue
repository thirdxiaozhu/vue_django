<template>
    <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="学号">
            <el-input v-model="form.stu_id"></el-input>
        </el-form-item>
        <el-form-item label="密码">
            <el-input v-model="form.passeword"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
            <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="性别">
            <el-radio-group v-model="form.sex">
                <el-radio label="男"></el-radio>
                <el-radio label="女"></el-radio>
            </el-radio-group>
        </el-form-item>
        <el-form-item label="身份证号">
            <el-input v-model="form.idnumber"></el-input>
        </el-form-item>
        <el-form-item label="生日">
            <el-col :span="11">
                <el-date-picker type="birthday" placeholder="选择日期" v-model="form.birthday" style="width: 100%;">
                </el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="入学日期">
            <el-col :span="11">
                <el-date-picker type="entryday" placeholder="选择日期" v-model="form.entryday" style="width: 100%;">
                </el-date-picker>
            </el-col>
        </el-form-item>
        <el-form-item label="活动区域">
            <el-select v-model="form.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="即时配送">
            <el-switch v-model="form.delivery"></el-switch>
        </el-form-item>
        <el-form-item label="活动性质">
            <el-checkbox-group v-model="form.type">
                <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
                <el-checkbox label="地推活动" name="type"></el-checkbox>
                <el-checkbox label="线下主题活动" name="type"></el-checkbox>
                <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
            </el-checkbox-group>
        </el-form-item>
        <el-form-item label="活动形式">
            <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
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
                    type: [],
                    desc: ''
                }
            }
        },
        props: {
            stu_id: String,
        },
        methods: {
            onSubmit() {
                console.log('submit!');
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