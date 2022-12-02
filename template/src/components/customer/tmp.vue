<template>
  <div>
    <div class="text-center">
      <v-app-bar
          color="blue"
          width="10dp"
          elevation="3"
          dense
          fixed
      >
        <v-app-bar-nav-icon
            @click="drawer = true">
        </v-app-bar-nav-icon>
      </v-app-bar>

      <v-navigation-drawer
          class="white"
          v-model="drawer"
          absolute temporary
          app
      >
        <v-row
            color="white"
            class="pa-4"
        >

          <v-avatar color="blue">
            <span class="white--text text-h5">CJ</span>
          </v-avatar>

          <div>12345678</div>
        </v-row>

        <v-divider></v-divider>

        <v-list>
          <v-list-item
              v-for="link in links"
              :key="link.text"
              router :to="link.route"
          >
            <v-list-item-action>
              <v-icon class="blue--text lighten-3">{{link.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="black--text">{{link.text}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn block>
              退出登录
            </v-btn>
          </div>
        </template>
      </v-navigation-drawer>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
//import test from './components/test';

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    cards: ['Today', 'Yesterday'],
    drawer: null,
    links:[{ text: '首页', icon: 'mdi-inbox-arrow-down',route:"/customerHome"},
          { text: '个人中心', icon: 'mdi-send',route:"/customerPerson"},
          { text: '历史订单', icon: 'mdi-alert-octagon',route:"/customerOrder2"},],
  }),
};
</script>

