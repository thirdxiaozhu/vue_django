<template>
    <el-form ref="form" :model="form" label-width="100px" :rules="rules">
        <el-form-item label="收信人类型" prop="option">
            <el-select v-model="form.option" placeholder="请选择" style="width: 90%" @change="typeChange()">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="收件人" prop="towho" :rules="form.option==1?rules.name:[{ required: false, trigger: 'blur' }]"> 
            <el-input v-model="form.towho" placeholder="仅支持输入学号" style="width: 90%;" :disabled="disabled"></el-input>
        </el-form-item>
        <el-form-item label="标题" prop="title"> 
            <el-input v-model="form.title" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item label="正文">
            <el-input type="textarea" rows="4"  v-model="form.content" style="width: 90%;"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="success" @click="onSave">发送</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    import { postMessage } from "@/api/axioses4tea"
    export default {
        name: 'Vmessagedraw',
        data() {
            return {
                form: {
                },
                rules: {
                    option: [
                        { required: true, message: '请选择收信人类型', trigger: 'change' }
                    ],
                    title: [
                        { required: true, message: '请输入标题', trigger: 'blur' },
                        { min: 2, max: 100, message: '长度在 2 到 100 个字符', trigger: 'blur' }
                    ],
                    towho: [
                        { required: true, message: '请输入收信人', trigger: 'blur' },
                    ],
                },
				options: [{
        		  value: '1',
        		  label: '学生'
        		}, {
        		  value: '2',
        		  label: '管理员'
        		}],
				tea_id: "",
				disabled: false,
            }
        },
        props: ['drawer', 'stu_id', 'ifadd'],
        mounted: function () {
            this.tea_id = this.$store.state.userid;
        },
        methods: {
            //点击保存之后
            onSave() {
                let form = this.form;
				console.log(this.form)
                this.$refs.form.validate((valid) => {
                    var that = this;
                    const param = {
                        form: JSON.stringify(this.form),
						tea_id: this.tea_id
                    }
                    if (valid) {
                       	postMessage(param).then(res => {
                       	    if (res.data.code == "1000") {
                       	        console.log(that.drawer);
                       	        this.$confirm('保存成功！')
                       	            .then(_ => {
                       	                that.drawer.infodrawer.hide();
                       	                this.$emit('initSendList');
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
			typeChange(){
				if(this.form.option == 1){
					this.disabled = false
				}else{
					this.disabled = true
				}
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