<template>
  <div class="height-100pc mx-3 goods-home">
    <v-row justify="center" class="my-3">
      <template v-for="(item, itemIndex) in indicators">
        <v-col :key="itemIndex" cols="12" md="3">
          <v-hover v-slot="{ hover }">
            <v-card
                class="item-card"
                :elevation="hover ? 12 : 2"
                :class="{ 'on-hover': hover }"
            >
              <v-row class="mx-3 ">
                <v-col md="6" class="align-center">
                  <v-icon :color="item.color" size="100">{{
                      item.icon
                    }}
                  </v-icon>
                </v-col>
                <v-col md="6" class="align-center justify-center flex-column ">
                  <div class="text-h5 text-center">{{ item.title }}</div>
                  <div class="text-h7 text-center">{{ item.text }}</div>
                </v-col>
              </v-row>
            </v-card>
          </v-hover>
        </v-col>
      </template>
    </v-row>

   <div>
      <v-card class="mt-9" v-if="chartLoaded">
        <v-row>
          <v-btn
              class="ma-2"
              color="blue"
              @click="leftPage"
          >
            <v-icon color="white">mdi-arrow-left</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
              class="ma-2"
              color="blue"
              @click="rightPage"
          >
            <v-icon color="white">mdi-arrow-right</v-icon>
          </v-btn>
        </v-row>
        <v-row class="ml-3">
          周业务量
        </v-row>
        <line-chart
            width="98%"
            :chart-data="lineChartData"
            :indicators="lineChartIndicators"
            :dimension="dimension"
        ></line-chart>
      </v-card>
    </div>

    <!-- 提示语，之后移至商家暂未通过审核处
    <div>
      <template>
        <v-footer padless color="blue">
          <v-col class="text-center white--text">
            欢迎{{business_name}}，您可以通过左侧导航栏查看更多不同页面。
          </v-col>
        </v-footer>
      </template>
    </div>
    -->
  </div>
</template>

<script>
import {getHomePanels, getWeekAnalysis} from "@/api/goods";
import LineChart from "@/components/business/LineChart";

const lineChartData = {
  purchases: [100, 120, 161, 134, 105, 160, 165],
  sales: [120, 82, 91, 154, 162, 140, 145],
  expenses: [110, 70, 150, 50, 46, 80, 111],
  profits: [99, 55, 110, 67, 88, 44, 76],
};
const DEFAULT_PANELS = [
  {icon: "mdi-dolly", color: "blue", title: "商品", text: "4(件)"},
  {
    icon: "mdi-cart-arrow-up",
    color: "cyan",
    title: "总销售额",
    text: "1100.00（元）",
  },
  {
    icon: "mdi-cash-refund",
    color: "red",
    title: "支出",
    text: "568.20（元）",
  },
  {
    icon: "mdi-currency-cny",
    color: "amber",
    title: "利润",
    text: "-368.20（元）",
  },
];

var now = new Date(); //当前日期
var nowDayOfWeek = now.getDay(); //今天本周的第几天
var nowDay = now.getDate(); //当前日
var nowMonth = now.getMonth(); //当前月
var nowYear = now.getFullYear(); //当前年

//获得本周的开端日期
function getWeekStartDate(offset,weekday) {
let weekStartDate = new Date(nowYear, nowMonth, nowDay - nowDayOfWeek +weekday+ 7*offset);
return weekStartDate;
}


function formatDate(date) {
let myyear = date.getFullYear();
let mymonth = date.getMonth() + 1;
let myweekday = date.getDate();
if (mymonth < 10) {
mymonth = "0" + mymonth;
}
if (myweekday < 10) {
myweekday = "0" + myweekday;
}
return (myyear + "" + mymonth + "" + myweekday);
}

export default {
  name: "business_saledata",
  components: {
    LineChart,
  },
  data: () => ({
    business_name :"商家lll",
    lineChartData,
    indicators: DEFAULT_PANELS,
    offset:0,
    lineChartIndicators: ["采购额", "销售额", "支出", "利润"],
    dimension: ["周一\n"+formatDate(getWeekStartDate(0,1)),
      "周二\n"+formatDate(getWeekStartDate(0,2)),
      "周三\n"+formatDate(getWeekStartDate(0,3)),
      "周四\n"+formatDate(getWeekStartDate(0,4)),
      "周五\n"+formatDate(getWeekStartDate(0,5)),
      "周六\n"+formatDate(getWeekStartDate(0,6)),
      "周日\n"+formatDate(getWeekStartDate(0,7)),],
    chartLoaded: false,





  }),
 computed: {



      },
   methods:{
    leftPage(){
      this.offset-=1
      this.newDimension()


    },
     rightPage(){
      this.offset+=1
       this.newDimension()
    },
     newDimension(){
      this.dimension= ["周一\n"+formatDate(getWeekStartDate(this.offset,1)),
      "周二\n"+formatDate(getWeekStartDate(this.offset,2)),
      "周三\n"+formatDate(getWeekStartDate(this.offset,3)),
      "周四\n"+formatDate(getWeekStartDate(this.offset,4)),
      "周五\n"+formatDate(getWeekStartDate(this.offset,5)),
      "周六\n"+formatDate(getWeekStartDate(this.offset,6)),
      "周日\n"+formatDate(getWeekStartDate(this.offset,7)),]
       console.log(this.dimension)
     }
   },
  created() {

  },


  mounted() {


    getHomePanels()
        .then((homePanels) => {
          this.indicators = homePanels;
        })
        .catch((err) => {
          console.warn(err);
        });

    getWeekAnalysis()
        .then((result) => {
          this.lineChartIndicators = result.indicators;
          this.dimension = result.dimension;
          this.lineChartData = {
            purchases: result.data[0],
            sales: result.data[1],
            expenses: result.data[2],
            profits: result.data[3],
          };
          this.$nextTick(() => {
            this.chartLoaded = true;
          });
        })
        .catch((err) => {
          console.warn(err);
          this.chartLoaded = true;
        });
  },
};
</script>

<style>
.item-card {
  transition: opacity 0.4s ease-in-out;
}

.item-card:not(.on-hover) {
  opacity: 0.6;
}

.line-chart {
  background: #fff;
}
</style>
