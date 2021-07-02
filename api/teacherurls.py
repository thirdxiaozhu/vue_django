from django.contrib import admin
from django.urls import path , include , re_path
from api.views.teacher import views

urlpatterns = [
    path('initteacherinfo/', views.initTeacherInfo.as_view()),
    path('getscheduled/',views.getScheduled.as_view()),
    path('getscheduled4test/',views.getScheduled4test.as_view()),
    path('initstudentlist/',views.initStudentList.as_view()),
    path('ifarrange/',views.ifarrange.as_view()),
    path('updategrade/',views.updateGrade.as_view()),
    path('getsendlist/',views.getSendlist.as_view()),
    path('getsavelist/',views.getSavelist.as_view()),
    path('replymessage/',views.replyMessage.as_view()),
    path('rejectmessage/',views.rejectMessage.as_view()),
    path('postmessage/',views.postMessage.as_view()),
]