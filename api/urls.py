from django.contrib import admin
from django.urls import path , include , re_path
from api.views import course,student

urlpatterns = [
    path('course/', course.CourseView.as_view()),
    path('studentlist/',student.studentStatus.as_view()),
    path('studentinfo/',student.studentInfo.as_view()),
]