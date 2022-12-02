import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            component: () => import('@/view/login'),
        },
        {
            path: '/customer',
            component: (resolve) => require(['../components/customer/tmp'], resolve),
            children: [
                {
            path: '/customerHome',
            meta: {
                title: '首页'
            },
            component: (resolve) => require(['../components/customer/customer_Home'], resolve)
        },
        {
            path: '/list',
            meta: {
                title: '首页'
            },
            component: (resolve) => require(['../components/customer/customer_list'], resolve)
        },
        {
            path: '/product/:id',
            meta: {
                title: '商品详情'
            },
            component: (resolve) => require(['../components/customer/customer_product_view.vue'], resolve)
        },
        {
            path: '/cart',
            meta: {
                title: '购物车'
            },
            component: (resolve) => require(['../components/customer/customer_cart.vue'], resolve)
        },
        {
            path: '/login/:loginStatus',
            meta: {
                title: '登录注册'
            },
            component: (resolve) => require(['../components/customer/login.vue'], resolve)
        },
        {
            path: '/customerPerson',
            meta: {
                title: '个人中心'
            },
            component: (resolve) => require(['../components/customer/customer_personal'], resolve)
        },
        {
            path: '/customerOrder2',
            meta: {
                title: '我的订单2'
            },
            component: (resolve) => require(['../components/customer/orderTry'], resolve)
        },
        {
            path: '*',
            redirect: '/login/login',
            //component: (resolve) => require(['../components/customer/login'], resolve)
            component: (resolve) => require(['../components/customer/customer_Home.vue'], resolve)
        }
            ]
        },

        {
            path: '/business',
            component: () => import('@/view/business/business'),
            children: [
                {
                    path : 'home',
                    component: () => import('@/view/business/business_home')
                },
                {
                    path : 'order',
                    component: () => import('@/view/business/business_order')
                },
                {
                    path : 'commodity',
                    component: () => import('@/view/business/business_commodity')
                },
                {
                    path : 'saledata',
                    component: () => import('@/view/business/business_home')
                },
                {
                    path : 'information',
                    component: () => import('@/view/business/business_information')
                }
            ]
        }
    ],
    mode: "hash" // 去除访问时候带#问题
})

