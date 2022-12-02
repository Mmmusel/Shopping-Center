<template>
    <v-virtual-scroll
        :items="items"
        :item-height="50"
        height="500"
        bench="5"
    >
      <template v-slot:default="{ item }">
        <v-list-item>
          <v-list-item-avatar>
            <v-avatar
                :color="item.color"
                size="56"
                class="white--text"
            >
              {{ item.initials }}
            </v-avatar>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-col>
              <v-list-item-title>{{ item.fullName }}</v-list-item-title>
            </v-col>
            <v-col>
              <v-card-text>{{item.commodity_and_num}}</v-card-text>
            </v-col>
          </v-list-item-content>

          <v-list-item-action>
            <v-btn
                class="ma-2"
                :loading="loading"
                :disabled="loading"
                color="success"
                @click="loader = 'loading'"
            >
              {{btn_content}}
              <template v-slot:loader>
                <span>Loading...</span>
              </template>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </template>
    </v-virtual-scroll>

</template>

<script>
export default {
  name: 'order_content',
  data: () => ({
    colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],
    names: ['lzh', 'lyq', 'lr'],
    commoditys: ['手机', '面包', '果冻'],
    nums: [1, 2, 3],
    btn_content: '提醒付款',
    loader: null,
    loading: false,
  }),

  watch: {
    loader () {
      const l = this.loader
      this[l] = !this[l]

      setTimeout(() => (this[l] = false), 500)

      this.loader = null
    },
  },

  computed: {
    items () {
      const colorsLength = this.colors.length
      const namesLength = this.names.length
      const commoditysLength = this.commoditys.length
      const numsLength = this.nums.length

      // return Array.from({ length: 10000 }, (k, v) => {
      return Array.from({ length: 10000 }, () => {
        const name = this.names[this.genRandomIndex(namesLength + 1) - 1]
        return {
          color: this.colors[this.genRandomIndex(colorsLength + 1) - 1],
          fullName: `${name}`,
          initials: `${name[0]}`,
          commodity_and_num: this.commoditys[this.genRandomIndex(commoditysLength + 1) - 1]
              + " x " + this.nums[this.genRandomIndex(numsLength + 1) - 1],
        }
      })
    },
  },

  methods: {
    genRandomIndex (length) {
      return Math.ceil(Math.random() * (length - 1))
    },
  },
}
</script>

