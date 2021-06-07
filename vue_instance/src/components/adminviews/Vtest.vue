<template>
    <div>
    <el-transfer
      filterable
      :filter-method="filterMethod"
      filter-placeholder="请输入城市拼音"
      v-model="value"
      :data="data"
      style="text-align: left;">
    </el-transfer>
    <el-button @click="getClick">aaa</el-button>
</div>
  </template>
  
  <script>
    export default {
      data() {
        const generateData = _ => {
          const data = [];
          const cities = ['上海', '北京', '广州', '深圳', '南京', '西安', '成都'];
          const pinyin = ['shanghai', 'beijing', 'guangzhou', 'shenzhen', 'nanjing', 'xian', 'chengdu'];
          cities.forEach((aaa, index) => {
            data.push({
              label: aaa,
              key: index,
              pinyin: pinyin[index]
            });
          });
          return data;
        };
        return {
          data: generateData(),
          value: [],
          filterMethod(query, item) {
            return item.pinyin.indexOf(query) > -1;
          }
        };
      },
      methods:{
        getClick(){
                console.log(this.data)
            }
      }
    };
  </script>