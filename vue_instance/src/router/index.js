import Vue from 'vue'
import Router from 'vue-router'
import User from '@/components/User'
import Vmain from '@/components/Vmain'
import Vnote from '@/components/Vnote'
import Vstudentlist from '@/components/Vstudentlist'
import Vteacherlist from '@/components/Vteacherlist'
import Vcourse from '@/components/Vcourse'
import Vtest from '@/components/Vtest'
import admin_index from '@/views/admin_index'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/admin',
      name: 'admin_index',
      component: admin_index,
      children: [
        {
          path: '/',
          name: 'Vmain',
          component: Vmain
        },
        {
          path: 'user',
          name: 'User',
          component: User
        },
        {
          path: 'note',
          name: 'Vnote',
          component: Vnote
        },
        {
          path: 'studentlist',
          name: 'Vstudentlist',
          component: Vstudentlist
        },
        {
          path: 'teacherlist',
          name: 'Vteacherlist',
          component: Vteacherlist
        },
        {
          path: 'course',
          name: 'Vcourse',
          component: Vcourse
        },
        {
          path: 'test',
          name: 'Vtest',
          component: Vtest
        },
      ]
    },
  ]
})
