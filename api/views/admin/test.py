from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models, page
from api import serializers as ser
import json


class initCourseList4test(APIView):
    def get(self, request, *args, **kwargs):
        mod = request.GET.get('mod')
        
        if mod == "1":
            courses = models.Course.objects.filter(isarranged = False).order_by('id')
        else:
            courses = models.Course.objects.filter(Q(college=request.GET.get('college')) & Q(isarranged = False)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(courses, request, self)
        courselist = ser.Courseinfo4testSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'form': courselist.data,
            'total': courses.count()
        }
        return Response(ret)


class getCollegeList4test(APIView):
    def get(self, request, *args, **kwargs):
        colleges = models.CollegeInfo4tc.objects.all().order_by('id')
        collegelist = ser.College4tclistSerializers(colleges, many=True)

        ret = {
            'code': 1000,
            'colleges': collegelist.data,
        }

        return Response(ret)

class updateChoice(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data.get('time'))
        course = models.Course.objects.filter(id = request.data.get('id')).first()
        course.isarranged = True
        course.testtime = request.data.get('time')
        course.save()

        
        return Response({'code': 1000})


class initCourseList4testarr(APIView):
    def get(self, request, *args, **kwargs):
        mod = request.GET.get('mod')
        
        if mod == "1":
            courses = models.Course.objects.filter(isarranged = True).order_by('id')
        else:
            courses = models.Course.objects.filter(Q(college=request.GET.get('college')) & Q(isarranged = True)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(courses, request, self)
        courselist = ser.Courseinfo4testSerializers(page_role, many=True)
        print(courselist.data)

        ret = {
            'code': 1000,
            'form': courselist.data,
            'total': courses.count()
        }
        return Response(ret)


class updateChoicearr(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data.get('time'))
        course = models.Course.objects.filter(id = request.data.get('id')).first()
        course.isarranged = True
        course.testtime = request.data.get('time')
        course.save()

        
        return Response({'code': 1000})