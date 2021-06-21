<template>
	<div>
		<!--查询-->
		<!--表格-->
		<el-table :data="timeData" stripe style="width: 100%">
			<el-table-column prop="" label="日期" width="90" type="index" align="center">
                        <template slot-scope="scope">
                            <span>{{weekdayData[scope.$index].title}}</span>
                        </template>
                    </el-table-column>
			<el-table-column  label="第1-2节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
			<el-table-column  label="第3-4节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
			<el-table-column  label="第5-6节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
			<el-table-column  label="第7-8节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
			<el-table-column  label="第9-10节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
			<el-table-column  label="第11-12节"  align="center">
				<template slot-scope="scope">
					<div>
						<div v-if="scope.row[sbjectKey[i]]">
							{{scope.row[sbjectKey[i]]}}<br />
							{{scope.row[teacherKey[i]]}}
						</div>
						<div v-else>
							<el-button icon="el-icon-edit"></el-button>
						</div>
					</div>
				</template>
			</el-table-column>
		</el-table>
	</div>
</template>

<script>
    import { getsch4room } from "@/api/axioses"
	export default {
		data() {
			return {
				room: 26,
				sbjectKey: ['oneS', 'twoS', 'threeS', 'fourS', 'fiveS', 'sixS', 'sevenS', 'eightS', 'nineS'],//科目key值
				teacherKey: ['oneT', 'twoT', 'threeT', 'fourT', 'fiveT', 'sixT', 'sevenT', 'eightT', 'nineT'],//老师key值
				//每天的课表
				 timeData:[
          {
            id:'1',
            label:'周一',
          },
          {
            id:'2',
            label:'周二',
            oneS:'java教程2',
            oneT:'郑老师',
            twoS:'语文',
            twoT:'张老师',
            threeS:'心理辅导',
            threeT:'杨老师',
            fourS:'音乐',
            fourT:'巩老师',
            fiveS:'网络',
            fiveT:'征老师',
            sixS:'舞蹈',
            sixT:'程老师',
            sevenS:'ppt教程',
            sevenT:'翟老师',
            eightS:'职业规划',
            eightT:'郝老师',
            nineS:'就业指导',
            nineT:'曹老师'
          },
          {
            id:'3',
            label:'周三',
            oneS:'java教程3',
            oneT:'郑老师',
            twoS:'语文',
            twoT:'张老师',
            threeS:'心理辅导',
            threeT:'杨老师',
            fourS:'音乐',
            fourT:'巩老师',
            fiveS:'网络',
            fiveT:'征老师',
            sixS:'舞蹈',
            sixT:'程老师',
            sevenS:'ppt教程',
            sevenT:'翟老师',
            eightS:'职业规划',
            eightT:'郝老师',
            nineS:'就业指导',
            nineT:'曹老师'
          },
          {
            id:'4',
            label:'周四',
            oneS:'java教程',
            oneT:'郑老师',
            twoS:'语文',
            twoT:'张老师',
            threeS:'心理辅导',
            threeT:'杨老师',
            fourS:'音乐',
            fourT:'巩老师',
            fiveS:'网络',
            fiveT:'征老师',
            sixS:'舞蹈',
            sixT:'程老师',
            sevenS:'ppt教程',
            sevenT:'翟老师',
            eightS:'职业规划',
            eightT:'郝老师',
            nineS:'就业指导',
            nineT:'曹老师'
          },
          {
            id:'5',
            label:'周五',
            oneS:'java教程',
            oneT:'郑老师',
            twoS:'语文',
            twoT:'张老师',
            threeS:'心理辅导',
            threeT:'杨老师',
            fourS:'音乐',
            fourT:'巩老师',
            fiveS:'网络',
            fiveT:'征老师',
            sixS:'舞蹈',
            sixT:'程老师',
            sevenS:'ppt教程',
            sevenT:'翟老师',
            eightS:'职业规划',
            eightT:'郝老师',
            nineS:'就业指导',
            nineT:'曹老师'
          },
          {
            id:'',
            label:'周六',
          },
          {
            id:'',
            label:'周天',
          },
        ],
				//课节数据---标题
				titleData: [
					{
						id: '1',
						title: "1-2"
					},
					{
						id: '2',
						title: "3-4"
					},
					{
						id: '3',
						title: "5-6"
					},
					{
						id: '4',
						title: "7-8"
					},
					{
						id: '5',
						title: "9-10"
					},
					{
						id: '6',
						title: "11-12"
					},
				],
				weekdayData: [
					{
						id: '1',
						title: "周一"
					},
					{
						id: '2',
						title: "周二"
					},
					{
						id: '3',
						title: "周三"
					},
					{
						id: '4',
						title: "周四"
					},
					{
						id: '5',
						title: "周五"
					},
					{
						id: '6',
						title: "周六"
					},
					{
						id: '7',
						title: "周日"
					},
				],
			}
		},
		mounted() {
			this.timetableLoad();
		},
		methods: {
			timetableLoad(){
				const params = {
					room: this.room
				}
				getsch4room(params).then( res => {
					if(res.data.code === 1000){
						that.timeData = res.data.timedata
					}
				})
			},
		}
	}
</script>
<style>
	.tabletitle-timeline {
		line-height: 18px !important;
	}
</style>