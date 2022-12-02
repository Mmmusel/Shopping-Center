<template>
  <v-row justify="center" class="my-3">
    <template v-for="(item, itemIndex) in indicators">
      <v-col :key="itemIndex" cols="12" md="3">
        <v-hover v-slot="{ hover }">
          <v-card
              class="item-card"
              :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }"
          >
            <v-row class="mx-3 ">

              <v-col md="6" class="align-center">
                <v-icon :color="item.color" size="100">{{
                    item.icon
                  }}
                </v-icon>
              </v-col>

              <v-col md="6" class="align-center justify-center flex-column ">
                <div class="text-h5 text-center">{{ item.name }}</div>
                <div class="text-h7 text-center">{{ item.price }}</div>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
      </v-col>
    </template>
  </v-row>

  <!--
  <v-card
      :loading="loading"
      class="mx-auto my-12"
      max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
      ></v-progress-linear>
    </template>

    <v-img
        height="250"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <v-card-title>Cafe Badilico</v-card-title>

    <v-card-text>
      <v-row
          align="center"
          class="mx-0"
      >
        <v-rating
            :value="4.5"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
        ></v-rating>

        <div class="grey--text ms-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 text-subtitle-1">
        $ • Italian, Cafe
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-title>Tonight's availability</v-card-title>

    <v-card-text>
      <v-chip-group
          v-model="selection"
          active-class="deep-purple accent-4 white--text"
          column
      >
        <v-chip>5:30PM</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
          color="deep-purple lighten-2"
          text
          @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions>
  </v-card>
  -->
</template>

<script>
export default {
  name: "business_commodity",
  components: {},
  data: () => ({
    loading: false,
    selection: 1,
    indicators: [
      {
        icon: "mdi-cart-arrow-up",
        color: "cyan",
        name: "总销售额",
        price: "1100.00（元）",
      },
      {
        icon: "mdi-cash-refund",
        color: "red",
        title: "支出",
        text: "568.20（元）",
      },
      {
        icon: "mdi-currency-cny",
        color: "amber",
        title: "利润",
        text: "-368.20（元）",
      },
      {icon: "mdi-dolly", color: "blue", title: "商品", text: "4(件)"},
      {
        icon: "mdi-cart-arrow-up",
        color: "cyan",
        title: "总销售额",
        text: "1100.00（元）",
      },
      {
        icon: "mdi-cash-refund",
        color: "red",
        title: "支出",
        text: "568.20（元）",
      },
      {
        icon: "mdi-currency-cny",
        color: "amber",
        title: "利润",
        text: "-368.20（元）",
      },
    ],
  }),

  methods: {
    reserve () {
      this.loading = true

      setTimeout(() => (this.loading = false), 2000)
    },
  },
}
</script>

<style scoped>

</style>