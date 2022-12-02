<template>
    <div class="cart">
        <div class="cart-header">
            <div class="cart-header-main">
                <div class="cart-info">商品信息</div>
                <div class="cart-price">单价</div>
                <div class="cart-count">数量</div>
                <div class="cart-cost">小计</div>
            </div>
        </div>
        <div class="cart-content">
            <!-- 列表显示购物清单 -->
            <div class="cart-content-main" v-for="(item, index)  in userCartList" :key="item.index">
                <div class="cart-info">
                    <img :src="`http://127.0.0.1:8000/media/${productDictList[item.fields.product_id].fields.product_image}`" alt=""
                    height="150px" width="150px">
                    <span>{{productDictList[item.fields.product_id].fields.product_name}}</span>
                </div>
                <div class="cart-price">
                    ￥ {{productDictList[item.fields.product_id].fields.product_cost}}
                </div>
                <div class="cart-count">
                    <span class="cart-control-minus"
                          @click="handleCount(index, -1)">-</span>
                    {{item.fields.num}}
                    <span class="cart-control-add"
                          @click="handleCount(index, 1)">+</span>
                </div>
                <div class="cart-cost">
                    ￥ {{productDictList[item.fields.product_id].fields.product_cost * (item.fields.num-0.0)}}
                </div>
            </div>
            <div class="cart-empty" v-if="!userCartList.length">无商品</div>
        </div>
        <div class="cart-footer" v-show="userCartList.length">
            <div class="cart-footer-desc">
                共计 <span>{{countAll}}</span>
            </div>
            <div class="cart-footer-desc">
                应付总额 <span>{{costAll - promotion}}</span>
                <br>
                <template v-if="promotion">
                    (优惠<span>￥ {{promotion}} </span>)
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "order_cart",
        data(){
            return {
                promotion: 0,
                promotionCode: '',
                userCartList:[],  //从cart表取到的原数据
                cartProductList:[],  //cart表里包含的product表的原数据
                productList: [],
                productDictList:[]  //product_id -> product
            }
        },
        computed: {
            //订单商品总数
            countAll(){
                let count = 0;
                this.userCartList.forEach(item => {
                    count += item.fields.num;
                });
                return count;
            },//订单商品总价
            costAll(){
                let cost = 0;
                this.userCartList.forEach(item => {
                    cost += this.productDictList[item.fields.product_id].fields.product_cost * (item.fields.num-0.0);
                    console.log(this.productDictList[item.fields.product_id].fields.product_cost * (item.fields.num-0.0));
                    console.log((item.fields.num-0.0));
                    console.log(this.productDictList[item.fields.product_id].fields.product_cost);
                });
                return cost;
            }

        },
        methods: {
            //通知Vuex,完成下单
            async handleOrder(){

              console.log("thisthis");
              await this.axios.get('add_order/',
                  {params:{user_id: this.$store.state.userId}})
              .then((response) => {
                  console.log(response);
                  //this.list = response.data.list

              })
              .catch(function (error) {
                  console.log(error);

              });
              console.log("this end");

              var i = this.userCartList.length
              for (; i>0; i--) {
                await this.handleDelete(0)
              }



              window.alert('购买成功');


            },

            async handleCount(index,count) {
              await this.axios.get('edit_num_in_cart/',
                  {
                    params: {
                      user_id: this.$store.state.userId,
                      product_id: this.userCartList[index].fields.product_id,
                      num: count
                    }
                  })
                  .then((response) => {
                    console.log("!!!!!!!!!!!!!!!!!----------");
                    console.log(response);
                    //this.list = response.data.list
                    console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!");
                  })
                  .catch(function (error) {
                    console.log(error);
                  });
              await this.cartList(this.$store.state.userId)
            },

            //订单数据
            async cartList(x1){
              await this.axios.get('show_cart/',{params:{user_id: x1}})
              .then((response) => {
                  console.log(response);
                  this.userCartList = response.data.list
              })
              .catch(function (error) {
                  console.log(error);
              });

              await this.cartProductsList(this.$store.state.userId)

              this.productDictList = {};
              await this.cartProductList.forEach(item => {
                    this.productDictList[item.pk] = item;
                });
            },
          async cartProductsList(x1){
              await this.axios.get('cartProductsList/',{params:{user_id: x1}})
              .then((response) => {
                  console.log(response);
                  this.cartProductList = response.data.list
              })
              .catch(function (error) {
                  console.log(error);
              });

            }
        },

        async created(){
          console.log("cart-create");
          console.log(this.$store.state.userId)
          await this.cartList(this.$store.state.userId)
          console.log("cart-create-success");
          await this.cartProductsList(this.$store.state.userId)
          console.log(this.productDictList);
          console.log(this.productDictList[2].fields.product_cost);


        }
    }
</script>

<style scoped>
    .cart{
        margin: 32px;
        background: #fff;
        border: 1px solid #dddee1;
        border-radius: 10px;
    }
    .cart-header-title{
        padding: 16px 32px;
        border-bottom: 1px solid #dddee1;
        border-radius: 10px 10px 0 0;
        background: #f8f8f9;
    }
    .cart-header-main{
        padding: 8px 32px;
        overflow: hidden;
        border-bottom: 1px solid #dddee1;
        background: #eee;
        overflow: hidden;
    }
    .cart-empty{
        text-align: center;
        padding: 32px;
    }
    .cart-header-main div{
        text-align: center;
        float: left;
        font-size: 14px;
    }
    div.cart-info{
        width: 60%;
        text-align: left;
    }
    .cart-price{
        width: 10%;
    }
    .cart-count{
        width: 10%;
    }
    .cart-cost{
        width: 10%;
    }
    .cart-delete {
        width: 10%;
    }
    .cart-content-main{
        padding: 0 32px;
        height: 60px;
        line-height: 60px;
        text-align: center;
        border-bottom: 1px dashed #e9eaec;
        overflow: hidden;
    }
    .cart-content-main div{
        float: left;
    }
    .cart-content-main img{
        width: 40px;
        height: 40px;
        position: relative;
        top: 10px;
    }
    .cart-control-minus,
    .cart-control-add{
        display: inline-block;
        margin: 0 4px;
        width: 24px;
        height: 24px;
        line-height: 22px;
        text-align: center;
        background: #f8f8f9;
        border-radius: 50%;
        box-shadow: 0 1px 1px rgba(0,0,0,.2);
        cursor: pointer;
    }
    .cart-control-delete{
        cursor: pointer;
        color: #2d8cf0;
    }
    .cart-promotion{
        padding: 16px 32px;
    }
    .cart-control-promotion,
    .cart-control-order{
        display: inline-block;
        padding: 8px 32px;
        border-radius: 6px;
        background: #2d8cf0;
        color: #fff;
        cursor: pointer;
    }
    .cart-control-promotion{
        padding: 2px 6px;
        font-size: 12px;
        border-radius: 3px;
    }
    .cart-footer{
        padding: 32px;
        text-align: right;
    }
    .cart-footer-desc{
        display: inline-block;
        padding: 0 16px;
    }
    .cart-footer-desc span{
        color: #f2352e;
        font-size: 20px;
    }
</style>