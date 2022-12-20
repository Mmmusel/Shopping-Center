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
            >

              <business_Product  :info="item" :key="item.fields.id"></business_Product>

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
    <div class="container">
      {{ upload_file || "导入" }}
      <input
        type="file"
        accept=".xls,.xlsx"
        class="upload_file"
        @change="readExcel($event)"
      />
      <el-button type="success" @click="addExcelStock">导入excel库存</el-button>
    </div>
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
import business_Product from "@/components/business/business_product";
import {read, utils} from "xlsx";

export default {
  name: "business_commodity",
  components:{

    business_Product
  },
  data () {
    return {
      excelParseData:[],
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

    async addCommodity() {

              let m=[]
              await this.axios.get('fetch_userInfo',{params:{user_id: this.$store.state.userId}})
              .then((response) => {
                  console.log(response);
                  m=response


              })
              .catch(function (error) {
                  console.log(error);

              });


              if(m.data.user_mobile===""){
                console.log("null")
                window.alert("请完善联系方式")
                this.$router.push({path: '/business/information'})
                return
              }

              if((m.data.user_province==="")||(m.data.user_city==="")||(m.data.user_area==="")){
                window.alert("请完善地址")
                this.$router.push({path: '/business/information'})
                return
              }


              if(m.data.user_address===""){
                window.alert("请完善详细地址")
                this.$router.push({path: '/business/information'})
                return
              }
      this.$router.push({path: '/business/commodity/add_commodity'})
    },
    addExcelStock(){
      console.log(this.excelParseData)
      if(!this.upload_file){
        window.alert("导入文件为空")
      }else{
        this.excelParseData.forEach(async (item) =>{
          await this.axios.get('add_product_stock/',
          {params:{product_id: item.product_id,stock:item.stock_num,cost:item.stock_cost}})
        .then((response) => {
            console.log(response);

        })
        .catch(function (error) {
            console.log(error);

        })
        })
        this.upload_file=null
        this.excelParseData=[]

      window.alert("库存添加成功")
      }
    },


    readExcel(e) {
      // 读取表格文件
      this.excelParseData=[]
      this.upload_file=null
      let that = this;
      const files = e.target.files;


      if (files.length <= 0) {
        return false;
      } else if (!/\.(xls|xlsx)$/.test(files[0].name.toLowerCase())) {
        this.$message({
          message: "上传格式不正确，请上传xls或者xlsx格式",
          type: "warning"
        });
        return false;
      } else {
        // 更新获取文件名
        that.upload_file = files[0].name;
      }



      const fileReader = new FileReader();
      fileReader.onload = ev => {
        try {
          const data = ev.target.result;

          const workbook = read(data, {
            type: "binary"
          });

          const wsname = workbook.SheetNames[0]; //取第一张表
          const ws = utils.sheet_to_json(workbook.Sheets[wsname]); //生成json表格内容
          //ws就是读取的数据（不包含标题行即表头，表头会作为对象的下标）

          //this.submit_form();

					console.log(ws);
          this.excelParseData=ws
          console.log(this.excelParseData);

        } catch (e) {

          console.log(e);
          return false;
        }
      };
      console.log("rrrttt")
      fileReader.readAsBinaryString(files[0]);
    },
  },
  async created(){

    await this.getProductsList()
    console.log("this")
    console.log(JSON.stringify(this.productsList))


  }
}
</script>

