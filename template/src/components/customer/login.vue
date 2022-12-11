<template>
  <v-app id="main_page">
    <div class="login-info">
        <template v-if="login">
            <form class="login-info-form">
                <p>登陆界面</p><br>
                <span>用户账号: </span><input type="text" v-model="username" placeholder=""/><br>
                <span>用户密码: </span><input type="password" v-model="password"/><br><br>
                <input class="submit" type="button" @click="goHome" value="提交">
                <input class="submit" type="button" @click="changeLogin(false, true)" value="前往注册">
            </form>

        </template>
        <template v-if="register">
            <form class="login-info-form">
                <p>注册界面</p><br>
                <span>用户账号: </span><input type="text" v-model="username" placeholder=""/><br>
                <span>用户密码: </span><input type="password" v-model="password"/><br>
                <span>确认密码: </span><input type="password" v-model="confirmPassword"/><br><br>
              <v-row justify="center">

    <label><input v-model="radioVal" type="radio" value="用户" @change="getRadioVal">用户</label>
    <label><input v-model="radioVal" type="radio" value="商家" @change="getRadioVal">商家</label>



                <!--
                <v-radio-group class="choose" justify="center" v-model="row"  row :mandatory="false" @change="selectID">
                  <v-radio label="用户" value="radio-1" v-model="register_type1"></v-radio>
                  <v-radio label="商家" value="radio-2" v-model="register_type2"></v-radio>
                  <v-radio label="管理员" value="radio-3" v-model="register_type3"></v-radio>
                </v-radio-group>
                -->
              </v-row><br><br>
                <input class="submit" type="button" @click="goLogin" value="提交">
                <input class="submit" type="button" @click="changeLogin(true, false)" value="已有账号">
            </form>
        </template>
    </div>
    </v-app>
</template>

<script>
    import util from './util';
    export default {
        name: "login_View",
        data(){
            return {
                login: false,
              radioVal:'用户',
                register: true,
                username: '',
                password: '',
                confirmPassword: '',
                res: false,  //数据库操作返回值
                userId: 0  //当前登录的用户

            }
        },
        methods: {
          getRadioVal(){},
           async  goLogin(){

                if(!util.trim(this.username) || !util.trim(this.password) ){ //TODO 111
                    window.alert('账号或密码不能为空');
                    return;
                }
                if(this.password !== this.confirmPassword){
                    window.alert('密码不一致，请重新输入');
                    this.password = '';
                    this.confirmPassword = '';
                }else{
                  //把注册信息写进数据库
                  await this.addUserInfo(this.username,this.password)

                  //res返回值 标志是否有重名
                  if(this.res) {
                    this.register = false;

                    //设置当前登陆状态；用于下次打开页面的默认登录
                    window.localStorage.setItem('loginStatus', 'login');

                    //把用户【id】保存在vuex，便于home页面使用
                    //this.$store.commit('getUser', this.username);
                    await window.localStorage.setItem('userId', this.userId);
                    this.$store.commit('editUserId', this.userId);
                    window.alert('注册成功，确定进入网站首页');
                    if(this.radioVal==='用户'){
                    window.location.href = '/#/customerHome';
                  }else{
                    window.location.href = '/#/business';
                  }
                  } else {
                    window.alert('用户名重复，请再次尝试');
                    this.username = '';
                    this.password = '';
                    this.confirmPassword = ''
                  }
                }
          },
          changeLogin(b1, b2){
              this.login = b1;
              this.register = b2;
          },
          async goHome(){
              if(!util.trim(this.username) || !util.trim(this.password) ){
                  window.alert('账号或密码不能为空');
                  return;
              }

              await this.searchUserInfo(this.username,this.password)

              if(this.res){
                  this.login = false;
                  window.localStorage.setItem('loginStatus', 'login');
                  await window.localStorage.setItem('userId', this.userId);
                  this.$store.commit('editUserId', this.userId);
                  console.log(this.userId);
                  //console.log(error);
                  window.alert('登陆成功，进入网站首页');

                  if(this.radioVal==='用户'){
                    window.location.href = '/#/customerHome';
                  }else{
                    window.location.href = '/#/business';
                  }

              }else{
                  window.alert('账号或密码错误');
              }
          },

          async addUserInfo (x1,x2) {
            await this.axios.get('add_userInfo/',
                {params:{user_name: x1,user_password: x2,user_type:this.radioVal}})
              .catch(function (error) {
                  console.log(error);
                  this.res=false
              })
              .then((response) => {
                if(response.data.error_num!==0){
                  this.res=false
                  console.log(response.data.msg);
                  return
                }
                  console.log(response.data.msg);
                  this.userId = response.data.userId
                this.res=true
              })
              ;
          },

          async getType(){
            await this.axios.get('search_usertype/',{params:{user_id:this.$store.state.userId }})
              .catch(function (error) {
                  console.log(error);

              })
              .then((response) => {

                this.radioVal=response.data.user_type

              })
              ;
          }
          ,

          async searchUserInfo (x1,x2) {
            await this.axios.get('search_userInfo/',{params:{user_name: x1,user_password: x2}})
              .catch(function (error) {
                  console.log(error);
                  console.log(x1);
                  console.log(x2);



                  this.res=false
              })
              .then((response) => {
                if(response.data.error_num!==0){
                  this.res=false
                  console.log(response.data.msg);
                  return
                }
                this.res=true

                console.log(response.data);
                this.userId = response.data.userId
                this.radioVal=response.data.user_type

              })
              ;
          }
        },
        async created(){
            //获取路由中的参数
            if(this.$route.params.loginStatus === 'logout'){
                window.localStorage.removeItem('loginStatus')

                this.$store.commit('getLoginStatus', false);
                return;
            }

            const loginStatus = this.$store.state.loginStatus;

            if(loginStatus){

                this.login = false;
                this.register = false;
                await this.getType()
                window.alert('您已经是登录状态')
                if(this.radioVal==='用户'){
                    window.location.href = '/#/customerHome';
                  }else{
                    window.location.href = '/#/business';
                  }
            }
        }
    }
</script>

<style scoped>
.choose{
  margin: auto;
  position: absolute;
}
  .textinput{
    outline-style: none ;
    border: 1px solid #ccc;
    border-radius: 3px;
    padding: 6px;
    width: 300px;
    font-size: 14px;
  }

 .login-info{
        height:100%;
        width:100%;
        text-align: center;
    }
    .login-info-form{
        position: relative;
        top: 100px;
    }
    p{
         font-size: 26px;
         color: #5c6b77;
     }
    .submit{
      width: 200px;/*设置按钮宽度*/
      height: 30px;/*设置按钮高度*/
      color:white;/*字体颜色*/
      background-color:cornflowerblue;/*按钮背景颜色*/
      border-radius: 3px;/*让按钮变得圆滑一点*/
      border-width: 0;/*消去按钮丑的边框*/
      margin: 0;
      outline: none;/*取消轮廓*/
      font-size: 17px;/*设置字体大小*/
      text-align: center;/*字体居中*/
      cursor: pointer;/*设置鼠标箭头手势*/
    }
    span{
        font-size: 16px;
        color: #5c6b77;
    }
</style>
