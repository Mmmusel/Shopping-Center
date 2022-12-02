<template>
  <div class="order-right">
    <div class="order-content">
      <div class="title">
        <h3>我的订单</h3>
      </div>
      <div class="chosetype">
        <table>
          <thead>
          <tr>
            <th style="width:29%">商品</th>
            <th style="width:31%">订单详情</th>
            <th style="width:13%">收货人</th>
            <th>金额</th>
            <th>状态</th>
            <th>操作</th>
          </tr>
          </thead>
        </table>
      </div>
      <div class="orders">
        <!-- 每一笔订单 -->
        <table class="order-item" v-for="order in myOrder" :key="order.id">
          <thead>
          <tr>
            <th colspan="5">
                <span class="ordertitle">{{ order.createTime }}订单编号:{{ order.outTradeNo }}
                  <span class="pull-right delete"><img src="./images/delete.png" />
                  </span></span>
            </th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(cart,index) in order.orderDetailList" :key="cart.id">
            <td style="width: 60%"  >
                <div class="typographic">
                  <img :src="cart.imgUrl" style="width:100px;height:100px;"/>
                  <a style="width: 30%" href="#" class="block-text">{{cart.skuName}}</a>
                  <a style="width: 40%">x{{cart.skuNum}}</a>
                  <a style="width: 30%" href="#" class="service">售后申请</a>
                </div>
            </td>

            <td :rowspan="order.orderDetailList.length" v-if="index==0" style="width:8%" class="center">{{order.consignee}}</td>
            <td :rowspan="order.orderDetailList.length" v-if="index==0" style="width:13%" class="center">
              <ul class="unstyled">
                <li>总金额¥{{order.totalAmount}}.00</li>
                <li>在线支付</li>
              </ul>
            </td>
            <td :rowspan="order.orderDetailList.length" v-if="index==0" style="width:8%" class="center">
              <a href="#" class="btn">{{order.orderStatusName}} </a>
            </td>
            <td :rowspan="order.orderDetailList.length" v-if="index==0" style="width:13%" class="center">
              <ul class="unstyled">
                <li>
                  <a href="" target="_blank">评价|晒单</a>
                </li>
              </ul>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import order_data from "./myOrders";
export default {
  name:"orderS",
  data() {
    return {
      //初始化参数
      //当前第几页
      page: 1,
      //每一页展示数据个数
      limit: 3,
      //存储我的订单的数据
      myOrder:{}
    }
  },
  mounted () {
    //获取我的订单的数据方法
    this.getData()
  },
  methods: {
    //获取我的订单的方法
    async getData() {
      //解构出参数
      this.myOrder = order_data;
    },
    //获取当前点击的那一页
  },
};
</script>

<style lang="scss" scoped>
table{
  border: 1px solid #e7e7e7;
  border-collapse: collapse;
  font-size: 12px;
  color: #666;
  text-align: left;
  width: 1000px;
}


</style>
