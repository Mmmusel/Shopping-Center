const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
    publicPath: './' ,
    outputDir: 'dist',
    assetsDir:'static'
})
