from django.contrib import admin
from django.urls import path , include , re_path
from api.views.teacher import views

urlpatterns = [
    path('initteacherinfo/', views.initTeacherInfo.as_view()),
]