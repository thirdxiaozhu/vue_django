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
    course = serializers.SerializerMethodField()

    class Meta:
        model = models.TeacherInfo
        fields = "__all__"

    #多对多钩子函数序列化，必须以get_ + model表名作为方法名
    def get_course(self, obj):
        temp = []
        for obj in obj.course.all():
            temp.append(obj.name)
        return temp


class CourselistSerializers4cou(serializers.ModelSerializer):
    college = serializers.CharField(source="college.name")
    function = serializers.CharField(source="function.name")
    elective = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ('id','cou_id','name','classhour','college','function','elective')

    #实现自定义返回(elective是布尔值，js无法回显布尔)
    def get_elective(self, obj):
        if obj.elective == False:
            return "否"
        else:
            return "是"


class CourseinfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

class BetyearlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Betteryear
        fields = "__all__"


class PreCourseidlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id','cou_id')

class PreCoursenamelistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id','name')



class CollegelistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CollegeInfo
        fields = "__all__"


class MajorlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.MajorInfo
        fields = "__all__"


class ClasslistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ClassInfo
        fields = "__all__"



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



class Relation4RoomlistSerializers(serializers.ModelSerializer):
    course = serializers.CharField(source="course.name")
    teacher = serializers.CharField(source="teacher.name")
    classtime = serializers.SerializerMethodField()
    class Meta:
        model = models.MainRelation
        fields = ('course','classtime','teacher')

    def get_classtime(self, obj):
        temp = []
        for obj in obj.classtime.all():
            temp.append(obj.id)
        return temp


class ClassTimelistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ClassTime
        fields = "__all__"


class ClassRoomlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ClassRoom
        fields = ('id', 'name')



        