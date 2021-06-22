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
        fields = ('id','cou_id','name','classhour','college','function')


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



class RelationlistSerializers(serializers.ModelSerializer):
    course = serializers.CharField(source="course.name")
    classroom = serializers.CharField(source="classroom.name")
    teacher = serializers.CharField(source="teacher.name")
    student = serializers.SerializerMethodField()
    classtime = serializers.SerializerMethodField()
    class Meta:
        model = models.MainRelation
        fields = "__all__"

    #多对多钩子函数序列化，必须以get_ + model表名作为方法名
    def get_classtime(self, obj):
        temp = []
        for obj in obj.classtime.all():
            temp.append(obj.name)
        return temp

    def get_student(self, obj):
        return str(obj.student.all().count()) + " / " + str(obj.stuquantity)