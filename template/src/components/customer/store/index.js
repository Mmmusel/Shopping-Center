import util from "@/components/customer/util";
import product_data from "@/components/customer/product";
import Vue from "vue"
import Vuex from 'vuex'

//import customer_cart from "@/components/customer/customer_cart";

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

//1.安装插件
Vue.use(Vuex)
const store = new Vuex.Store({
    state: {
        //商品列表信息
        productList: [],
        //购物车数据，数组形式，数据元素为对象（商品id，购买数量count）
        cartList: [],
        //当前用户账号
        username: window.localStorage.getItem('username'),
        userId: parseInt(window.localStorage.getItem('userId')),
        //登录状态
        loginStatus: !!window.localStorage.getItem('loginStatus'),
        searchText:'',
        chooseProductId:-1,
    },
    getters: {
        //品牌、颜色筛选
        brands: state => {
            const brands = state.productList.map(item => item.brand);
            return util.getFilterArray(brands);
        },
        colors: state => {
            const colors = state.productList.map(item => item.color);
            return util.getFilterArray(colors);
        }
    },
    //mutations只能以同步方式
    mutations: {
        //添加商品列表
        setProductList(state, data){
            state.productList = data;
        },
        //添加购物车

        //修改购物车商品数量
        editCartCount(state, payload){
            const product = state.cartList.find(item => item.id === payload.id);
            product.count += payload.count;
        },
        //删除购物车商品
        deleteCart(state, id){
            const index = state.cartList.findIndex(item => item.id === id);
            state.cartList.splice(index, 1)
        },
        //清空购物车
        emptyCart(state){
            state.cartList = [];
        },
        getUser(state, username){
            console.log('username',username)
            state.username = username;
        },
        getLoginStatus(state, flag){
            state.loginStatus = flag;
        },
        editUserId(state,id){
            state.userId=id
            console.log('useridinjs',state.userId)
        }
    },
    actions: {
        //异步请求商品列表，暂且使用setTimeout
        getProductList(context){
            setTimeout(() => {
                context.commit('setProductList', product_data)
            }, 500);
        },
        addCart(state, id){
            this.axios.get('add_to_cart/',
                  {params:{user_id: this.$store.state.userId, product_id: id}})
              .then((response) => {
                  console.log(response);
                  //this.list = response.data.list
                  window.alert("添加成功")
              })
              .catch(function (error) {
                  console.log(error);
              });
            /*const isAdded = state.cartList.find(item => item.id === id);
            //如果不存在设置购物车为1，存在count++
            if(isAdded){
                isAdded.count++;
            }else{
                state.cartList.push({
                    id: id,
                    count: 1
                })
            }*/
        },
        //购买
        buy(context){
            //生产环境使用ajax请求服务端响应后再清空购物车
            return new Promise(resolve => {
                setTimeout(() => {
                    context.commit('emptyCart');
                    resolve();
                }, 500);
            });
        },
    }
});
export default store