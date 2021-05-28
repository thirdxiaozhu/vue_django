// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import qs from 'qs';

Vue.use(axios);
Vue.use(ElementUI,{ size: 'big', zIndex: 3000 }); //size默认组件尺寸 zindex：弹窗大小
Vue.use(Vuex);
Vue.config.productionTip = false;
//在vue全局变量中设置了$axios = axios
//以后每个组件使用的时候可以 this.$axios
Vue.prototype.$axios = axios;
Vue.prototype.$qs = qs;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed';
axios.defaults.headers.get['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.transformRequest = [function (data) {
    let src = ''
    for (let item in data) {
      src += encodeURIComponent(item) + '=' + encodeURIComponent(data[item]) + '&'
    }
    return src
}]
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  data:{
    title : '土豆',
  }
})
