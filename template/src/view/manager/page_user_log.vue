<template>
  <div>

    <v-container fluid>
      <v-data-iterator
          :items="business_lists"
          :items-per-page.sync="itemsPerPage"
          :page="page"
          :search="search"
          hide-default-footer
      >
        <template v-slot:header>
          <v-toolbar
              dark
              color="blue darken-3"
              class="mb-1"
          >
            <v-spacer></v-spacer>
            <v-toolbar-title>
              <h4>用户登录日志</h4>
            </v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>

        <template v-slot:default="props">

          <v-list-item
            v-for="item in props.items"
            :key="item.pk"
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
        </template>

        <template v-slot:footer>
          <v-row class="mt-2" align="center" justify="center">
            <span class="grey--text">Items per page</span>
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                    dark
                    text
                    color="primary"
                    class="ml-2"
                    v-bind="attrs"
                    v-on="on"
                >
                  {{ itemsPerPage }}
                  <v-icon>mdi-chevron-down</v-icon>
                </v-btn>
              </template>
              <v-list>
                <v-list-item
                    v-for="(number, index) in itemsPerPageArray"
                    :key="index"
                    @click="updateItemsPerPage(number)"
                >
                  <v-list-item-title>{{ number }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-spacer></v-spacer>

            <span
                class="mr-4
            grey--text"
            >
            Page {{ page }} of {{ numberOfPages }}
          </span>
            <v-btn
                fab
                dark
                color="blue darken-3"
                class="mr-1"
                @click="formerPage"
            >
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
            <v-btn
                fab
                dark
                color="blue darken-3"
                class="ml-1"
                @click="nextPage"
            >
              <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
          </v-row>
        </template>
      </v-data-iterator>
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
      itemsPerPageArray: [12],
      search: '',
      page: 1,
      itemsPerPage: 12,



      business_lists:[],

    }
  },
  computed: {
    numberOfPages () {
      return Math.ceil(this.business_lists.length / this.itemsPerPage)
    },


  },
  methods: {
    nextPage () {
      if (this.page + 1 <= this.numberOfPages) this.page += 1
    },
    formerPage () {
      if (this.page - 1 >= 1) this.page -= 1
    },
    updateItemsPerPage (number) {
      this.itemsPerPage = number
    },},
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

        })
        .catch(function (error) {
            console.log(error);
        });
  }
}
</script>
