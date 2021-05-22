import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import User from '@/components/User'
import Vmain from '@/components/Vmain'
import Vnote from '@/components/Vnote'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Vmain',
      component: Vmain
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/note',
      name: 'Vnote',
      component: Vnote
    },
  ]
})
