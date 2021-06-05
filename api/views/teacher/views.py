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


class initTeacherInfo(APIView):
    def get(self , request, *args, **kwargs):
        tea_id = request.GET.get('tea_id')
        teacher = models.TeacherInfo.objects.filter(tea_id = tea_id).first()

        teacherinfo = ser.TeacherInfoSerializers(teacher, many=False)
        print(teacherinfo.data)
        ret={
            'code': 1000,
            'form': teacherinfo.data
        }
        return Response(ret)