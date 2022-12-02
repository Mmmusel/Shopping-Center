<template>
  <div class="home">
    <div class="header">头部</div>
    <template v-if="show">
      <div class="header">
        <router-link to="/customerHome"
                     class="header-title">电商网站首页</router-link>
        <div class="header-menu">
          {{user}}
        </div>
        {% csrf_token %}
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="商品图片">
            <input type="file" @change="getImageFile" id="img">
            <img :src="image"/>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">确认添加</el-button>
          </el-form-item>
        </el-form>
        <div class="header-menu">
          <router-link to="/cart"
                       class="header-menu-cart">
            购物车
            <span v-if="cartList.length">{{cartList.length}}</span>
          </router-link>
        </div>

        <div class="header-menu">
          <router-link to="/login/logout"
                       class="header-menu-cart">
            退出登录
          </router-link>
        </div>
        <customerList></customerList>
      </div>
      <router-view></router-view>
    </template>
    <!-- 挂载所有路由 -->
    <router-view></router-view>
  </div>
</template>

<script>
import customerList from "./customer_list.vue"
export default {
  components: {
    customerList
  },
  data(){
    return {
      user: '',
      image:'http://127.0.0.1:8000/media/'+'avatar/airPods.jpg',
      //image:'',
        form: {

          goods_image: '',

        }
    }
  },
  methods: {
     getImageFile:function(e) {
       this.form.goods_image = e.target.files[0];
    },
    async onSubmit(){
      console.log("good");
      let formData = new FormData();
      formData.append('goods_image', this.form.goods_image);

      var configs = {
        headers:{'Content-Type':'multipart/form-data'}
      }
      await this.axios.post('add_product/',formData, configs).then(response => {
        if(response.data.msg==="success"){
          this.image = 'http://127.0.0.1:8000/media/'+response.data.image
          console.log(response)
        }
      })
    }
  },
  computed: {
    cartList(){
      return this.$store.state.cartList;
    },
    show(){
      return true;
    }
  },
  async created(){
    await this.axios.get('userId2userName/',{params:{user_id: this.$store.state.userId}})
        .then((response) => {
          console.log("ttttttttttttttttt");
            console.log(this.$store.state.userId);
            console.log(response.data.user_name);
            console.log("ttttttttttttttttt");
            this.user = response.data.user_name
        })
        .catch(function (error) {
            console.log(error);
        });
  }
}
</script>

<style scoped>
.header {
  position: absolute;
  line-height: 40px;
  top: 0px;
  left: 0px;
  right: 0px;
}
body{
  margin:0;
}
</style>