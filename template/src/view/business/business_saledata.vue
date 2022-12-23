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

    <v-btn
              class="ma-2"
              color="blue"
              @click="printOut"
          >导出pdf
    </v-btn>
    <!-- todo -->
              <template>
              <download-excel
              class="export-excel-wrapper"
              :data="DetailsForm"
              :fields="json_fields"
              :header="Title"
              name="导出销量.xls"
            >
              <!-- 上面可以自定义自己的样式，还可以引用其他组件button -->
              <el-button type="success">导出excel</el-button>
              </download-excel>
              </template>
    <!--删除删除 TODO
    -->
    <div class="container">
      {{ upload_file || "导入" }}
      <input
        type="file"
        accept=".xls,.xlsx"
        class="upload_file"
        @change="readExcel($event)"
      />
    </div>
    <!-- todo -->
    <div>
      <region-selects


                                v-model="chooseRegion"
                                :town="false"


                                @change="selectLogs"
                                clearable
                              />
    </div>

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
        <line-chart id="xxx"
            width="98%"
            :chart-data="lineChartData"
            :indicators="lineChartIndicators"
            :dimension="dimension"
        ></line-chart>
      </v-card>
    </div>


    <div v-show="list.length">

    <div class="list-control">
      <div class="list-control-filter">
        <span>品牌:</span>
        <span class="list-control-filter-item"
              :class="{on: item === filterBrand}"
              v-for="item in brands" :key="item.index"
              @click="handleFilterBrand(item)" >{{item}}</span>
      </div>
      <div class="list-control-filter">
        <span>颜色:</span>
        <span class="list-control-filter-item"
              :class="{on: item === filterColor}"
              v-for="item in colors" :key="item.index"
              @click="handleFilterColor(item)">{{item}}</span>
      </div>

      <div class="list-control-order">
        <span>排序:</span>
        <span class="list-control-order-item"
              :class="{on: order === ''}"
              @click="handleOrderDefault">默认</span>
        <span class="list-control-order-item"
              :class="{on: order === 'sales'}"
              @click="handleOrderSales">
                    销量
                    <template v-if="order === 'sales'">↓</template>
                </span>
        <span class="list-control-order-item"
              :class="{on: order.indexOf('cost') > -1}"
              @click="handleOrderCost">
                    价格
                    <template v-if="order === 'cost-desc'">↓</template>
                    <template v-if="order === 'cost-asc'">↑</template>
                </span>
      </div>
    </div>
    <div class="productsList">
      <!--<business_Product v-for="item in filteredAndOrderedList" :info="item" :key="item.fields.id"></business_Product>
-->
      <div class="product" v-for="item in filteredAndOrderedList" :key="item.fields.id">
      <img :src="`http://127.0.0.1:8000/media/${item.fields.product_image}`" alt="" height="200px">
      <h4>{{item.fields.product_name}}</h4>
        <v-btn

            @click="ttt(item.pk)"
          >
            {{筛选显示}}
          </v-btn>
      <h4>销量{{item.fields.product_sales}}</h4>
      <div class="product-color"
           :style="{background: ccolors[item.fields.product_color]}"></div>
      <div class="product-cost">￥ {{item.fields.product_cost}}</div>
      <!-- 阻止冒泡，否则点击按钮的同时也会触发a标签进入详情页 -->


  </div>

    </div>



    <div class="product-not-found"
         v-show="!filteredAndOrderedList.length">暂无相关商品</div>



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
}; //todo

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
//导入商品简介组件

import htmlToPdf from '@/components/business/echartstopdf';
import { RegionSelects } from 'v-region'
import util from "@/components/customer/util";

