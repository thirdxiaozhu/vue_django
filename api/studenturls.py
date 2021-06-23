from django.contrib import admin
from django.urls import path , include , re_path
from api.views.student import views

urlpatterns = [
    path('initstudentinfo/', views.initStudentInfo.as_view()),
    path('getcourselist/',views.getCourseList.as_view()),
    path('initcourselist/',views.initCourseList.as_view()),
    path('getrelations/',views.getRelations.as_view()),
    path('updatechoice/',views.updateChoice.as_view()),
    path('getscheduled/',views.getScheduled.as_view()),
    path('deletescheduled/',views.deleteScheduled.as_view()),
    path('getcollegelist/',views.getCollegelist.as_view()),
    path('initcourseinfo/',views.initCourseInfo.as_view()),
    path('getcourses/',views.getCourses.as_view()),
    path('filtercourses/',views.filterCourses.as_view()),
]