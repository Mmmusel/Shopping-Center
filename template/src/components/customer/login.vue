<template>
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
                <input class="submit" type="button" @click="goLogin" value="提交">
                <input class="submit" type="button" @click="changeLogin(true, false)" value="已有账号">
            </form>
        </template>
    </div>
</template>

<script>
    import util from './util';
    export default {
        name: "login_View",
        data(){
            return {
                login: false,
                register: true,
                username: '',
                password: '',
                confirmPassword: '',
                res: false,  //数据库操作返回值
                userId: 0  //当前登录的用户
            }
        },
        methods: {
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
                    window.location.href = '/#/customerHome';
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
                  window.alert('登陆成功，确定进入网站首页');
                  window.location.href = '/#/customerHome';
              }else{
                  window.alert('账号或密码错误');
              }
          },

          async addUserInfo (x1,x2) {
            await this.axios.get('add_userInfo/',{params:{user_name: x1,user_password: x2}})
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

              })
              ;
          }
        },
        created(){
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
                window.alert('您已经是登录状态')
                window.location.href = '/#/customerHome'
            }
        }
    }
</script>

<style scoped>
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
        font-size: 18px;
    }
    span{
        font-size: 16px;
        color: #5c6b77;
    }
</style>