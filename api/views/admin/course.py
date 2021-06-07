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

class getCourseList(APIView):
    def get(self,request,*args,**kwargs):
        functions = models.Function.objects.all().order_by('id')
        colleges = models.CollegeInfo4tc.objects.all().order_by('id')
        courses = models.Course.objects.all().order_by('id')
        
        #分页
        pages = page.MyLimitOffsetPagination()
        #获取自己继承的类
        page_role = pages.paginate_queryset(courses, request, self)
        courselist = ser.CourselistSerializers4cou(page_role, many=True)
        functionlist = ser.FunctionlistSerializers(functions, many = True)
        collegelist = ser.College4tclistSerializers(colleges, many=True)

        print(courselist.data)

        ret = {
            'code': 1000,
            'colleges': collegelist.data,
            'functions': functionlist.data,
            'courselist': courselist.data,
            'total': courses.count()
        }

        return Response(ret)


class filterCourseList(APIView):
    def get(self,request,*args,**kwargs):
        courses = models.Course.objects.all().order_by('id')
        
        #分页
        pages = page.MyLimitOffsetPagination()
        #获取自己继承的类
        page_role = pages.paginate_queryset(courses, request, self)
        courselist = ser.CourselistSerializers4cou(page_role, many=True)

        ret = {
            'code': 1000,
            'courselist': courselist.data,
            'total': courses.count()
        }

        return Response(ret)


class initCourseInfo(APIView):
    def get(self,request,*args,**kwargs):
        cou_id = request.GET.get('cou_id')
        course = models.Course.objects.filter(cou_id = cou_id).first()
        courselist = ser.CourseinfoSerializers(course, many=False)

        ret = {
            'code': 1000,
            'form': courselist.data,
        }

        return Response(ret)


class getCourseOption(APIView):
    def get(self,request,*args,**kwargs):
        functions = models.Function.objects.all().order_by('id')
        colleges = models.CollegeInfo.objects.all().order_by('id')
        betyear = models.Betteryear.objects.all().order_by('id')
        pre_courses = models.Course.objects.all().order_by('id')


        functionlist = ser.FunctionlistSerializers(functions, many = True)
        collegelist = ser.College4tclistSerializers(colleges, many=True)
        betyearlist = ser.BetyearlistSerializers(betyear, many=True)

        pre_course_id = []
        pre_course_name = []
        for i in pre_courses:
            pre_course_id.append(i.cou_id)
            pre_course_name.append(i.name)

        ret = {
            'code': 1000,
            'colleges': collegelist.data,
            'functions': functionlist.data,
            'betyear': betyearlist.data,
            'pre_course_id': pre_course_id,
            'pre_course_name': pre_course_name,
        }

        return Response(ret)