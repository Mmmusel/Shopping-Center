"use strict";(self["webpackChunkmy_project"]=self["webpackChunkmy_project"]||[]).push([[18],{18:function(t,s,o){o.r(s),o.d(s,{default:function(){return l}});var d=function(){var t=this,s=t._self._c;return t.product?s("div",[s("div",{staticClass:"product"},[s("div",{staticClass:"product-image"},[s("img",{attrs:{src:`http://127.0.0.1:8000/media/${t.product.fields.product_image}`,alt:""}})]),s("div",{staticClass:"product-info"},[s("h1",{staticClass:"product-name"},[t._v(t._s(t.product.fields.product_name))]),s("div",{staticClass:"product-cost"},[t._v(t._s(t.product.fields.product_cost))]),s("div",{staticClass:"product-add-cart",on:{click:t.handleAddCart}},[t._v("加入购物车")])])]),s("div",{staticClass:"product-desc"},[s("h2",[t._v("产品介绍")]),s("img",{attrs:{src:`http://127.0.0.1:8000/media/${t.product.fields.product_imageDetail}`,alt:""}})])]):t._e()},c=[],i={data(){return{id:parseInt(this.$route.params.id),product:null}},methods:{async getProduct(t){await this.axios.get("fetch_product/",{params:{product_id:t}}).then((t=>{console.log(t),this.product=t.data.product})).catch((function(t){console.log(t)}))},handleAddCart(){this.$store.commit("addCart",this.id)}},async created(){console.log("detailview"),console.log(this.id),await this.getProduct(this.id),console.log("detailviewend"),console.log(this.product)},async mounted(){console.log("11detailview"),console.log(this.id),await this.getProduct(this.id),console.log("11detailviewend"),console.log(this.product)}},a=i,e=o(1001),r=(0,e.Z)(a,d,c,!1,null,"8c219878",null),l=r.exports}}]);
//# sourceMappingURL=18.ff639f4c.js.map