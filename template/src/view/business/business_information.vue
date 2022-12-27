<template>
  <div class="py-2 px-2 height-100pc user-center" elevation="1">
    <v-row no-gutters justify="space-between">
      <v-col class="mr-3" md="3">
        <v-card shaped>
          <v-img
              :style="{ 'background-image': usercard }"
              height="250"
              class="user-card-img"
          >
            <div class="text-center mt-2">
              <img
                  class="avatar-img"
                  v-if="userInfo.user_avatar"
                  :src="userInfo.user_avatar"
                  alt=""/>
              <v-icon v-else size="190" color="#fff">mdi-account-circle</v-icon>
            </div>
            <div class="my-2 text-center font-weight-bold">
              {{ userInfo.user_name }}
            </div>
          </v-img>

          <v-card-text>
            <div v-for="(line, index) in cardlines" :key="index">
              <div class="py-2">
                <v-icon small left>{{ line.icon }}
                </v-icon
                >
                {{ line.text }}
              </div>
              <v-divider/>
            </div>


            <div class="py-2">
                <v-icon small left> mdi-email
                </v-icon
                >
                <region-text
                  separator="-"
                  :town="false"
                  v-model="userInfo.user_selectAddress"
                />

              </div>
              <v-divider/>



            <div class="mb-3"></div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col class="ml-3">
        <v-card>
          <v-tabs>
            <v-tab>个人设置</v-tab>
            <v-tab>修改密码</v-tab>

            <!-- 个人设置 -->
            <v-tab-item>
              <v-card flat class="pa-3">
                <v-row>
                  <v-col md="6">
                    <v-form ref="form">
                      <!-- 字段渲染 -->
                      <v-container>
                        <v-row>
                          <v-col md="12">
                            <v-text-field
                                label="用户名"
                                :rules="profileRules.user_name"
                                v-model="profileForm.user_name"
                                clearable
                            />
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col md="12">
                            <v-text-field
                                label="手机号码"
                                :rules="profileRules.user_mobile"
                                v-model="profileForm.user_mobile"
                                clearable
                            />
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-card>
                            <v-col>
                              详细地址
                              <region-selects


                                v-model="region"
                                :town="false"


                                @change="selectLogs"
                                clearable
                              />
                            </v-col>
                            <v-col>
                              <v-text-field
                                label="详细地址"
                                :rules="profileRules.user_email"
                                v-model="profileForm.user_address"
                                clearable
                              />
                            </v-col>
                          </v-card>
                        </v-row>
                      </v-container>
                    </v-form>
                  </v-col>
                  <v-col md="6">
                    <!-- <avatar-upload
                        tips-text="拖拽或单击进行上传图片"
                        v-model="profileForm.user_avatar"
                    />-->

                    <el-form ref="form" :model="profileForm" label-width="80px">
                      <el-form-item label="头像">
                        <input type="file" @change="getImageFile" id="img">

                        <img :src="showImage"  height="150px" width="150px">
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
                        outlined
                        tile
                        class="mr-2"
                        color="secondary"
                        @click="resetProfile"
                    >
                      重置
                    </v-btn>
                    <v-btn
                        small
                        tile
                        class="mr-2"
                        color="primary"
                        @click="saveProfile"
                    >
                      保存
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card>
            </v-tab-item>

            <!-- 修改密码 -->
            <v-tab-item>
              <v-card flat class="pa-3">
                <v-row justify="center" align="center">
                  <v-col md="6">
                    <v-form ref="passwordForm">
                      <!-- 字段渲染 -->
                      <v-container>
                        <v-row>
                          <v-col md="12">
                            <v-text-field
                                label="旧密码"
                                :rules="passwordRules.oldPassword"
                                v-model="passwordForm.oldPassword"
                                type="password"
                                clearable
                            />
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col md="12">
                            <v-text-field
                                label="新密码"
                                :rules="passwordRules.newPassword"
                                v-model="passwordForm.newPassword"
                                id="newPassword"
                                type="password"
                                clearable
                            />
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col md="12">
                            <v-text-field
                                label="确认密码"
                                :rules="passwordRules.confirmPassword"
                                v-model="passwordForm.confirmPassword"
                                id="confirmPassword"
                                type="password"
                                clearable
                            />
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-form>
                  </v-col>
                </v-row>
                <v-row justify="end">
                  <v-col md="4" align="end">
                    <v-btn
                        small
                        tile
                        class="mr-2"
                        color="primary"
                        @click="passwordUpate"
                    >
                      保存
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import GeoPattern from "geopattern";

