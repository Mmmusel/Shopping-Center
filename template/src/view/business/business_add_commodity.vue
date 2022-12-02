<template>
  <div class="py-2 px-2 height-100pc user-center" elevation="1">
    <v-row no-gutters justify="space-between">
      <v-col class="ml-3">
        <v-toolbar
            dark
            color="blue darken-3"
            class="mb-1"
        >
          <v-spacer></v-spacer>
          <v-toolbar-title>
            <h4>添加商品</h4>
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-card>
          <v-card flat class="pa-3">
            <v-row>
              <v-col md="6">
                <v-form ref="form">
                  <!-- 字段渲染 -->
                  <v-container>
                    <v-row>
                      <v-col md="12">
                        <v-text-field
                            label="商品名"
                            clearable
                        />
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col md="12">
                        <v-text-field
                            label="商品颜色"
                            clearable
                        />
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col md="12">
                        <v-text-field
                            label="商品进价"
                            clearable
                        />
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col md="12">
                        <v-text-field
                            label="商品售价"
                            clearable
                        />
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col md="12">
                        <v-text-field
                            label="商品库存"
                            clearable
                        />
                      </v-col>
                    </v-row>
                  </v-container>
                </v-form>
              </v-col>
              <v-col md="6">
                <el-form ref="form" :model="productForm" label-width="80px">
                  <el-form-item label="主页图片">
                    <input type="file" @change="getImageFile" id="img">
                    <img :src="productForm.product_image"/>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit">确认添加</el-button>
                  </el-form-item>
                </el-form>
                <el-form ref="form" :model="productForm" label-width="80px">
                  <el-form-item label="细节图片">
                    <input type="file" @change="getImageFile" id="img">
                    <img :src="productForm.product_image"/>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit">确认添加</el-button>
                  </el-form-item>
                </el-form>
              </v-col>
            </v-row>
            <v-divider/>
            <v-row justify="end">
              <v-col md="4" align="end">
                <v-btn
                    small
                    tile
                    class="mr-2"
                    color="primary"
                    @click="saveProfile"
                >
                  添加
                </v-btn>
              </v-col>
            </v-row>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "business_add_commodity",
  data() {
    return {
      productForm: {
        product_name: "", // 商品名
        product_color: "", // 商品颜色
        // TODO：商品进价/商品售价
        product_stock: "", // 商品库存
        product_image: "", // 主页图片
        // TODO：细节图片
      },

    };
  },

  methods: {
    // TODO：保存商品信息
    saveProduct() {

    },
    getImageFile:function(e) {
      this.productForm.product_image = e.target.files[0];
    },
    async onSubmit(){
      console.log("good");
    },
  },
};
</script>

<style>

</style>
