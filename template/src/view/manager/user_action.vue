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
          <h4>用户操作日志{{num}}条</h4>
        </v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
<v-list-item
            v-for="item in business_lists"
            :key="item.title"
        >

          <v-list-item-content>
            <v-row>

        <!--用户名-->
        <v-col>
          <v-list-item-title>{{ item.fields.action_name }}</v-list-item-title>
        </v-col>

        <v-col>
          <v-list-item-title>{{ item.fields.action_type  }}</v-list-item-title>
          </v-col>
 <v-col>
          <v-list-item-title>{{ item.fields.action_time | format  }}</v-list-item-title>

        </v-col>
              <v-col >
          <!--<v-list-item-title>{{ item.address }}</v-list-item-title>-->
                <div v-if="item.fields.region.area!==''">
          <region-text
                  separator="-"
                  :town="false"
                  v-model="item.fields.region"
          /></div>
        </v-col>
              <v-col>
          <v-list-item-title>{{ item.fields.action  }}</v-list-item-title>

        </v-col>

              </v-row>
          </v-list-item-content>

        </v-list-item>
    </v-container>
  </div>
</template>


<script>
import {RegionText} from "v-region";

export default {
    components: {

    RegionText
  },
  data () {
    return {

      business_lists:[],
      num:0,

    }
  },
  async created() {
    await this.axios.get('get_user_action_log/',
          {params:{}})
        .then((response) => {
            console.log(response);
            this.business_lists = response.data.list;

            this.business_lists.forEach(item => {
                    item.fields['region']={
                      province:item.fields.action_province,
                      city:item.fields.action_city,
                      area:item.fields.action_area,
                      town:''
                    }});
        })
        .catch(function (error) {
            console.log(error);
        });

    await this.axios.get('get_user_action_num/',
          {params:{}})
        .then((response) => {
            console.log(response);
            this.num = response.data.num;

            this.business_lists.forEach(item => {
                    item.fields['region']={
                      province:item.fields.action_province,
                      city:item.fields.action_city,
                      area:item.fields.action_area,
                      town:''
                    }});
        })
        .catch(function (error) {
            console.log(error);
        });
  }
}
</script>
