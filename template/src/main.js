import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router/index'
//import router from './router/index' //导入刚刚在route文件下定义的router
import store from './components/customer/store'
import ElementUI from "element-ui";
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)


new Vue({
  vuetify,
  router, // 引入路由
  render: h => h(App),
  store
}).$mount('#app')

Vue.config.productionTip = false
Vue.use(router)
Vue.use(ElementUI)
