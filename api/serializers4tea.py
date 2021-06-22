from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models
import json


class StudentlistSerializers(serializers.ModelSerializer):
    Class = serializers.CharField(source="Class.class_id")
    class Meta:
        model = models.StudentInfo
        fields = ('id','stu_id','name','Class','sex')

