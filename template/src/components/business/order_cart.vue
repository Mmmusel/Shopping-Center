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
            <div class="cart-content-main" v-for="(item)  in cart_list" :key="item.index">
                <div class="cart-info">
                    <img :src="`http://127.0.0.1:8000/media/${productDictList[item.fields.product_id].fields.product_image}`" alt=""
                    height="150px" width="150px">
                    <span>{{productDictList[item.fields.product_id].fields.product_name}}</span>
                </div>
                <div class="cart-price">
                    ￥ {{item.fields.order_product_cost}}
                </div>
                <div class="cart-count">

                    {{item.fields.num}}

                </div>
                <div class="cart-cost">
                    ￥ {{item.fields.order_product_cost * (item.fields.num-0.0)}}
                </div>
            </div>
            <div class="cart-empty" v-if="!cart_list.length">无商品</div>
        </div>
        <div class="cart-footer" v-show="cart_list.length">
            <div class="cart-footer-desc">
                共计 <span>{{countAll}}</span>
            </div>
            <div class="cart-footer-desc">
                总额 <span>{{costAll}}</span>
                <br>

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "order_cart",
      props: {
          info: Object,
          orderProducts: Object,
          productDictList: Object,
        },
        data(){
            return {

                userCartList:[],  //从cart表取到的原数据
                cartProductList:[],  //cart表里包含的product表的原数据
                productList: [],
                //productDictList:[] , //product_id -> product

              cart_list:[],

            }
        },
      created(){
          this.orderProducts.forEach(item => {
            if(item.fields.order_id==this.info.pk){
              this.cart_list.push(item)
            }
            });
      },
        computed: {
            //订单商品总数
            countAll(){
                let count = 0;
                this.cart_list.forEach(item => {
                    count += item.fields.num;
                });
                return count;
            },//订单商品总价
            costAll(){
                let cost = 0;
                this.cart_list.forEach(item => {
                    cost += item.fields.order_product_cost * (item.fields.num-0.0);

                });
                return cost;
            }

        },


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