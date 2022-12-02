<template>
  <v-container
      id="user-profile-view"
      fluid
      tag="section"
  >
    <v-row justify="center">
      <v-col
          cols="12"
          md="8"
      >
        <materialCard
            color="primary"
            icon="mdi-account-outline"
        >
          <template #title>
            修改个人信息
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="公司"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="用户名"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="4"
                >
                  <v-text-field
                      color="purple"
                      label="联系电话"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="6"
                >
                  <v-text-field
                      color="purple"
                      label="姓名"
                  />
                </v-col>

                <v-col
                    cols="12"
                    md="6"
                >
                  <v-text-field
                      color="purple"
                      label="邮箱"
                  />
                </v-col>

                <v-col cols="12">
                  <v-text-field
                      color="purple"
                      label="默认地址"
                  />
                </v-col>

                <v-col
                    cols="12"
                    class="text-right"
                >
                  <v-btn
                      color="primary"
                      min-width="150"
                  >
                    更新个人信息
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </materialCard>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import materialCard from "@/components/customer/MaterialCard";

export default {
  name: 'UserProfileView',
  components:{
    materialCard
  }
}
</script>
