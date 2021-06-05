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

class studentStatus(APIView):
    versioning_class =  URLPathVersioning
    def get(self,request,*args,**kwargs):
        students = models.StudentInfo.objects.all().order_by('stu_id')
        #分页
        pages = page.MyLimitOffsetPagination()
        #获取自己继承的类
        page_role = pages.paginate_queryset(students, request, self)
        #序列化分页后的内容并返回
        stulist = ser.StudentlistSerializers(page_role,many = True)
        print(stulist)

        ret = {
            'code': 1000,
            'students': stulist.data,
            'total':students.count()
        }
        return Response(ret)


class studentInfo(APIView):
    def get(self,request, *args , **kwargs):
        stu_id = request.GET.get('stu_id')
        student = models.StudentInfo.objects.filter(stu_id = stu_id).first()

        location = []
        classes = []
        location.append(student.country_id)
        location.append(student.province_id)
        location.append(student.city_id)
        classes.append(student.College_id)
        classes.append(student.Major_id)
        classes.append(student.Class_id)
        form={
            'id': student.id,
            'stu_id': student.stu_id,
            'password': student.password,
            'name': student.name,
            'sex': student.sex,
            'IDnumber': student.IDnumber.idnumber,
            'grade': student.grade.id,
            'birthday': student.birthday,
            'entrytime': student.entrytime,
            'credit': student.credit,
            'outlook': student.outlook_id,
            'address':location,
            'classes' : classes,
        }

        ret={
            'code': 1000,
            'form': form,
            'city': student.city.atitle,
            'province': student.province.atitle,
            'country': student.country.atitle,
            'college': student.College.name,
            'major': student.Major.name,
            'class':student.Class.class_id, 
        }

        return Response(ret)

class editstuoptions(APIView):
    def get(self, request, *args, **kwargs):
        outlooks = models.Outlook.objects.all()
        grades = models.StudentGrade.objects.all()
        outlooklist = []
        gradelist = []
        for i in outlooks:
            data={
                'value': i.id,
                'label': i.name,
            }
            outlooklist.append(data)

        for i in grades:
            data={
                'value': i.id,
                'label': i.name,
            }
            gradelist.append(data)

        ret={
            'code': 1000,
            'outlooklist':outlooklist,
            'gradelist':gradelist,
        }
        
        return Response(ret)
        

#获取地名级联
class getlocation(APIView):
    def get(self, request, *args, **kwargs):
        ret_type = request.GET.get('type')
        if ret_type == 'country':
            countries = models.Countries.objects.all()
            countrylist = []
            for i in countries:
                data={
                    'value': str(i.id),
                    'label': i.atitle,
                }
                countrylist.append(data)

            ret={
                'code': 1000,
                'data':countrylist,
            }
            return Response(ret)
        elif ret_type == 'province':
            provinces = models.Provinces.objects.filter(Country_id = request.GET.get('country_id'))

            provincelist = []
            for i in provinces:
                data={
                    'value': str(i.id),
                    'label': i.atitle,
                }
                provincelist.append(data)

            ret={
                'code': 1000,
                'data':provincelist,
            }
            return Response(ret)
        else:
            cities = models.Cities.objects.filter(Province_id = request.GET.get('province_id'))

            citylist = []
            for i in cities:
                data={
                    'value': str(i.id),
                    'label': i.atitle,
                    'leaf': 'level >= 2' #设置中止叶节点
                }
                citylist.append(data)

            ret={
                'code': 1000,
                'data':citylist,
            }
            return Response(ret)

class getclass(APIView):
    def get(self, request, *args, **kwargs):
        ret_type = request.GET.get('type')
        if ret_type == "college":
            colleges = models.CollegeInfo.objects.all()
            collegelist = []
            for i in colleges:
                data={
                    'value': str(i.id),
                    'label': i.name,
                }
                collegelist.append(data)

            ret={
                'code': 1000,
                'data':collegelist,
            }
            return Response(ret)

        elif ret_type == "major":
            majors = models.MajorInfo.objects.filter(college_id = request.GET.get('college_id'))
            majorlist = []
            for i in majors:
                data={
                    'value': str(i.id),
                    'label': i.name,
                }
                majorlist.append(data)

            ret={
                'code':1000,
                'data': majorlist
            }
            return Response(ret)

        else :
            classes = models.ClassInfo.objects.filter(major_id = request.GET.get('major_id'))
            classlist = []
            for i in classes:
                data={
                    'value': str(i.id),
                    'label': i.class_id,
                    'leaf': 'level >= 2' #设置中止叶节点
                }
                classlist.append(data)

            ret={
                'code':1000,
                'data': classlist
            }
            return Response(ret)


class editstudent(APIView):
    def post(self,request, *args ,**kwargs):
        form_json = request.data.get('form')
        outlook = request.data.get('outlook')
        grade = request.data.get('grade')

        form = json.loads(form_json)
        new_stu_id = form['stu_id']
        new_password = form['password']
        new_name = form['name']
        new_sex = form['sex']
        new_idnumber = form['IDnumber']
        new_grade = form['grade']
        new_birthday = form['birthday']
        new_entrytime = form['entrytime']
        new_credit = form['credit']
        new_address = form['address']
        new_class = form['classes']


        if models.StudentInfo.objects.filter(Q(stu_id = new_stu_id) & ~Q(id = form['id'])):
            ret={
                'code': 1001,
                'error': "学号重复,请检查",
            }
            return Response(ret)

        id_stu_flag = models.IDNumber.objects.filter(idnumber=new_idnumber).first()

        if id_stu_flag and id_stu_flag.studentinfo_set.all().first().id != form['id']:
            ret={
                'code': 1001,
                'error': "身份证号重复,请检查",
            }
            return Response(ret)

        student = models.StudentInfo.objects.filter(id = form['id']).first()
        idnum = models.IDNumber.objects.filter(id=student.IDnumber_id).first()
        student.stu_id = new_stu_id
        student.password = new_password
        student.name = new_name
        student.sex = new_sex
        idnum.idnumber = new_idnumber
        student.birthday = new_birthday
        student.entrytime = new_entrytime
        student.credit = new_credit
        student.outlook_id = outlook
        student.grade_id = grade
        student.country_id = new_address[0]
        student.province_id = new_address[1]
        student.city_id = new_address[2]
        student.College_id = new_class[0]
        student.Major_id = new_class[1]
        student.Class_id = new_class[2]
        
        student.save()
        idnum.save()

        ret={
            'code': 1000
        }
        return Response(ret)

