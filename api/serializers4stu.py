from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models
import json


class CourseinfoSerializers(serializers.ModelSerializer):
    college = serializers.CharField(source="college.name")
    function = serializers.CharField(source="function.name")
    class Meta:
        model = models.Course
        fields = ('cou_id','name','classhour','college','function')




class StudentInfoSerializers(serializers.ModelSerializer):
    IDnumber = serializers.CharField(source="IDnumber.idnumber")
    College = serializers.CharField(source="College.name")
    Major = serializers.CharField(source="Major.name")
    Class = serializers.CharField(source="Class.class_id")
    outlook = serializers.CharField(source="outlook.name")
    country = serializers.CharField(source="country.atitle")
    province = serializers.CharField(source="province.atitle")
    city = serializers.CharField(source="city.atitle")


    class Meta:
        model = models.StudentInfo
        fields = "__all__"