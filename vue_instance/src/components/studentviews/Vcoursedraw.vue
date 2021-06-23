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
                <el-option v-for="item in betyear" :key="item.id" :label="item.name" :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开课学院" prop="college">
            <el-select v-model="form.college" placeholder="请选择" style="width: 90%">
                <el-option v-for="item in colleges" :key="item.id" :label="item.name" :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="课程类型" prop="function">
            <el-select v-model="form.function" placeholder="请选择" style="width: 90%">
                <el-option v-for="item in functions" :key="item.id" :label="item.name" :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item>
            <el-button @click="getClick">确定</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { initCourseInfo } from "@/api/axioses4stu"
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
                betyear: {},
                collegeselected: 1,
                colleges: {},
                preselected: [],
                pre_courses: {},
                functionselected: 1,
                functions: {},
                //级联选择地区
                pre_course_id: [],
                pre_course_cou_id: [],
                pre_course_name: [],
                data: [],
                value: [],
            };
        },
        props: ['drawer', 'cou_id', 'ifadd'],
        mounted: function () {
            this.initInfo();
        },
        methods: {
            initInfo() {
                var that = this;
                initCourseInfo({
                    'cou_id': this.cou_id,
                }).then(ret => {
                    console.log(ret.data)
                    if (ret.data.code === 1000) {
                        that.form = ret.data.form;
                        console.log(that.form);
                        this.generateData()
                    } else {
                        alert('获取数据失败')
                    }
                }).catch(function (ret) {
                })
            },
            getClick() {
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