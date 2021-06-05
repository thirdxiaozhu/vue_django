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


class getTeacherlist(APIView):
    def get(self, request, *args, **kwargs):
        ret_type = request.GET.get('type')
        if ret_type == "1":
            teachers = models.TeacherInfo.objects.all().order_by('id')
            colleges = models.CollegeInfo4tc.objects.all().order_by('id')

            teacherlist = ser.TeacherlistSerializers(teachers, many=True)
            collegelist = ser.College4tclistSerializers(colleges, many=True)

            ret = {
                'code': 1000,
                'colleges': collegelist.data,
                'teacherlist': teacherlist.data,
                'total':teachers.count()
            }

            return Response(ret)
        elif ret_type == "2":
            pre = int(request.GET.get('pre'))
            courses = models.Course.objects.filter(college_id = pre).order_by('id')
            teachers = models.TeacherInfo.objects.filter(college_id = pre).order_by('id')

            courselist = ser.College4tclistSerializers(courses, many=True)
            teacherlist = ser.TeacherlistSerializers(teachers, many=True)

            ret = {
                'code':1000,
                'courses': courselist.data,
                'teacherlist': teacherlist.data,
                'total':teachers.count()
            }

            return Response(ret)

        elif ret_type == "3":
            pre = int(request.GET.get('pre'))
            teachers = models.Course.objects.get(id = pre).teacherinfo_set.all().order_by('id')

            teacherlist = ser.TeacherlistSerializers(teachers, many=True)

            ret = {
                'code':1000,
                'teacherlist': teacherlist.data,
                'total':teachers.count()
            }

            return Response(ret)


class getTeacherinfo(APIView):
    def get(self, request, *args, **kwargs):
        tea_id = request.GET.get('tea_id')
        teacher = models.TeacherInfo.objects.filter(tea_id = tea_id).first()
        courses = models.Course.objects.filter(college_id = teacher.college_id).order_by('id')
        courselist = ser.CourselistSerializers(courses, many=True)
        teacourse = teacher.course.all()
        courseselected = []
        for i in teacourse:
            courseselected.append(i.id)

        location = []
        location.append(teacher.country_id)
        location.append(teacher.province_id)
        location.append(teacher.city_id)
        form={
            'id': teacher.id,
            'tea_id': teacher.tea_id,
            'password': teacher.password,
            'name': teacher.name,
            'sex': teacher.sex,
            'IDnumber': teacher.IDnumber.idnumber,
            'birthday': teacher.birthday,
            'entrytime': teacher.entrytime,
            'outlook': teacher.outlook_id,
            'college':teacher.college_id,
            'title':teacher.title_id,
            'address':location,
        }

        ret={
            'code': 1000,
            'form': form,
            'city': teacher.city.atitle,
            'province': teacher.province.atitle,
            'country': teacher.country.atitle,
            'courses': courselist.data,
            'courseselected': courseselected
        }

        return Response(ret)


class editTeacherOptions(APIView):
    def get(self, request, *args, **kwargs):
        outlooks = models.Outlook.objects.all().order_by('id')
        colleges = models.CollegeInfo4tc.objects.all().order_by('id')
        titles = models.Teacher_title.objects.all().order_by('id')

        outlooklist = ser.OutlooklistSerializers(outlooks, many=True)
        collegelist = ser.College4tclistSerializers(colleges, many=True)
        titlelist = ser.TeachertitlelistSerializers(titles, many=True)

        ret = {
            'code': 1000,
            'outlooklist': outlooklist.data,
            'collegelist': collegelist.data,
            'titlelist': titlelist.data,
        }

        return Response(ret)

