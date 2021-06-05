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

class RoomlistSerializers(serializers.ModelSerializer):
    function = serializers.CharField(source="function.name")
    class Meta:
        model = models.ClassRoom
        fields = ('name','capacity','function')


class BuildinglistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = ('id','name')

class FunctionlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Function
        fields = ('id','name')


class TeacherlistSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source="title.name")
    class Meta:
        model = models.TeacherInfo
        fields = ('tea_id','name','sex','title')


class College4tclistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CollegeInfo4tc
        fields = ('id','name')

class TeachertitlelistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher_title
        fields = ('id','name')


class CourselistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id','name')

class OutlooklistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Outlook
        fields = ('id','name')


class TeacherInfoSerializers(serializers.ModelSerializer):
    IDnumber = serializers.CharField(source="IDnumber.idnumber")
    college = serializers.CharField(source="college.name")
    outlook = serializers.CharField(source="outlook.name")
    title = serializers.CharField(source="title.name")
    country = serializers.CharField(source="country.atitle")
    province = serializers.CharField(source="province.atitle")
    city = serializers.CharField(source="city.atitle")
    class Meta:
        model = models.TeacherInfo
        fields = "__all__"