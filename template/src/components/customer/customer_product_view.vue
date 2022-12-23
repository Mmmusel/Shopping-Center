<template>
  <div v-if="product">
    <div class="product">
      <!-- 商品图片、名称、价格 -->
      <div class="product-image">
        <img :src="`http://127.0.0.1:8000/media/${product.fields.product_image}`" alt="">
      </div>
      <div class="product-info">
        <h1 class="product-name">{{product.fields.product_name}}</h1>
        <div class="product-cost">{{product.fields.product_cost}}</div>
        <div class="product-add-cart" @click="handleAddCart">加入购物车</div>
      </div>



      <div>
        <span class="fillheart" v-if="begood" @click="changeGood">
            <font-awesome-icon :icon="['fas', 'heart']" class="icon righticon" ></font-awesome-icon>
        </span>
        <span class="heart" v-if="!begood" @click="changeGood">
            <font-awesome-icon :icon="['fas', 'heart']" class="icon righticon" ></font-awesome-icon>

        </span>

        <span class="word">{{product_goods}}</span>
    </div>

      </div>
    <div class="product-desc">
      <h2>商家详情</h2>
      <router-link :to="'/shop/' + product.fields.product_business">
        点击进入商家主页

      </router-link>
       <div>
        <span class="fillstar" v-if="bestar" @click="changeStar">
            <font-awesome-icon :icon="['fas', 'star']" class="icon righticon" ></font-awesome-icon>
        </span>
        <span class="star" v-if="!bestar" @click="changeStar">
            <font-awesome-icon :icon="['fas', 'star']" class="icon righticon" ></font-awesome-icon>

        </span>

        <span class="word">{{shop_stars}}</span>
    </div>
    </div>


    <div class="product-desc">
      <h2>产品介绍</h2>
      <img :src="`http://127.0.0.1:8000/media/${product.fields.product_imageDetail}`" alt="">
    </div>
  </div>
</template>

<script>
//导入本地数据
//import product_data from './product.js';

export default {
  data(){
    return {
      //获取路由中的参数
      id: parseInt(this.$route.params.id),
      product: null,
      product_goods:0,
      begood:true,
      bestar:true,
      shop_stars:0,
    }
  },
  methods: {
    async getProductLikes(){
      await this.axios.get('get_product_likes/',
            {params:{ product_id: this.id}})
        .then((response) => {
            console.log(response);
           this.product_goods=response.data.goods

        })
        .catch(function (error) {
            console.log(error);
        });

      await this.axios.get('get_shop_stars/',
            {params:{ business_id: this.product.fields.product_business}})
        .then((response) => {
            console.log(response);
           this.shop_stars=response.data.stars

        })
        .catch(function (error) {
            console.log(error);
        });
    },
    async changeGood(){
      if(this.begood){
        this.product_goods-=1
      }else{
        this.product_goods+=1
      }
      this.begood=!this.begood

      await this.axios.get('toggle_user_like_to_product/',
            {params:{user_id: this.$store.state.userId, product_id: this.id}})
        .then((response) => {
            console.log(response);

        })
        .catch(function (error) {
            console.log(error);
        });
    },
    async changeStar(){
      if(this.bestar){
        this.shop_stars-=1
      }else{
        this.shop_stars+=1
      }
      this.bestar=!this.bestar

      await this.axios.get('toggle_user_star_to_shop/',
            {params:{user_id: this.$store.state.userId, business_id: this.product.fields.product_business}})
        .then((response) => {
            console.log(response);

        })
        .catch(function (error) {
            console.log(error);
        });
    },
    async initUserToProduct(){
      await this.axios.get('get_user_like_to_product/',
            {params:{user_id: this.$store.state.userId, product_id: this.id}})
        .then((response) => {
            console.log(response);
            //this.list = response.data.list
          if(response.data.good==='good'){
            this.begood=true
          }else{
            this.begood=false
          }

        })
        .catch(function (error) {
            console.log(error);
        });

      await this.axios.get('get_user_star_to_shop/',
            {params:{user_id: this.$store.state.userId, business_id: this.product.fields.product_business}})
        .then((response) => {
            console.log(response);
            //this.list = response.data.list
          if(response.data.star==='star'){
            this.bestar=true
          }else{
            this.bestar=false
          }

        })
        .catch(function (error) {
            console.log(error);
        });
    },


    async getProduct(x1){
      await this.axios.get('fetch_product/',{params:{product_id: x1}})
        .then((response) => {
            console.log(response);
            this.product = response.data.product
        })
        .catch(function (error) {
            console.log(error);

        });
    },
    async handleAddCart(){

      await this.axios.get('add_to_cart/',
            {params:{user_id: this.$store.state.userId, product_id: this.id}})
        .then((response) => {
            console.log(response);
            //this.list = response.data.list
            window.alert("添加成功")
        })
        .catch(function (error) {
            console.log(error);
        });
    }
  },
  async created(){
    //初始化数据
    console.log("detailview");
    console.log(this.id);
    await this.getProduct(this.id)
    console.log("detailviewend");
    console.log(this.product)
    await this.initUserToProduct()
    await this.getProductLikes()

  },

  async mounted(){
    //初始化数据
    console.log("11detailview");
    console.log(this.id);
    await this.getProduct(this.id)
    console.log("11detailviewend");
    console.log(this.product)

  }
}
</script>
<!-- scoped属性表示只对当前组件有效，不影响其他组件 -->
<style scoped>
.word{
   font-size: 32px;
}
.fillheart{
color: red;

        font-size: 32px;
}
.heart{
color: gray;

        font-size: 32px;
}

.fillstar{
color: yellow;

        font-size: 32px;
}
.star{
color: gray;

        font-size: 32px;
}

.product{
  margin: 32px;
  padding: 32px;
  background: #fff;
  border: 1px solid #dddee1;
  border-radius: 10px;
  overflow: hidden;
}
.product-image{
  width: 50%;
  height: 550px;
  float: left;
  text-align: center;
}
.product-image img{
  height: 100%;
}
.product-info{
  width: 50%;
  padding: 150px 0 250px;
  height: 150px;
  float: left;
  text-align: center;
}
.product-cost{
  color: #f2352e;
  margin: 8px 0;
}
.product-add-cart{
  display: inline-block;
  padding: 8px 64px;
  margin: 8px 0;
  background: #2d8cf0;
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}
.product-desc{
  background: #fff;
  margin: 32px;
  padding: 32px;
  border: 1px solid #dddee1;
  border-radius: 10px;
  text-align: center;
}
.product-desc img{
  display: block;
  width: 50%;
  margin: 32px auto;
  padding: 32px;
  border-bottom: 1px solid #dddee1;
}
</style>