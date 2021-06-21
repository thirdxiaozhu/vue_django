from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models, page
from api import serializers4stu as ser
import json


class initStudentInfo(APIView):
    def get(self , request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        student = models.StudentInfo.objects.filter(stu_id = stu_id).first()

        studentinfo = ser.StudentInfoSerializers(student, many=False)
        print(studentinfo.data)
        ret={
            'code': 1000,
            'form': studentinfo.data
        }
        return Response(ret)


class getCourseList(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        major = models.StudentInfo.objects.filter(stu_id = stu_id).first().Major.id
        courses = models.MajorInfo.objects.filter(id=major).first().course.all()

        courseinfo = ser.CourseinfoSerializers(courses, many=True)
        print(courseinfo.data)

        ret = {
            'code': 1000,
            'courselist': courseinfo.data
        }

        return Response(ret)