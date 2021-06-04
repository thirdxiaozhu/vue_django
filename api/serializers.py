from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models
import json

class StudentSerializers(serializers.Serializer):

    id = serializers.IntegerField()
    stu_id = serializers.CharField(max_length=20)
    password = serializers.CharField( max_length=50)
    name = serializers.CharField( max_length=20)
    birthday = serializers.DateField()
    IDnumber = serializers.CharField(source="IDnumber.idnumber")
    sex = serializers.CharField( max_length=5)
    entrytime = serializers.DateField()
    grade = serializers.CharField(source="grade.id")
    outlook = serializers.CharField(source="outlook.id")
    country_id = serializers.CharField(source="country.id")
    province_id = serializers.CharField(source="province.id")
    city_id = serializers.CharField(source="city.id")
    College_id = serializers.CharField(source="College.id")
    Major_id = serializers.CharField(source="Major.id")
    Class_id = serializers.CharField(source="Class.id")
    credit = serializers.FloatField()


class StudentlistSerializers(serializers.ModelSerializer):
    #model序列化自定义外键字段
    Class = serializers.CharField(source="Class.class_id")
    class Meta:
        model = models.StudentInfo
        fields = ('stu_id','name','sex','Class')
