from django.contrib import admin
from django.urls import path , include , re_path
from api.views.admin import course,student,room,teacher
from api.views import general
from api import teacherurls

urlpatterns = [
    path('course/', course.CourseView.as_view()),
    path('login/',general.login.as_view()),
    path('studentlist/',student.studentStatus.as_view()),
    path('studentinfo/',student.studentInfo.as_view()),
    path('editstuoptions/',student.editstuoptions.as_view()),
    path('getlocation/',student.getlocation.as_view()),
    path('getclass/',student.getclass.as_view()),
    path('editstudent/',student.editstudent.as_view()),
    path('getOrganize/',student.getOrganize.as_view()),
    path('addstudent/',student.addStudent.as_view()),
    path('deletestudent/',student.deleteStudent.as_view()),
    path('roomlist/',room.roomList.as_view()),
    path('getfunctions/',room.getFunctions.as_view()),
    path('getroominfo/',room.getRoomInfo.as_view()),
    path('filterroom/',room.filterRoom.as_view()),
    path('getteacher/',teacher.getTeacherlist.as_view()),
    path('getteacherinfo/',teacher.getTeacherinfo.as_view()),
    path('editteaoptions/',teacher.editTeacherOptions.as_view()),
    path('editteacher/',teacher.editTeacher.as_view()),
    path('addteacher/',teacher.addTeacher.as_view()),
    path('collegechange/',teacher.collegeChange.as_view()),
    path('teacher/',include(teacherurls)),
]