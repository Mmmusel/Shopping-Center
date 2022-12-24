<template>

  <div class="home">
    <div class="header">头部</div>

    <template v-if="show">
      <div class="header">
        <router-link to="/customerHome"
                     class="header-title">电商网站首页</router-link>
    <br><br>
    <v-avatar class="name" color="orange" size="62">
      <span class="white--text headline">{{user}}</span>
    </v-avatar>

        <!--
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
        -->
        <div class="header-menu">
          <router-link to="/cart"
                       class="header-menu-cart">
            购物车
            <span v-if="cartList.length">{{cartList.length}}</span>
          </router-link>
        </div>

        <!--搜索框-->
    <div class="container" id="div1" align="center">
      <v-row align="center">
      <div class="search_bar1">
        <form>
          <input type="text" v-model="inputText" placeholder="请输入您要搜索的内容...">

        </form>
        </div>
        <div class="search bar1">
      <button @click="Click"> <img src="../../assets/search.png" width="25px" height="25px"> </button>
        </div>
    </v-row>
    </div>
        <!--
        <div class="header-menu">
          <router-link to="/login/logout"
                       class="header-menu-cart">
            退出登录
          </router-link>
        </div>
        -->
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
      inputText:'',
      statuss:0,
      image:'http://127.0.0.1:8000/media/'+'avatar/airPods.jpg',
        form: {
          goods_image: '',
        }
    }
  },
  watch:{
    statuss:function() {
      if(this.statuss>0){
        //window.location.href = '/#/business/searchOut';
        console.log(this.$store.state.searchText)
      }
    }
  },
  methods: {

    async Click(){
      if(this.inputText===''){
        window.alert('请输入搜索内容')
        return
      }
      this.$store.state.searchText=this.inputText
      //window.location.href = '/#/business/searchOut';
      //window.event.returnValue=false
      this.$router.push({path: '/searchOut'})
      //this.statuss+=1;


    }
    /*async onSubmit(){
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
    }*/
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

.container {
  width: 5000px;
  margin: 50px auto;
  overflow: hidden;
  border: 1px solid #fdfdfe;
  position: center;

}
.search_bar1 {
  background-color: rgb(63, 150, 245);
  height: 50px;
  width:800px;
  overflow: hidden;
  border-radius: 3px;
  margin-left: 200px;
  box-sizing: border-box;
  padding: 5px;}
input {
  width: 100%;
  height: 40px;
  box-sizing: border-box;
  border: 0;
  border-radius: 3px;
  margin: 0;
  padding: 0px 40px 0px 10px;
  outline: 0;
  font-size: 14px;
  color: #949494;
  background-color: #fff;
}
input::-webkit-input-placeholder {
  color: #8c8c8c;
}
</style>