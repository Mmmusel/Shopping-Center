<template>
  <v-expansion-panels focusable multiple popout>
    <v-expansion-panel
        v-for="item in business_orders"
        :key="item.fields.customer_name"
    >
      <v-expansion-panel-header>
        <!--蓝底头像+用户名-->
        <v-col>
          <!--
          <v-avatar
            color="#64B5F6"
            size="56"
            class="white--text"
          >
            {{ item.fields.customer_name }}
          </v-avatar>
          !-->
          <img :src="`http://127.0.0.1:8000/media/${userAvatar[item.fields.customer_id]}`" alt=""
                    height="50px" width="50px">
        </v-col>
        <!--用户名-->
        <v-col>
          <v-list-item-title>{{ item.fields.customer_name }}</v-list-item-title>
        </v-col>
        <!--下单时间-->
        <v-col>
          <v-list-item-title>{{ item.fields.order_createtime | format  }}</v-list-item-title>
        </v-col>
        <!--地址-->
        <v-col>
          <!--<v-list-item-title>{{ item.address }}</v-list-item-title>-->
          <region-text
                  separator="-"
                  :town="false"
                  v-model="item.fields.region"
          />
        </v-col>
        <v-col>
          <v-list-item-title>{{ item.fields.customer_address  }}</v-list-item-title>

        </v-col>
        <v-col>
          <v-list-item-title>{{ item.fields.customer_mobile  }}</v-list-item-title>

        </v-col>

        <!-- 提醒付款：需要消息系统，后续实现-->
        <v-col>
          <v-btn
            color="success"
            @click="changeStatus(item.fields.pk)"
          >
            {{btn_content}}
          </v-btn>
        </v-col>
      </v-expansion-panel-header>

      <v-expansion-panel-content>
        <Order_cart :info="item" :orderProducts="orderProducts" :productDictList="nowProduct" ></Order_cart>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Order_cart from "@/components/business/order_cart";
import {RegionText} from 'v-region'
export default {
  name: 'order_weifukuan',
  components: {Order_cart,

    RegionText
  },
  data: () => ({
    items: [
      {color: '#2196F3', name: 'lzh', address: '北京', dingdan:'111'},
      {color: '#90CAF9', name: 'lyq', address: '山东', dingdan:'222'},
      {color: '#64B5F6', name: 'lr', address: '湖南', dingdan:'333'},
      {color: '#42A5F5', name: 'lzh', address: '北京', dingdan:'444'},
      {color: '#1E88E5', name: 'lyq', address: '山东', dingdan:'555'},
      {color: '#1976D2', name: 'lr', address: '湖南', dingdan:'666'},
    ],
    // 用户头像颜色，此处没有使用图片，后续可以考虑改为用户头像
    //colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],

    /* 可以使用订单类？
     * 从每个订单类中查找用户名、商品名和对应的商品数量
     */

    btn_content: '提醒付款',


    business_orders:[],
    orderProducts:[],
    nowProduct:[],
    userAvatar:[],


  }),
  methods:{

    async initBusinessOrders(){
      await this.axios.get('show_business_orderProduct/',{params:{business_id: this.$store.state.userId}})
        .then((response) => {
            console.log(response);
            this.business_orders = response.data.orders;
            response.data.nowProduct.forEach(item => {
                    this.nowProduct[item.pk] = item;
                });

            response.data.userAvatar.forEach(item => {
                    this.userAvatar[item.pk] = item.fields.user_avatar;
                });

            this.business_orders.forEach(item => {
                    item.fields['region']={
                      province:item.fields.customer_province,
                      city:item.fields.customer_city,
                      area:item.fields.customer_area,
                      town:''
                    }

                });



            this.orderProducts = response.data.orderProducts;
            //this.nowProduct = response.data.nowProduct;
            console.log(this.business_orders);
            //this.business_orders_ids = response.data.list.map(item => item.pk)
        })
        .catch(function (error) {
            console.log(error);
        });

    },

    changeStatus(order_id) {
      console.log(order_id)
    },
  },
  async created(){
    await this.initBusinessOrders()
  },
}
</script>