import {
  //getAccessLogsByUserId,
  //saveUserProfile,

} from "@/api/user";

//import AvatarUpload from "@/components/business/AvatarUpload";
import {required} from "@/utils/widget";
import { RegionSelects } from 'v-region'
import { RegionText } from 'v-region'


export default {
  name: "business_information",
  components: {
    RegionSelects,
    RegionText
  },
  data() {
    return {
      //alert: false,
      res:true,
      showImage:"",
      region:{
        province: '350000',
        city: '350100',
        area: '350104',
        town:''
      },
      cardlines: [

      ],
      tabItems: [
        {tab: "profile", content: "个人设置"},
        {tab: "password", content: "修改密码"},
      ],
      usercard: "",
      userInfo: {
        user_name: "",
        user_mobile: "",
        user_selectAddress:{
          province: '',
          city: '',
          area: '',
          town: ''
      },
        user_address: "",
        user_avatar: "",
        user_createtime: ""
      },

      //accessLogs: [],
      profileForm: {
        //userId: "",
        user_name: "",
        user_mobile: "",
        user_address: "",
        user_avatar: "",
      },
      profileRules: {
        user_name: [required("用户名")],
        user_mobile: [
          required("手机号码"),
          function (v) {
            return /^1[3456789]\d{9}$/.test(v) || `手机号码格式错误`;
          },
        ],
        user_email: [required("地址")],

      },
      passwordForm: {
        oldPassword: "",
        newPassword: "",
        confirmPassword: "",
      },
      passwordRules: {
        oldPassword: [required("密码")],
        newPassword: [required("密码")],
        confirmPassword: [required("密码")],
      },
      addrSelectRules:""


    };
  },

  //mounted() {
  async created() {
    await this.initBaseInfo();
    //this.initAccessLogs();
    this.initPasswordRules();
    console.log(this.region)
  },
  methods: {

    async fetchUserInfo(){
      await this.axios.get('fetch_userInfo/',{params:{user_id: this.$store.state.userId}})
        .then((response) => {
            console.log(response);
            var ttt=response.data.user_avatar.fields.user_avatar
            this.userInfo = {
              user_name: response.data.user_name,
              user_mobile: response.data.user_mobile,
              user_address: response.data.user_address,
              user_avatar: (ttt!=="")?'http://127.0.0.1:8000/media/'+ttt:'',
              user_createtime: response.data.user_createtime,
              user_selectAddress:{
          province: response.data.user_province,
          city:response.data.user_city,
          area: response.data.user_area,
          town: ''
      },
            }
            this.showImage = (ttt!=="")?'http://127.0.0.1:8000/media/'+ttt:''
        })
        .catch(function (error) {
            console.log(error);
        });
    },
    resetProfile() {
       this.region=this.userInfo.user_selectAddress,
      this.profileForm = {
        user_name: this.userInfo.user_name,
        user_mobile: this.userInfo.user_mobile,
        user_address: this.userInfo.user_address,
        user_avatar:   this.userInfo.user_avatar,


      };
    },
    async initBaseInfo() {
      await this.fetchUserInfo()
      this.usercard = GeoPattern.generate(this.userInfo.user_name, {}).toDataUrl();
      this.resetProfile();

      this.cardlines = [
        {
          icon:"mdi-account",
          text:this.userInfo.user_name,
        },

        {
          icon: "mdi-cellphone",
          text: this.userInfo.user_mobile,
        },

        {
          icon: "mdi-update",
          text: `加入于 ${this.userInfo.user_createtime}`
        },

        {
          icon: "mdi-email",
          text: this.userInfo.user_address,
        }
        /*{
          icon: "mdi-account-multiple",
          text: this.userInfo.organizations
              ? this.userInfo.organizations.map((item) => item.organName)
              : "无",
        },
        {
          icon: "mdi-account-tie-outline",
          text: this.userInfo.admin
              ? "超级管理员"
              : this.userInfo.roles
                  ? this.userInfo.roles.map((item) => item.roleName)
                  : "无",
        },*/

      ];
    },
    /*initAccessLogs() {
      getAccessLogsByUserId(this.userInfo.userId)
          .then((result) => {
            this.accessLogs = result.records;
          })
          .catch((err) => {
            console.warn(err);
          });
    },*/
    /*async onSubmit(){
      console.log("good");
      let formData = new FormData();
      formData.append('goods_image', this.form.goods_image);

      var configs = {
        headers:{'Content-Type':'multipart/form-data'}
      }
      await this.axios.post('add_product/',formData, configs).then(response => {
        if(response.data.msg==="success"){
          this.image = 'http://127.0.0.1:8000/media/'+response.data.image
        }
      })
    },*/
    selectLogs:async function (e){
      console.log(e)
      console.log(this.region.city)

      await this.checkSelectAddr()
    },

    getImageFile:function(e) {
       this.profileForm.user_avatar = e.target.files[0];
      let img = new FileReader();
      img.readAsDataURL(this.profileForm.user_avatar);
      console.log("img:",img)
      img.onload = ({ target }) => {
        this.showImage = target.result; //将img转化为二进制数据
        console.log("target:",target)
      };
    },
    async onSubmit(){
      console.log("good");
      /*let formData = new FormData();
      formData.append('goods_image', this.form.goods_image);

      var configs = {
        headers:{'Content-Type':'multipart/form-data'}
      }
      await this.axios.post('add_product/',formData, configs).then(response => {
        if(response.data.msg==="success"){
          this.image = 'http://127.0.0.1:8000/media/'+response.data.image
          console.log(response)
        }
      })*/
    },

    async saveProfile() {
      if (this.$refs.form.validate()) {
        let formData = new FormData();
        formData.append('user_image', this.profileForm.user_avatar);
        //formData.append('user_id',this.$store.state.userId)
        //formData.append('forms',JSON.stringify(this.profileForm))

        if(this.profileForm.user_name==''){
          window.alert('请完善用户名')
          return
        }else if(this.profileForm.user_mobile==''){
          window.alert('请完善手机号码')
          return
        }else if(this.profileForm.user_address==''){
          window.alert('请完善详细地址')
          return
        }else if(!this.region.area){
          window.alert('请完善地址')
          return
        }else if(!this.region.province){
          window.alert('请完善地址')
          return
        }else if(!this.region.city){
          window.alert('请完善地址')
          return
        }else if(this.region.area===''){
          window.alert('请完善地址')
          return
        }else if(this.region.province===''){
          window.alert('请完善地址')
          return
        }else if(this.region.city===''){
          window.alert('请完善地址')
          return
        }




        const json = JSON.stringify(this.profileForm);
        const blob = new Blob([json], {
          type: 'application/json'
        });

        formData.append('forms',blob)

        const json2 = JSON.stringify((this.$store.state.userId));
        const blob2 = new Blob([json2], {
          type: 'application/json'
        });

        formData.append('user_id',blob2)
        console.log("blob2")
        console.log(blob2)
        console.log(JSON.stringify((this.$store.state.user_id)))



        const json3 = JSON.stringify(this.region);
        const blob3 = new Blob([json3], {
          type: 'application/json'
        });

        formData.append('selectAddr',blob3)



        var configs = {
          headers:{'Content-Type':'multipart/form-data'}
        }

        await this.axios.post('edit_userInfo/',formData, configs).then(response => {
          console.log(formData.get('forms'))
        if(response.data.msg==="success"){
          this.userInfo.user_avatar = 'http://127.0.0.1:8000/media/'+response.data.image
          this.showImage = 'http://127.0.0.1:8000/media/'+response.data.image
          console.log(response)

          }
        console.log(response)
        })
        .catch(function (error) {
            console.log(error);
        });
        await this.initBaseInfo()


        /*await this.axios.get('edit_userInfo/',
            {params:{user_id: this.$store.state.userId,
                    forms: JSON.stringify(this.profileForm)}})
          .then((response) => {
            console.log(response)
            this.initBaseInfo()
            this.$toast.success("保存成功", {
              position: "top-center",
            });
          })
          .catch((response) => {
            console.log(response)

          });*/
      }
    },

    // Responding to data changes
    // 地址选择器
    regionChange (data) {
      console.log(data)
    },

    async passwordUpate() {
      if (this.passwordForm.newPassword!==this.passwordForm.confirmPassword) {
       window.alert('请保持密码一致')
      }
      if (this.passwordForm.newPassword=="") {
       window.alert('密码不能为空')
      }

      await this.axios.get('edit_password/',
                {params:{old_password: this.passwordForm.oldPassword,
                    new_password:this.passwordForm.newPassword
                  ,user_id:this.$store.state.userId}})
              .catch(function (error) {
                  console.log(error);
                  this.res=false
                window.alert('请重新确认原密码')
              })
              .then((response) => {
                if(response.data.error_num!==0){
                  this.res=false
                  console.log(response.data.msg);
                  window.alert('请重新确认原密码')
                  return
                }
                window.alert('密码修改成功')

                this.res=true
              })
              ;

    },

    checkaddr() {
      /*const _this = this;
      const getField = function () {
        console.log(_this.region)
        console.log(_this.region.city)
        return _this.region.city;
      };
      console.log(getField())
      if(!getField()) return "错"
      console.log("tttttt")
      return true*/
      console.log("tttttt")
      console.log(this.region.area)
      if(!this.region.area) return "下拉选择省市区"
console.log("fffffftt")
      return true
    },

    checkNewPassword(passwordFormfield) {
      const _this = this;
      const getField = function () {
        return _this.passwordForm[passwordFormfield];
      };

      return function (v) {
        const field = getField();
        const checkResult = !field || v === field;

        if (_this.$refs.passwordForm) {
          const targetInput = _this.$refs.passwordForm.inputs.filter(
              (input) => input.id === passwordFormfield
          )[0];

          if (v === field && !targetInput.valid) {
            targetInput.resetValidation();
          }
        }

        return checkResult || `两次输入的密码不一致`;
      };
    },

    async checkSelectAddr(){
      this.profileRules = {
        user_name: [required("用户名")],
        user_mobile: [
          required("手机号码"),
          function (v) {
            return /^1[3456789]\d{9}$/.test(v) || `手机号码格式错误`;
          },
        ],
        user_email: [required("地址"),
        this.checkaddr(),

        ]

      }
    },

    initPasswordRules() {

      this.profileRules = {
        user_name: [required("用户名")],
        user_mobile: [
          required("手机号码"),
          function (v) {
            return /^1[3456789]\d{9}$/.test(v) || `手机号码格式错误`;
          },
        ],
        user_email: [required("地址"),
        this.checkaddr(),

        ],

      },

      this.passwordRules.newPassword = [
        required("新密码"),
        this.checkNewPassword("confirmPassword"),
      ];
      this.passwordRules.confirmPassword = [
        required("确认密码"),
        this.checkNewPassword("newPassword"),
      ];
    },

  },
};
</script>

<style>
.user-card-img {
  opacity: 0.8 !important;
  background-size: 100%;
}

.avatar-img {
  width: 170px;
  border-radius: 50%;
}
</style>
