<template>
  <v-expansion-panels focusable>
    <v-expansion-panel
        v-for="item in items"
        :key="item.name"
    >
      <v-expansion-panel-header>
        <!--蓝底头像+用户名-->
        <v-col>
          <v-avatar
            :color="item.color"
            size="56"
            class="white--text"
          >
            {{ item.name }}
          </v-avatar>
        </v-col>
        <!--用户名-->
        <v-col>
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-col>
        <!--地址-->
        <v-col>
          <v-list-item-title>{{ item.address }}</v-list-item-title>
        </v-col>

        <!-- 提醒付款：需要消息系统，后续实现-->
        <v-col>
          <v-btn
            class="ma-2"
            :loading="loading"
            :disabled="loading"
            color="success"
            @click="loader = 'loading'"
          >
            {{btn_content}}
            <template v-slot:loader>
              <span>Loading...</span>
            </template>
          </v-btn>
        </v-col>
      </v-expansion-panel-header>

      <v-expansion-panel-content>
        <Order_cart></Order_cart>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script>
import Order_cart from "@/components/business/order_cart";
export default {
  name: 'order_weifukuan',
  components: {Order_cart},
  data: () => ({
    items: [
      {color: '#2196F3', name: 'lzh', address: '北京', dingdan:'111'},
      {color: '#90CAF9', name: 'lyq', address: '山东', dingdan:'222'},
      {color: '#64B5F6', name: 'lr', address: '湖南', dingdan:'333'},
      {color: '#42A5F5', name: 'lzh', address: '北京', dingdan:'444'},
      {color: '#1E88E5', name: 'lyq', address: '山东', dingdan:'555'},
      {color: '#1976D2', name: 'lr', address: '湖南', dingdan:'666'},
    ],
    // 用户头像颜色，此处没有使用图片，后续可以考虑改为用户头像
    //colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],

    /* 可以使用订单类？
     * 从每个订单类中查找用户名、商品名和对应的商品数量
     */

    btn_content: '提醒付款',
    loader: null,
    loading: false,
  }),

  watch: {
    loader () {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 500)

      this.loader = null
    },
  },
}
</script>