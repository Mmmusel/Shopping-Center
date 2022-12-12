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

var lineChartData = {
  purchases: [100, 120, 161, 134, 105, 160, 165],
  sales: [120, 82, 91, 154, 162, 140, 145],
  expenses: [110, 70, 150, 50, 46, 80, 111],
  profits: [99, 55, 110, 67, 88, 44, 76],
};
var DEFAULT_PANELS = [
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
var nowDayOfWeek = (now.getDay()==0)?7:now.getDay(); //今天本周的第几天
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

function sum(arr) {
        return arr.reduce(function (total, value) {
          return total + value;
        });
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

    business_orders:[],
    orderProducts:[],
    nowProduct:[],

    business_stocks:[],

    week_orders:[],
    week_stocks:[],
    week:[],




  }),

   methods:{
    leftPage(){
      this.offset-=1
      this.newDimension()


    },
     rightPage(){
      this.offset+=1
       this.newDimension()
    },
     async newDimension(){
      console.log("zzzb")
      for(var i = 1;i<8;i++){
       this.week[i]=getWeekStartDate(this.offset,i)
      }

      this.dimension= ["周一\n"+formatDate(getWeekStartDate(this.offset,1)),
      "周二\n"+formatDate(getWeekStartDate(this.offset,2)),
      "周三\n"+formatDate(getWeekStartDate(this.offset,3)),
      "周四\n"+formatDate(getWeekStartDate(this.offset,4)),
      "周五\n"+formatDate(getWeekStartDate(this.offset,5)),
      "周六\n"+formatDate(getWeekStartDate(this.offset,6)),
      "周日\n"+formatDate(getWeekStartDate(this.offset,7)),]
console.log("zzzbb")
       await this.newWeekChartData()
       console.log("zzzbbb")

     },


     newWeekChartData(){
      console.log("zzzc")
       let s = getWeekStartDate(this.offset,1)
       let e = getWeekStartDate(this.offset,8)

       console.log(this.business_orders)
       console.log(s)
       console.log(e)

       this.week_orders=this.business_orders.filter((item) => {
         var i=item.fields.order_createtime
         if(i<s) return false
         if(i>=e) return false
         return true
       });

       console.log(this.week_orders)

       var tmpSales=[0,0,0,0,0,0,0]
       var tmpProfits=[0,0,0,0,0,0,0]

       this.week_orders.forEach((item) => {
         console.log("\nmm")
         console.log(item.fields.sumnum)
         console.log(item.fields.sumcost)
         console.log(this.week[i])
         console.log(item.fields.order_createtime)
         for(var i = 2;i<8;i++){
           if(this.week[i]>item.fields.order_createtime){
             tmpSales[i-1]+=item.fields.sumnum
             tmpProfits[i-1]+=item.fields.sumcost
             console.log(item.fields.sumnum)
             console.log(tmpSales[i-1])
             break
           }
          }

       });
       lineChartData.sales=tmpSales
       lineChartData.profits=tmpProfits


       this.week_stocks=this.business_stocks.filter((item) => {
         var i=item.fields.stock_createtime
         if(i<s) return false
         if(i>=e) return false
         return true
       });
       console.log(this.week_stocks)

       var tmpPurchases=[0,0,0,0,0,0,0]
       var tmpExpenses=[0,0,0,0,0,0,0]

       this.week_stocks.forEach((item) => {
         console.log("\nmm")
         console.log(item.fields.stocksumnum)
         console.log(item.fields.stocksumcost)
         console.log(this.week[i])
         console.log(item.fields.stock_createtime)
         for(var i = 2;i<8;i++){
           if(this.week[i]>item.fields.stock_createtime){
             tmpPurchases[i-1]+=item.fields.stocksumnum
             tmpExpenses[i-1]+=item.fields.stocksumcost
             console.log("pppppp")
             break

           }
          }

       });
       lineChartData.purchases=tmpPurchases
       lineChartData.expenses=tmpExpenses

       console.log(lineChartData)

       console.log("zzzccc")

       this.indicators[0].text = sum(lineChartData.purchases)+"（件）"
       this.indicators[1].text = sum(lineChartData.sales)+"（件）"
       this.indicators[2].text = sum(lineChartData.expenses).toFixed(2)+"（元）"
       this.indicators[3].text = sum(lineChartData.profits).toFixed(2)+"（元）"

     },

     async getProductsList(){
      //从Vuex获取商品列表信息
      //return this.$store.state.productList;
      await this.axios.get('show_products/')
        .then((response) => {
            console.log(response.data.list);
            var tmp = response.data.list.filter(i => i.fields.product_business === this.$store.state.userId)
           tmp.forEach(item => {
          this.nowProduct[item.pk] = item;

        });})
        .catch(function (error) {
            console.log(error);
        });
    },


  async initBusinessOrders(){



      await this.axios.get('show_business_orderProduct/',{params:{business_id: this.$store.state.userId}})
        .then((response) => {
            console.log(response);
            this.orderProducts = response.data.orderProducts;

            this.business_orders = response.data.orders;
            this.nowProduct.forEach(item => {


                    var sum=0.0
                    var num=0
                    this.orderProducts.forEach(tt => {
                      if(tt.fields.product_id==item.pk){
                        sum+=(tt.fields.num-0.0)*(tt.fields.order_product_cost)
                        num+=tt.fields.num
                      }
                    });
                    item.fields['sumcost']=sum;//每一个商品的销售额
                    item.fields['sumnum']=num;//每一个商品的销售量


            });



            this.business_orders.forEach(item => {
                    item.fields['order_createtime']=new Date(item.fields['order_createtime'])
                    item.fields['region']={
                      province:item.fields.customer_province,
                      city:item.fields.customer_city,
                      area:item.fields.customer_area,
                      town:''
                    };
                    var sum=0.0
                    var num=0
                    this.orderProducts.forEach(tt => {

                      if(tt.fields.order_id==item.pk){
                        sum+=(tt.fields.num-0.0)*(parseFloat(tt.fields.order_product_cost))
                        num+=tt.fields.num
                        console.log(num);
                        console.log(sum);
                      }
                    });
                    item.fields['sumcost']=sum;//每一个订单的销售额
                    item.fields['sumnum']=num;//每一个订单的销售量

                });
            console.log(this.business_orders);
        })
        .catch(function (error) {
            console.log(error);
        });

    },


     async initBusinessStocks(){
      await this.axios.get('fetch_stock/',{params:{business_id: this.$store.state.userId}})
        .then((response) => {
            console.log(response);


            this.business_stocks = response.data.stock_orders;
            this.nowProduct.forEach(item => {


                    var stocksum=0.0
                    var stocknum=0
                    this.business_stocks.forEach(tt => {
                      if(tt.fields.product_id==item.pk){
                        stocksum+=(tt.fields.stock_num-0.0)*(tt.fields.stock_cost)
                        stocknum+=tt.fields.stock_num
                      }
                    });
                    item.fields['stocksumcost']=stocksum;//每一个商品的支出
                    item.fields['stocksumnum']=stocknum;//每一个商品的采购数量


            });



            this.business_stocks.forEach(item => {
                    item.fields['stock_createtime']=new Date(item.fields['stock_createtime'])
                    item.fields['region']={
                      province:item.fields.customer_province,
                      city:item.fields.customer_city,
                      area:item.fields.customer_area,
                      town:''
                    };

                    item.fields['stocksumcost']=(item.fields.stock_num-0.0)*(item.fields.stock_cost);//每一个订单的支出
                    item.fields['stocksumnum']=item.fields.stock_num;//每一个订单的采购数量

                });
            console.log(this.business_stocks);
        })
        .catch(function (error) {
            console.log(error);
        });

    },

  },
  async created(){
    await this.getProductsList()
    await this.initBusinessOrders()
    await this.initBusinessStocks()
    console.log("zzz")
    await this.newDimension()
    console.log("zzzzz")
    console.log(lineChartData)
    console.log(this.dimension)
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
