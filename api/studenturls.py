from django.contrib import admin
from django.urls import path , include , re_path
from api.views.student import views

urlpatterns = [
    path('initstudentinfo/', views.initStudentInfo.as_view()),
]