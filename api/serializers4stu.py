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
        students = models.Student2Relation.objects.filter(relation = obj.id)
        return str(students.count()) + " / " + str(obj.stuquantity)


class College4tclistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CollegeInfo4tc
        fields = ('id','name')


class Courseinfo4planSerializers(serializers.ModelSerializer):
    college = serializers.CharField(source="college.name")
    function = serializers.CharField(source="function.name")
    betyear = serializers.CharField(source="betyear.name")
    elective = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = "__all__"

    def get_elective(self, obj):
        if obj.elective == False:
            return "否"
        else:
            return "是"

class Courseinfo4plandrawSerializers(serializers.ModelSerializer):
    college = serializers.CharField(source="college.name")
    function = serializers.CharField(source="function.name")
    betyear = serializers.CharField(source="betyear.name")

    class Meta:
        model = models.Course
        fields = "__all__"


class FunctionlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Function
        fields = ('id','name')


class Relationlist4testSerializers(serializers.ModelSerializer):
    teacher = serializers.CharField(source="teacher.name")
    course = serializers.CharField(source="course.name")
    testtime = serializers.SerializerMethodField()
    class Meta:
        model = models.MainRelation
        fields = ('course','teacher','testtime')

    def get_testtime(self, obj):
        if obj.course.testtime:
            return obj.course.testtime 
        else:
            return "尚未排考"


class GradeSerializers(serializers.ModelSerializer):
    teacher = serializers.CharField(source="relation.teacher.name")
    #teacher = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    class Meta:
        model = models.Student2Relation
        fields = ('course','teacher','grade')

    def get_course(self, obj):
        return obj.relation.course.name
    
    def get_grade(self, obj):
        if obj.grade:
            return obj.grade
        else:
            return "尚未录入"

class MessagelistSerializers(serializers.ModelSerializer):
    messagetype = serializers.CharField(source="messagetype.name")
    finishtime = serializers.SerializerMethodField()
    isFinished = serializers.SerializerMethodField()
    fromwho = serializers.SerializerMethodField()
    towho = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Message
        fields = "__all__"

    def get_finishtime(self, obj):
        if obj.finishtime:
            return obj.finishtime
        else:
            return "-"

    def get_isFinished(self, obj):
        if obj.isFinished:
            return "是"
        else:
            return "否"

    def get_towho(self, obj):
        if obj.towho == "student":
            return str(obj.student.stu_id) + " " + obj.student.name
        elif obj.towho == "teacher":
            return str(obj.teacher.tea_id) + " " + obj.teacher.name
        else :
            return "管理员"


    def get_fromwho(self, obj):
        if obj.fromwho == "student":
            return str(obj.student.stu_id) + " " + obj.student.name
        elif obj.fromwho == "teacher":
            return str(obj.teacher.tea_id) + " " + obj.teacher.name
        else :
            return "管理员"