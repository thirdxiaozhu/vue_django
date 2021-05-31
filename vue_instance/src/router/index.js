import Vue from 'vue'
import Router from 'vue-router'
import Vmain from '@/components/adminviews/Vmain'
import Vstudentlist from '@/components/adminviews/Vstudentlist'
import Vteacherlist from '@/components/adminviews/Vteacherlist'
import Vcourse from '@/components/adminviews/Vcourse'
import Vtest from '@/components/adminviews/Vtest'
import admin_index from '@/views/admin_index'
import login from '@/views/login'
import student_index from '@/views/student_index'
import Vmain4stu from '@/components/studentviews/Vmain'


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
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/student',
      name: 'student',
      component: student_index,
      children: [
         {
          path: '/',
          name: 'Vmain',
          component: Vmain4stu
        },
      ]
    }
  ]
})
