from django.contrib import admin
from django.urls import path , include , re_path
from api.views import course,student,general

urlpatterns = [
    path('course/', course.CourseView.as_view()),
    path('login/',general.login.as_view()),
    path('studentlist/',student.studentStatus.as_view()),
    path('studentinfo/',student.studentInfo.as_view()),
    path('editstuoptions/',student.editstuoptions.as_view()),
    path('getlocation/',student.getlocation.as_view()),
    path('getclass/',student.getclass.as_view()),
    path('editstudent/',student.editstudent.as_view()),
]