<template>
  <div>
    <div>
      <v-container fluid>
        <v-data-iterator
            :items="items"
            :items-per-page.sync="itemsPerPage"
            :page="page"
            :search="search"
            :sort-by="sortBy.toLowerCase()"
            :sort-desc="sortDesc"
            hide-default-footer
        >
          <template v-slot:header>
            <div class="title">
              <h3>我的订单</h3>
            </div>
            <v-toolbar
                dark
                color="blue darken-3"
                class="mb-1"
            >
              <v-text-field
                  clearable
                  flat
                  solo-inverted
                  hide-details
                  label="Search"
              ></v-text-field>
              <template v-if="$vuetify.breakpoint.mdAndUp">
                <v-spacer></v-spacer>
                <v-select
                    v-model="sortBy"
                    flat
                    solo-inverted
                    hide-details
                    :items="keys"
                    label="Sort by"
                ></v-select>
                <v-spacer></v-spacer>
                <v-btn-toggle
                    v-model="sortDesc"
                    mandatory
                >
                  <v-btn
                      large
                      depressed
                      color="blue"
                      :value="false"
                  >
                    <v-icon>mdi-arrow-up</v-icon>
                  </v-btn>
                  <v-btn
                      large
                      depressed
                      color="blue"
                      :value="true"
                  >
                    <v-icon>mdi-arrow-down</v-icon>
                  </v-btn>
                </v-btn-toggle>
              </template>
            </v-toolbar>
          </template>

          <template v-slot:default="props">
            <v-row>
              <v-col
                  v-for="item in props.items"
                  :key="item.name"
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
              >
                <v-card>
                  <v-card-title class="subheading font-weight-bold">{{ item.name }}</v-card-title>

                  <v-divider></v-divider>

                  <v-list dense>
                    <v-list-item
                        v-for="(key, index) in filteredKeys"
                        :key="index"
                    >
                      <v-list-item-content :class="{ 'blue--text': sortBy === key }">{{ key }}:</v-list-item-content>
                      <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === key }">{{ item[key.toLowerCase()] }}</v-list-item-content>
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
    </div>
    <div>
      <v-container fluid>
        <v-data-iterator
            :items="items"
            :items-per-page.sync="itemsPerPage"
            :page="page"
            :search="search"
            :sort-by="sortBy.toLowerCase()"
            :sort-desc="sortDesc"
            hide-default-footer
        >
          <template v-slot:header>
            <div class="title">
              <h3>历史订单</h3>
            </div>
            <v-toolbar
                dark
                color="blue darken-3"
                class="mb-1"
            >
              <v-text-field
                  clearable
                  flat
                  solo-inverted
                  hide-details
                  label="Search"
              ></v-text-field>
              <template v-if="$vuetify.breakpoint.mdAndUp">
                <v-spacer></v-spacer>
                <v-select
                    v-model="sortBy"
                    flat
                    solo-inverted
                    hide-details
                    :items="keys"
                    label="Sort by"
                ></v-select>
                <v-spacer></v-spacer>
                <v-btn-toggle
                    v-model="sortDesc"
                    mandatory
                >
                  <v-btn
                      large
                      depressed
                      color="blue"
                      :value="false"
                  >
                    <v-icon>mdi-arrow-up</v-icon>
                  </v-btn>
                  <v-btn
                      large
                      depressed
                      color="blue"
                      :value="true"
                  >
                    <v-icon>mdi-arrow-down</v-icon>
                  </v-btn>
                </v-btn-toggle>
              </template>
            </v-toolbar>
          </template>

          <template v-slot:default="props">
            <v-row>
              <v-col
                  v-for="item in props.items"
                  :key="item.name"
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
              >
                <v-card>
                  <v-card-title class="subheading font-weight-bold">{{ item.name }}</v-card-title>

                  <v-divider></v-divider>

                  <v-list dense>
                    <v-list-item
                        v-for="(key, index) in filteredKeys"
                        :key="index"
                    >
                      <v-list-item-content :class="{ 'blue--text': sortBy === key }">{{ key }}:</v-list-item-content>
                      <v-list-item-content class="align-end" :class="{ 'blue--text': sortBy === key }">{{ item[key.toLowerCase()] }}</v-list-item-content>
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
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      itemsPerPageArray: [4, 8, 12],
      search: '',
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 4,
      sortBy: '商店名',
      keys: [
        '商店名',
        '订单编号',
        '下单时间',
        '邮政编码',
        '用户名',
        '金额',
        '状态',
      ],
      items:[
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },
        {
          商店名:"华为",
          订单编号: 1,
          下单时间: 2022-10-10,
          邮政编码: 111111,
          用户名:"小红",
          金额:100,
          状态:"已完成",
        },

        {
          商店名:"小米",
          订单编号: 2,
          下单时间: 2022-11-10,
          邮政编码: 111112,
        }
      ],
    }
  },
  computed: {
    numberOfPages () {
      return Math.ceil(this.items.length / this.itemsPerPage)
    },
    filteredKeys () {
      return this.keys.filter(key => key !== `Name`)
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
  },
}
</script>