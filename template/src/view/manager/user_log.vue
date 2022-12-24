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
<v-list-item
            v-for="item in business_lists"
            :key="item.title"
        >

          <v-list-item-content>
            <v-row>

        <!--用户名-->
        <v-col>
          <v-list-item-title>{{ item.fields.log_name }}</v-list-item-title>
        </v-col>

        <v-col>
          <v-list-item-title>{{ item.fields.log_type  }}</v-list-item-title>
          </v-col>
 <v-col>
          <v-list-item-title>{{ item.fields.log_time | format  }}</v-list-item-title>

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
      headers: [
        {
          text: '用户名',
          align: 'start',
          sortable: false,
          value: '用户名',
        },
        { text: '身份', value: '身份' },
        { text: '时间', value: 'time' },
        { text: 'IP地址', value: 'ip' },
      ],
      business_lists:[],
      desserts: [
        {
          用户名: "a",
          身份: "用户",
          time: "2022-10-1",
          ip: "山东德州新湖"
        }
      ],
    }
  },
  async created() {
    await this.axios.get('get_user_log/',
          {params:{}})
        .then((response) => {
            console.log(response);
            this.business_lists = response.data.list;

            this.business_lists.forEach(item => {
                    item.fields['region']={
                      province:item.fields.log_province,
                      city:item.fields.log_city,
                      area:item.fields.log_area,
                      town:''
                    }

                });

            this.desserts=[]
          this.business_lists.forEach(item => {
                    this.desserts.push({
          用户名: item.fields.log_name,
          身份: item.fields.log_type,
          time: item.fields.log_time,
          ip: item.fields.region
        },)

                });

        })
        .catch(function (error) {
            console.log(error);
        });
  }
}
</script>