class editTeacher(APIView):
    def post(self, request, *args, **kwargs):
        form_json = request.data.get('form')
        outlook = request.data.get('outlook')
        college = request.data.get('college')
        title = request.data.get('title')
        courses = request.data.get('courses')
        #返回的是'4,5'字符串，先使用split分开成字符串列表，再转换成整数列表
        courses = list(map(int, courses.split(',')))
        form = json.loads(form_json)

        new_tea_id = form['tea_id']
        new_password = form['password']
        new_name = form['name']
        new_sex = form['sex']
        new_idnumber = form['IDnumber']
        new_birthday = form['birthday']
        new_entrytime = form['entrytime']
        new_address = form['address']
        new_title = form['title']


        if models.TeacherInfo.objects.filter(Q(tea_id = new_tea_id) & ~Q(id = form['id'])):
            ret={
                'code': 1001,
                'error': "教师号重复,请检查",
            }
            return Response(ret)

        id_stu_flag = models.IDNumber.objects.filter(idnumber=new_idnumber).first()

        if id_stu_flag and id_stu_flag.teacherinfo_set.all().first().id != form['id']:
            ret={
                'code': 1001,
                'error': "身份证号重复,请检查",
            }
            return Response(ret)

        teacher = models.TeacherInfo.objects.filter(id = form['id']).first()
        idnum = models.IDNumber.objects.filter(id=teacher.IDnumber_id).first()
        teacher.tea_id = new_tea_id
        teacher.password = new_password
        teacher.name = new_name
        teacher.sex = new_sex
        idnum.idnumber = new_idnumber
        teacher.birthday = new_birthday
        teacher.entrytime = new_entrytime
        teacher.outlook_id = int(outlook)
        teacher.college_id = int(college)
        teacher.title_id = int(title)
        teacher.country_id = new_address[0]
        teacher.province_id = new_address[1]
        teacher.city_id = new_address[2]
        teacher.course.set(courses)
        print(teacher.title_id)

        teacher.save()
        idnum.save()

        ret={
            'code': 1000
        }
        return Response(ret)



class addTeacher(APIView):
    def post(self, request, *args, **kwargs):
        form_json = request.data.get('form')
        outlook = request.data.get('outlook')
        college = request.data.get('college')
        title = request.data.get('title')
        courses = request.data.get('courses')
        #返回的是'4,5'字符串，先使用split分开成字符串列表，再转换成整数列表
        courses = list(map(int, courses.split(',')))
        form = json.loads(form_json)

        new_tea_id = form['tea_id']
        new_password = form['password']
        new_name = form['name']
        new_sex = form['sex']
        new_idnumber = form['IDnumber']
        new_birthday = form['birthday']
        new_entrytime = form['entrytime']
        new_address = form['address']
        new_title = form['title']


        if models.TeacherInfo.objects.filter(tea_id = new_tea_id):
            ret={
                'code': 1001,
                'error': "教师号重复,请检查",
            }
            return Response(ret)

        id_stu_flag = models.IDNumber.objects.filter(idnumber=new_idnumber).first()

        if id_stu_flag:
            ret={
                'code': 1001,
                'error': "身份证号重复,请检查",
            }
            return Response(ret)

        
        idnumber_id = models.IDNumber.objects.create(idnumber=form['IDnumber'])
        print(idnumber_id , type(idnumber_id))

        new_teacher = models.TeacherInfo.objects.create(
            tea_id = new_tea_id,
            password = new_password,
            name = new_name,
            sex = new_sex,
            birthday = new_birthday,
            entrytime = new_entrytime,
            outlook_id = int(outlook),
            college_id = int(college),
            title_id = int(title),
            IDnumber_id = idnumber_id.id,
            country_id = new_address[0],
            province_id = new_address[1],
            city_id = new_address[2],
        )
        new_teacher.course.set(courses)

        ret = {
            'code': 1000,
        }

        return Response(ret)



class collegeChange(APIView):
    def get(self, request, *args, **kwargs):
        college = request.GET.get('college')
        courses = models.Course.objects.filter(college_id = college).order_by('id')
        courselist = ser.CourselistSerializers(courses, many=True)

        ret = {
            'code': 1000,
            'courses': courselist.data,
        }

        return Response(ret)