class getOrganize(APIView):
    def get(self, request, *args, **kwargs):
        org_type = request.GET.get('type')
        pre = request.GET.get('pre')

        print(type(org_type) , type(pre))

        if org_type == "1":
            colleges = models.CollegeInfo.objects.all()
            collegelist = []
            for i in colleges:
                data={
                    'value': str(i.id),
                    'label': i.name,
                }
                collegelist.append(data)

            students = models.StudentInfo.objects.all().order_by('stu_id')

            #分页
            pages = page.MyLimitOffsetPagination()
            page_role = pages.paginate_queryset(students, request, self)
            stulist = ser.StudentlistSerializers(page_role,many = True)

            ret = {
                'code': 1000,
                'data': collegelist,
                'students': stulist.data,
                'total':students.count()
            }

            return Response(ret)
        
        elif org_type == "2":
            majors = models.MajorInfo.objects.filter(college_id = int(pre))
            majorlist = []
            for i in majors:
                data={
                    'value': str(i.id),
                    'label': i.name,
                }
                majorlist.append(data)

            students = models.StudentInfo.objects.filter(College_id = int(pre)).order_by('stu_id')

            #分页
            pages = page.MyLimitOffsetPagination()
            page_role = pages.paginate_queryset(students, request, self)
            stulist = ser.StudentlistSerializers(page_role,many = True)

            ret = {
                'code': 1000,
                'majors': majorlist,
                'students': stulist.data,
                'total':students.count()
            }

            return Response(ret)

        elif org_type == "3":
            classes = models.ClassInfo.objects.filter(major_id = int(pre))
            classlist = []
            for i in classes:
                data={
                    'value': str(i.id),
                    'label': i.class_id,
                }
                classlist.append(data)


            students = models.StudentInfo.objects.filter(Major_id = int(pre)).order_by('stu_id')
            pages = page.MyLimitOffsetPagination()
            page_role = pages.paginate_queryset(students, request, self)
            stulist = ser.StudentlistSerializers(page_role,many = True)

            ret = {
                'code': 1000,
                'classes': classlist,
                'students': stulist.data,
                'total':students.count()
            }
            return Response(ret)

        elif org_type == "4":
            students = models.StudentInfo.objects.filter(Class_id = int(pre)).order_by('stu_id')

            pages = page.MyLimitOffsetPagination()
            page_role = pages.paginate_queryset(students, request, self)
            stulist = ser.StudentlistSerializers(page_role,many = True)

            ret = {
                'code': 1000,
                'students': stulist.data,
                'total':students.count()
            }

            return Response(ret)



class addStudent(APIView):
    def post(self,request, *args , **kwargs):
        form_json = request.data.get('form')
        outlook = request.data.get('outlook')
        grade = request.data.get('grade')

        form = json.loads(form_json)
        new_stu_id = form['stu_id']
        new_password = form['password']
        new_name = form['name']
        new_sex = form['sex']
        new_idnumber = form['IDnumber']
        new_grade = form['grade']
        new_birthday = form['birthday']
        new_entrytime = form['entrytime']
        new_credit = form['credit']
        new_address = form['address']
        new_class = form['classes']


        if models.StudentInfo.objects.filter(stu_id = new_stu_id):
            ret={
                'code': 1001,
                'error': "学号重复,请检查",
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

        models.StudentInfo.objects.create(
            stu_id = new_stu_id,
            password = new_password,
            name = new_name,
            sex = new_sex,
            birthday = new_birthday,
            entrytime = new_entrytime,
            credit = new_credit,
            outlook_id = outlook,
            grade_id = grade,
            IDnumber_id = idnumber_id.id,
            country_id = new_address[0],
            province_id = new_address[1],
            city_id = new_address[2],
            College_id = new_class[0],
            Major_id = new_class[1],
            Class_id = new_class[2],
        )

        ret = {
            'code': 1000,
        }

        return Response(ret)


class studentInfoSer(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        students = models.StudentInfo.objects.filter(stu_id = stu_id)
        ss = ser.StudentSerializers(students,many=True)
        defaultlocation = students[0].country.atitle + "/" + students[0].province.atitle + "/" + students[0].city.atitle
        defaultorganize = students[0].College.name + "/" + students[0].Major.name + "/" + students[0].Class.class_id
        
        ret={
            'code': 1000,
            'form': ss.data[0],
            'location' : defaultlocation,
            'organize' : defaultorganize
        }
        return Response(ret)



class deleteStudent(APIView):
    def get(self, request, *args, **kwargs):
        print(request.GET.get('stuid'))
        models.StudentInfo.objects.filter(stu_id = request.GET.get('stuid')).first().delete()

        ret = {'code': 1000}
        print(ret)
        return Response(ret)