import { read, utils } from 'xlsx'
//import business_Product from "@/components/business/business_product";
export default {
  name: "business_saledata",
  components: {
    LineChart,RegionSelects
  },
  data: () => ({
    Title:"导出本周数据",

    json_fields: {
        "采购额":'purchases',
        "销售额":'sales',
        "支出":'expenses',
        "利润":'profit',
      },
    DetailsForm: [
        {
          purchases:lineChartData.purchases[0],
          sales:lineChartData.sales[0],
          expenses:lineChartData.expenses[0],
          profit:lineChartData.profits[0]
        },
        {
          purchases:lineChartData.purchases[1],
          sales:lineChartData.sales[1],
          expenses:lineChartData.expenses[1],
          profit:lineChartData.profits[1]
        },
    ],
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


    list:[],
    chooseRegion:{
        province: '',//1
        city: '',//2
        area: '',//3
        town:''
      },
    regionState:0,

ccolors: {
        '白色': '#ffffff',
        '金色': '#dac272',
        '蓝色': '#233472',
        '红色': '#f2352e'
      },

    //品牌过滤
      filterBrand: '',
      //颜色过滤
      filterColor: '',
      order: '',

    choosedProduct:[]

  }),

   methods:{
    // todo
    readExcel(e) {
      // 读取表格文件
      let that = this;
      const files = e.target.files;


      if (files.length <= 0) {
        return false;
      } else if (!/\.(xls|xlsx)$/.test(files[0].name.toLowerCase())) {
        this.$message({
          message: "上传格式不正确，请上传xls或者xlsx格式",
          type: "warning"
        });
        return false;
      } else {
        // 更新获取文件名
        that.upload_file = files[0].name;
      }



      const fileReader = new FileReader();
      fileReader.onload = ev => {
        try {
          const data = ev.target.result;

          const workbook = read(data, {
            type: "binary"
          });

          const wsname = workbook.SheetNames[0]; //取第一张表
          const ws = utils.sheet_to_json(workbook.Sheets[wsname]); //生成json表格内容
          //ws就是读取的数据（不包含标题行即表头，表头会作为对象的下标）

          //this.submit_form();

					console.log(ws);

        } catch (e) {

          console.log(e);
          return false;
        }
      };
      console.log("rrrttt")
      fileReader.readAsBinaryString(files[0]);
    },
    printOut () {
        htmlToPdf.downloadPDF(document.querySelector('#xxx'), '统计报表')
      },
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

       await this.newWeekChartData()

     },


     newWeekChartData(){
       let s = getWeekStartDate(this.offset,1)
       let e = getWeekStartDate(this.offset,8)

       this.week_orders=this.business_orders.filter((item) => {
         var i=item.fields.order_createtime
         if(i<s) return false
         if(i>=e) return false
         return true
       });

       var tmpSales=[0,0,0,0,0,0,0]
       var tmpProfits=[0,0,0,0,0,0,0]

       this.week_orders.forEach((item) => {

         for(var i = 2;i<8;i++){
           if(this.week[i]>item.fields.order_createtime){
             tmpSales[i-1]+=item.fields.sumnum
             tmpProfits[i-1]+=item.fields.sumcost

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

         for(var i = 2;i<8;i++){
           if(this.week[i]>item.fields.stock_createtime){
             tmpPurchases[i-1]+=item.fields.stocksumnum
             tmpExpenses[i-1]+=item.fields.stocksumcost

             break

           }
          }

       });
       lineChartData.purchases=tmpPurchases
       lineChartData.expenses=tmpExpenses


       this.indicators[0].text = sum(lineChartData.purchases)+"（件）"
       this.indicators[1].text = sum(lineChartData.sales)+"（件）"
       this.indicators[2].text = sum(lineChartData.expenses).toFixed(2)+"（元）"
       this.indicators[3].text = sum(lineChartData.profits).toFixed(2)+"（元）"

       this.DetailsForm= [
        {
          purchases:lineChartData.purchases[0],
          sales:lineChartData.sales[0],
          expenses:lineChartData.expenses[0],
          profit:lineChartData.profits[0]
        },
        {
          purchases:lineChartData.purchases[1],
          sales:lineChartData.sales[1],
          expenses:lineChartData.expenses[1],
          profit:lineChartData.profits[1]
        },
           {
          purchases:lineChartData.purchases[2],
          sales:lineChartData.sales[2],
          expenses:lineChartData.expenses[2],
          profit:lineChartData.profits[2]
        },
           {
          purchases:lineChartData.purchases[3],
          sales:lineChartData.sales[3],
          expenses:lineChartData.expenses[3],
          profit:lineChartData.profits[3]
        },
           {
          purchases:lineChartData.purchases[4],
          sales:lineChartData.sales[4],
          expenses:lineChartData.expenses[4],
          profit:lineChartData.profits[4]
        },
           {
          purchases:lineChartData.purchases[5],
          sales:lineChartData.sales[5],
          expenses:lineChartData.expenses[5],
          profit:lineChartData.profits[5]
        },
           {
          purchases:lineChartData.purchases[6],
          sales:lineChartData.sales[6],
          expenses:lineChartData.expenses[6],
          profit:lineChartData.profits[6]
        },

    ]

     },

     async selectLogs(){

      if(!this.chooseRegion.province) {
        this.regionState = 0
      }else if(!this.chooseRegion.city){
        this.regionState=1
      }else if(!this.chooseRegion.area){
        this.regionState=2
      }else {
        this.regionState=3
      }

      console.log(this.regionState)
       console.log(this.chooseRegion)

      await this.initBusinessOrders()
    await this.initBusinessStocks()

    await this.newDimension()
    },

     async getProductsList(){
      //从Vuex获取商品列表信息
      //return this.$store.state.productList;
      await this.axios.get('show_products/')
        .then((response) => {
            console.log(response.data.list);
            var tmp = response.data.list.filter(i => i.fields.product_business === this.$store.state.userId)
          this.list=response.data.list.filter(i => i.fields.product_business === this.$store.state.userId)
          this.choosedProduct=response.data.list.filter(i => i.fields.product_business === this.$store.state.userId)
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

                    var regionRight =0
              if(this.regionState===1){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1}

              }else if(this.regionState===2){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1
                }else if(item.fields['region'].city!==this.chooseRegion.city){
                  regionRight=1
                }
              }else if(this.regionState===3){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1
                }else if(item.fields['region'].city!==this.chooseRegion.city){
                  regionRight=1
                }else if(item.fields['region'].area!==this.chooseRegion.area){
                  regionRight=1
                }

              }
              if(regionRight===0){
                    this.orderProducts.forEach(tt => {

                      if(tt.fields.order_id==item.pk){
                        if(this.choosedProduct.find(m => m.pk===tt.fields.product_id)) {
                          sum += (tt.fields.num - 0.0) * (parseFloat(tt.fields.order_product_cost))
                          num += tt.fields.num
                          console.log(num);
                          console.log(sum);
                        }
                      }
                    });}
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

                    var regionRight =0
              if(this.regionState===1){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1}

              }else if(this.regionState===2){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1
                }else if(item.fields['region'].city!==this.chooseRegion.city){
                  regionRight=1
                }
              }else if(this.regionState===3){
                if(item.fields['region'].province!==this.chooseRegion.province){
                  regionRight=1
                }else if(item.fields['region'].city!==this.chooseRegion.city){
                  regionRight=1
                }else if(item.fields['region'].area!==this.chooseRegion.area){
                  regionRight=1
                }

              }
              if(regionRight===0){

                    if(this.choosedProduct.find(m => m.pk===item.fields.product_id)) {
                      item.fields['stocksumcost'] = (item.fields.stock_num - 0.0) * (item.fields.stock_cost);//每一个订单的支出
                      item.fields['stocksumnum'] = item.fields.stock_num;//每一个订单的采购数量
                    }else{
                      item.fields['stocksumcost'] = 0.0;//每一个订单的支出
                      item.fields['stocksumnum'] = 0;//每一个订单的采购数量
                    }}else{
                      item.fields['stocksumcost'] = 0.0;//每一个订单的支出
                      item.fields['stocksumnum'] = 0;//每一个订单的采购数量
                    }
                });
            console.log(this.business_stocks);
        })
        .catch(function (error) {
            console.log(error);
        });

    },

     async fixedChoosed(){
      let list = [...this.list];
      //品牌过滤
      if(this.filterBrand !== ''){
        list = list.filter(item => item.fields.product_brand === this.filterBrand);
      }
      //颜色过滤
      if(this.filterColor !== ''){
        list = list.filter(item => item.fields.product_color === this.filterColor);
      }
      //排序
      if(this.order !== ''){
        if(this.order === 'sales'){
          list = list.sort((a, b) => b.fields.product_sales - a.fields.product_sales);
        }else if(this.order === 'cost-desc'){
          list = list.sort((a, b) => b.fields.product_cost - a.fields.product_cost);
        }else if(this.order === 'cost-asc'){
          list = list.sort((a, b) => a.fields.product_cost - b.fields.product_cost);
        }
      }
      this.choosedProduct=[...list]
       await this.initBusinessOrders()
    await this.initBusinessStocks()

    await this.newDimension()
     },

     async ttt(id){

      this.choosedProduct=this.list.filter(item => item.pk === id);
      await this.initBusinessOrders()
    await this.initBusinessStocks()

    await this.newDimension()
     },



     //品牌筛选
    async handleFilterBrand(brand){
      //点击品牌过滤，再次点击取消
      if (this.filterBrand === brand) {
        this.filterBrand = '';
      }else{
        this.filterBrand = brand;
      }
      await this.fixedChoosed()
    },
    //颜色筛选
    async handleFilterColor(color){
      //点击颜色过滤，再次点击取消
      if (this.filterColor === color) {
        this.filterColor = '';
      }else{
        this.filterColor = color;
      }
      await this.fixedChoosed()
    },
    async handleOrderDefault(){
      this.order = '';
      await this.fixedChoosed()
    },
    async handleOrderSales(){
      this.order = 'sales';
      await this.fixedChoosed()
    },
    handleOrderCost(){
      //当点击升序时将箭头更新↓,降序设置为↑
      if(this.order === 'cost-desc'){
        this.order = 'cost-asc';
      }else{
        this.order = 'cost-desc';
      }
    },

  },
  async created(){
    await this.getProductsList()
    await this.initBusinessOrders()
    await this.initBusinessStocks()

    await this.newDimension()



  },
  computed:{
    brands(){

      const brands = this.list.map(item => item.fields.product_brand);

      return util.getFilterArray(brands);

    },
    colors(){
      const colors = this.list.map(item => item.fields.product_color);
      return util.getFilterArray(colors);
    },
    filteredAndOrderedList(){
      //拷贝原数组
      let list = [...this.list];
      //品牌过滤
      if(this.filterBrand !== ''){
        list = list.filter(item => item.fields.product_brand === this.filterBrand);
      }
      //颜色过滤
      if(this.filterColor !== ''){
        list = list.filter(item => item.fields.product_color === this.filterColor);
      }
      //排序
      if(this.order !== ''){
        if(this.order === 'sales'){
          list = list.sort((a, b) => b.fields.product_sales - a.fields.product_sales);
        }else if(this.order === 'cost-desc'){
          list = list.sort((a, b) => b.fields.product_cost - a.fields.product_cost);
        }else if(this.order === 'cost-asc'){
          list = list.sort((a, b) => a.fields.product_cost - b.fields.product_cost);
        }
      }
      console.log("kkk")
      console.log(this.list)
      console.log(list)

      return list;
    }
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

<style scoped>
.item-card {
  transition: opacity 0.4s ease-in-out;
}

.item-card:not(.on-hover) {
  opacity: 0.6;
}

.line-chart {
  background: #fff;
}

.list-control{
  background: #fff;
  border-radius: 6px;
  margin: 16px;
  padding: 16px;
  box-shadow: 0 1px 1px rgba(0,0,0,.2);
}
.list-control-filter{
  margin-bottom: 16px;
}

.container {

  width: 500px;

  margin: 50px auto;

  overflow: hidden;

  border: 1px solid #ccc;

}
.bar1 {background: #A3D0C3; }
.bar1 input {
  border: 2px solid #7BA7AB;
  border-radius: 5px;
  background: #F9F0DA;
  color: #9E9C9C;
}
.bar1 button {
  top: 0;
  right: 0;
  background: #7BA7AB;
  border-radius: 0 5px 5px 0;
}
.bar1 button:before {
  font-family: FontAwesome,serif;
  font-size: 16px;
  color: #F9F0DA;
}
.list-control-filter-item,
.list-control-order-item {
  cursor: pointer;
  display: inline-block;
  border: 1px solid #e9eaec;
  border-radius: 4px;
  margin-right: 6px;
  padding: 2px 6px;
}
.list-control-filter-item.on,
.list-control-order-item.on{
  background: #f2352e;
  border: 1px solid #f2352e;
  color: #fff;
}
.product-not-found{
  text-align: center;
  padding: 32px;
}
.like {
  width: 1000px;

  margin: 50px auto;

  overflow: hidden;

  border: 1px solid #ccc;
}
.likeItem {
  display:inline-block; width:200px; height:200px;
}

.product{
  width: 330px;
  float: left;
}
.product-main{
  display: block;
  margin: 16px;
  padding: 16px;
  border: 1px solid #dddee1;
  border-radius: 6px;
  overflow: hidden;
  background: #fff;
  text-align: center;
  position: relative;
}
.product-main img{
  width: 100%;
}
h4{
  color: #222;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.product-main:hover h4{
  color: #0070c9;
}
.product-color{
  display: block;
  width: 16px;
  height: 16px;
  border: 1px solid #dddee1;
  border-radius: 50%;
  margin: 6px auto;
}
.product-cost{
  color: #de4037;
  margin-top: 6px;
}
.product-add-cart{
  display: none;
  padding: 4px 8px;
  background: #2d8cf0;
  color: #fff;
  font-size: 12px;
  border-radius: 3px;
  cursor: pointer;
  position: absolute;
  top: 5px;
  right: 5px;
}
.product-main:hover .product-add-cart{
  display: inline-block;
}
</style>
