<!-- business主页面 -->
<template>
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
        fixed
        app
    >
      <v-row
          color="white"
          class="pa-4"
      >
        <v-avatar color="blue">
            <span class="white--text text-h5">{{ this.user }}</span>
          </v-avatar>

          <div>{{ this.user }}</div>
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
          <router-link to="/login/logout">
          <v-btn block>
            退出登录
          </v-btn>
            </router-link>
        </div>
      </template>
    </v-navigation-drawer>

    <div style="height: 3rem;"></div>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'manager_main',

  components: {

  },

  data: () => ({
    drawer: null,
    user:"",
    links:[{ text: '审核商品', icon: 'mdi-inbox-arrow-down',route:"/manager/check"},
      { text: '登录日志', icon: 'mdi-send',route:"/manager/log"},
      { text: '操作日志', icon: 'mdi-delete',route:"/manager/actionlog"},
      ],
  }),
  async created(){
    await this.axios.get('userId2userName/',{params:{user_id: this.$store.state.userId}})
        .then((response) => {

            this.user = response.data.user_name
        })
        .catch(function (error) {
            console.log(error);
        });
  }
};
</script>

