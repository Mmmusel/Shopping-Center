<template>
  <div>
    <br><br><br>
    <br>
    <v-card
        class="mx-auto"
        max-width="1000"
        raised
    >
      <v-card-title style="margin-left: 400px">本周交易额</v-card-title>
      <v-list-item three-line>
        <v-list-item-content>
          <Data_show></Data_show>
        </v-list-item-content>
      </v-list-item>
      <router-view></router-view>
    </v-card>
  </div>

</template>
<script>
import Data_show from "@/view/manager/data_show";
export default {
  components: {Data_show}
}
</script>
