import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login'

import admin_index from '@/views/admin_index'
import Vmain from '@/components/adminviews/Vmain'
import Vstudentlist from '@/components/adminviews/Vstudentlist'
import Vteacherlist from '@/components/adminviews/Vteacherlist'
import Vcourselist from '@/components/adminviews/Vcourselist'
import Vtest from '@/components/adminviews/Vtest'
import Vroom from '@/components/adminviews/Vroom'
import Vcollege from '@/components/adminviews/Vcollege'
import Vschedulemain from '@/components/adminviews/Vschedulemain'

import student_index from '@/views/student_index'
import Vmain4stu from '@/components/studentviews/Vmain'
import Vstudentinfo from '@/components/studentviews/Vstudentinfo'
import Vselectcourse from '@/components/studentviews/Vselectcourse'
import Vstudentplan from '@/components/studentviews/Vstudentplan'

import teacher_index from '@/views/teacher_index'
import Vmain4tea from '@/components/teacherviews/Vmain'
import Vteacherinfo from '@/components/teacherviews/Vteacherinfo'
import Vteachercourse from '@/components/teacherviews/Vteachercourse'


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
          name: 'Vcourselist',
          component: Vcourselist
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
        {
          path: 'collegelist',
          name: 'Vcollege',
          component: Vcollege
        },
        {
          path: 'schedule',
          name: 'Vschedulemain',
          component: Vschedulemain
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
        {
          path: 'info',
          name: 'Vstudentinfo',
          component: Vstudentinfo
        },
        {
          path: 'plan',
          name: 'Vstudentplan',
          component: Vstudentplan
        },
        {
          path: 'selectcourse',
          name: 'Vselectcourse',
          component: Vselectcourse
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
        {
          path: 'course',
          name: 'Vteachercourse',
          component: Vteachercourse
        },
      ]
    }
  ]
})
