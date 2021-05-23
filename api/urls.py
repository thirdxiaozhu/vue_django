from django.contrib import admin
from django.urls import path , include , re_path
from api.views import course

urlpatterns = [
    path('course/', course.CourseView.as_view()),
]