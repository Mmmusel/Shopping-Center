<template>
  <div>
    <v-container fluid>
      <v-data-iterator
          :items="productsList"
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
              <h4>上架商品</h4>
            </v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>

        <template v-slot:default="props">
          <v-row>
            <v-col
                v-for="item in props.items"
                :key="item.fields.product_name"
                cols="12"
                sm="6"
                md="4"
                lg="3"
            >
              <v-card>
                <v-card-title class="subheading font-weight-bold">{{ item.fields.product_name }}</v-card-title>

                <v-divider></v-divider>

                <v-list dense>
                  <v-list-item
                      v-for="(key, index) in myFilteredKeys"
                      :key="index"
                  >
                    <v-list-item-content>{{ key }}:</v-list-item-content>
                    <v-list-item-content class="align-end">{{ item.fields[key] }}</v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card>
            </v-col>
          </v-row>
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
    <v-btn
      class="ma-2"
      color="success"
      @click="addCommodity"
    >
      添加商品
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "business_commodity",
  data () {
    return {
      itemsPerPageArray: [4, 8, 12],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 4,
      keys: [
        '库存',
        '金额',
      ],
      productsList:[],
      items:[
        {
          name: "手机",
          库存: 10000,
          金额: "5000元",
        },
        {
          name: "面包",
          库存: 50000,
          金额: "3元",
        },
        {
          name: "牛奶1",
          库存: 1000,
          金额: "5元",
        },
        {
          name: "牛奶2",
          库存: 1000,
          金额: "5元",
        },
        {
          name: "牛奶3",
          库存: 1000,
          金额: "5元",
        },
        {
          name: "牛奶4",
          库存: 1000,
          金额: "5元",
        },
        {
          name: "牛奶5",
          库存: 1000,
          金额: "5元",
        },

      ],
    }
  },
  computed: {
    numberOfPages () {
      return Math.ceil(this.productsList.length / this.itemsPerPage)
    },
    filteredKeys () {
      return this.keys.filter(key => key !== `Name`)
    },
    myFilteredKeys () {
      if(this.productsList.length!=0){

        //console.log(Object.keys(this.productsList[1].fields))
        return Object.keys(this.productsList[1].fields).filter(key => key !== `product_name`)
      }
      return []
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
    },
    async getProductsList(){
      //从Vuex获取商品列表信息
      //return this.$store.state.productList;
      await this.axios.get('show_products/')
        .then((response) => {
            console.log(response.data.list);
            this.productsList = response.data.list.filter(i => i.fields.product_business === this.$store.state.userId)
            console.log(this.productsList);
        })
        .catch(function (error) {
            console.log(error);
        });
    },

    addCommodity() {
      this.$router.push({path: '/business/commodity/add_commodity'})
    }
  },
  async created(){

    await this.getProductsList()
    console.log("this")
    console.log(JSON.stringify(this.productsList))
    console.log(this.myFilteredKeys)

  }
}
</script>