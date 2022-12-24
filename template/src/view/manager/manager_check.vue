<template>
  <div>
    <br><br><br>
    <v-card
        max-width="1200"
        class="mx-auto"
    >
      <v-toolbar
          color="light-blue"
          dark
      >

        <v-toolbar-title>商家申请审核</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>

      <v-list two-line subheader>
        <v-subheader inset>待审核</v-subheader>

        <v-list-item
            v-for="item in items"
            :key="item.title"
        >
          <v-list-item-avatar>
            <v-icon
                :class="[item.iconClass]"
                v-text="item.icon"
            ></v-icon>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title v-text="item.title"></v-list-item-title>
            <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-content>
            <v-list-item-title v-text="item.location"></v-list-item-title>
            <v-list-item-subtitle v-text="item.other"></v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn small @click="pass">通过</v-btn>
          </v-list-item-action>
          <v-list-item-action>
            <v-btn small @click="ban">禁止</v-btn>
          </v-list-item-action>
        </v-list-item>

        <v-divider inset></v-divider>

        <v-subheader inset>已审核</v-subheader>

        <v-list-item
            v-for="item in items2"
            :key="item.title"
        >
          <v-list-item-avatar>
            <v-icon
                :class="[item.iconClass]"
                v-text="item.icon"
            ></v-icon>
          </v-list-item-avatar>

          <v-row no-gutters>
            <v-col
                :cols=11
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
                <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
              </v-list-item-content>
            </v-col>
            <v-col
                :cols=1
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.status"></v-list-item-title>
              </v-list-item-content>
            </v-col>
          </v-row>


        </v-list-item>
      </v-list>
    </v-card>
  </div>

</template>

<script>
export default {
  data: () => ({
    //店家申请审核时需要的信息
    items: [
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
    { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },
        { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Photos', subtitle: 'Jan 9, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Recipes', subtitle: 'Jan 17, 2014', location: "山东" , other: "xxxx" },
      { icon: 'folder', iconClass: 'grey lighten-1 white--text', title: 'Work', subtitle: 'Jan 28, 2014',location: "山东" , other: "xxxx" },

    ],
    items2: [
      { icon: 'assignment', iconClass: 'blue white--text', title: 'Vacation itinerary', subtitle: 'Jan 20, 2014' , status: "未通过"},
      { icon: 'call_to_action', iconClass: 'amber white--text', title: 'Kitchen remodel', subtitle: 'Jan 10, 2014' , status: "已通过" },
    ],
  }),
  methods: {
    pass () {

    },
    add () {

    }
  }
}
</script>
