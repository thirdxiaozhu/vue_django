import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login'

import admin_index from '@/views/admin_index'
import Vmain from '@/components/adminviews/Vmain'
import Vstudentlist from '@/components/adminviews/Vstudentlist'
import Vteacherlist from '@/components/adminviews/Vteacherlist'
import Vcourse from '@/components/adminviews/Vcourse'
import Vtest from '@/components/adminviews/Vtest'
import Vroom from '@/components/adminviews/Vroom'

import student_index from '@/views/student_index'
import Vmain4stu from '@/components/studentviews/Vmain'

import teacher_index from '@/views/teacher_index'
import Vmain4tea from '@/components/teacherviews/Vmain'
import Vteacherinfo from '@/components/teacherviews/Vteacherinfo'



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
        {
          path: 'roomlist',
          name: 'Vroom',
          component: Vroom
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
    },
    {
      path: '/teacher',
      name: 'teacher',
      component: teacher_index,
      children: [
        {
          path: '/',
          name: 'Vmain',
          component: Vmain4tea
        },
        {
          path: 'info',
          name: 'Vteacherinfo',
          component: Vteacherinfo
        },
      ]
    }
  ]
})
