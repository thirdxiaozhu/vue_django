from rest_framework import renderers
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from django.db.models import Q
from rest_framework import serializers
from api import models, page
from api import serializers as ser
import json

class getColleges(APIView):
    def get(self, rqeuest, *args, **kwargs):
        colleges = models.CollegeInfo.objects.all().order_by('college_id')

        collegelist = ser.CollegelistSerializers(colleges, many=True)
        ret = {
            'code': 1000,
            'colleges': collegelist.data,
        }

        return Response(ret)


class getMajors(APIView):
    def get(self, request, *args, **kwargs):
        college_id = request.GET.get('college_id')
        majors = models.MajorInfo.objects.filter(college_id = college_id).order_by('id')

        majorlist = ser.MajorlistSerializers(majors, many=True)
        ret = {
            'code': 1000,
            'majors': majorlist.data,
        }

        return Response(ret)


class getClasses(APIView):
    def get(self, request, *args, **kwargs):
        major_id = request.GET.get('major_id')
        print(major_id)
        classes = models.ClassInfo.objects.filter(major_id = major_id).order_by('class_id')

        classlist = ser.ClasslistSerializers(classes, many=True)
        ret = {
            'code': 1000,
            'classes': classlist.data,
        }

        return Response(ret)