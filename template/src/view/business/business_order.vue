<template>
  <div>
    <v-container fluid>
      <v-toolbar
          dark
          color="blue darken-3"
          class="mb-1"
      >
        <v-spacer></v-spacer>
        <v-toolbar-title>
          <h4>订单信息</h4>
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>

      <v-col class="ml-3">
          <v-tabs>
            <v-tabs-slider color="blue"></v-tabs-slider>
            <v-tab>买家未付款</v-tab>
            <v-tab>商家未发货</v-tab>
            <v-tab>商家已发货</v-tab>
            <v-tab>买家已收货</v-tab>
            <v-tab>买家已确认订单</v-tab>

            <!-- 买家未付款 -->
            <v-tab-item>
              <Order_content></Order_content>
            </v-tab-item>

            <!-- 商家未发货 -->
            <v-tab-item>
              <Order_content></Order_content>
            </v-tab-item>

            <!-- 商家已发货 -->
            <v-tab-item>
              <v-card flat>
                <Order_content></Order_content>
              </v-card>
            </v-tab-item>

            <!-- 买家已收货 -->
            <v-tab-item>
              <Order_content></Order_content>
            </v-tab-item>

            <!-- 买家已确认订单 -->
            <v-tab-item>
              <Order_content></Order_content>
            </v-tab-item>
          </v-tabs>
      </v-col>
    </v-container>
  </div>
</template>

<script>
import Order_content from "@/components/business/order_content";
export default {
  name: "business_order",
  components: {Order_content},
  data () {
    return {
    }
  },
}
</script>

<style scoped>

</style>