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


      </v-expansion-panel-header>

      <v-expansion-panel-content>

        <Order_cart :info="item" :orderProducts="orderProducts" :productDictList="nowProduct" ></Order_cart>
         <!-- 提醒付款：需要消息系统，后续实现-->

        <v-col>
          <v-btn
            color="success"
            @click="changeStatus(item.pk)"
          >
            {{btn_content}}
          </v-btn>
        </v-col>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Order_cart from "@/components/business/order_cart";
import {RegionText} from 'v-region'
export default {
  name: 'order_inDelivery',
  components: {Order_cart,

    RegionText
  },
  props:{
    tabkey:Object
  },
    watch: {
  tabkey: function () {
    this.initBusinessOrders()
  }
},
  data: () => ({
    btn_content: '货物已送达',


    business_orders:[],
    orderProducts:[],
    nowProduct:[],
    userAvatar:[],


  }),
  methods:{

    async initBusinessOrders(){
      await this.axios.get('show_business_orderProduct_status/',
          {params:{business_id: this.$store.state.userId,status:'买家未到货'}})
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

    async changeStatus(click_order_id) {
      await this.axios.get('alterOrderStatus/',
          {params:{order_id: click_order_id,status:'买家未收货'}})
        .then((response) => {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
      await this.initBusinessOrders()
    },
  },
  async created(){
    await this.initBusinessOrders()
  },
}
</script>