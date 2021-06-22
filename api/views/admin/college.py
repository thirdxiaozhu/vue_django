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


class initMajorInfo(APIView):
    def get(self, request, *args, **kwargs):
        major_id = request.GET.get('maj_id')
        print(major_id)
        major = models.MajorInfo.objects.filter(id = major_id).first()
        majordata = ser.MajorlistSerializers(major, many=False)
        print(majordata.data)
        ret = {
            'code': 1000,
            'majordata': majordata.data,
        }

        return Response(ret)


class editMajorOptions(APIView):
    def get(self, request, *args, **kwargs):
        college = request.GET.get('col_id')
        colleges = models.CollegeInfo4tc.objects.all().order_by('id')
        collegelist = ser.College4tclistSerializers(colleges, many=True)

        courses = models.Course.objects.all().order_by('id')
        course_id = []
        course_cou_id = []
        course_name = []
        for i in courses:
            course_id.append(i.id)
            course_cou_id.append(i.cou_id)
            course_name.append(i.name)
            print(i.name, i.cou_id, i.id)


        ret = {
            'code': 1000,
            'colleges': collegelist.data,
            'course_id': course_id,
            'course_cou_id': course_cou_id,
            'course_name': course_name,
        }

        return Response(ret)


class postMajorSubmit(APIView):
    def post(self, request, *args, **kwargs):
        form = request.data.get('form')
        form = json.loads(form)
        print(form)
        major = models.MajorInfo.objects.filter(id=form['id']).first()
        ms = ser.MajorlistSerializers(major, data=form)
        if ms.is_valid():
            ms.save()
            return Response({'code': 1000})
        else:
            ret = {
                'code':1001,
                'error':ms.errors
            }
            return Response(ret)
