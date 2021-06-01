from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from django.db.models import Q
from api import models
import json

class studentStatus(APIView):
    versioning_class =  URLPathVersioning
    def get(self,request,*args,**kwargs):
        students = models.StudentInfo.objects.all()
        stulist=[]
        for i in students:
            data={
                'stu_id':i.stu_id,
                'name':i.name,
                'sex':i.sex,
                'class': i.Class.class_id,
            }
            stulist.append(data)

        ret = {
            'code': 1000,

            'students': stulist,
        }
        return Response(ret)


class studentInfo(APIView):
    def get(self,request, *args , **kwargs):
        stu_id = request.GET.get('stu_id')
        student = models.StudentInfo.objects.filter(stu_id = stu_id).first()

        location = []
        classes = []
        location.append(student.native.Province.Country.id)
        location.append(student.native.Province.id)
        location.append(student.native.id)
        classes.append(student.Class.major.college.id)
        classes.append(student.Class.major.id)
        classes.append(student.Class.id)
        print(classes)
        form={
            'id': student.id,
            'stu_id': student.stu_id,
            'password': student.password,
            'name': student.name,
            'sex': student.sex,
            'idnumber': student.IDnumber.idnumber,
            'grade': student.grade.id,
            'birthday': student.birthday,
            'entryday': student.entrytime,
            'credit': student.credit,
            'outlook': student.outlook_id,
            'address':location,
            'classes' : classes,
        }

        ret={
            'code': 1000,
            'form': form,
            'city': student.native.atitle,
            'province': student.native.Province.atitle,
            'country': student.native.Province.Country.atitle,
            'college': student.Class.major.college.name,
            'major': student.Class.major.name,
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
                'value': str(i.id),
                'label': i.name,
            }
            outlooklist.append(data)

        for i in grades:
            data={
                'value': str(i.id),
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
        new_idnumber = form['idnumber']
        new_grade = form['grade']
        new_birthday = form['birthday']
        new_entryday = form['entryday']
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
        idnum = models.IDNumber.objects.filter(idnumber=new_idnumber).first()
        print(new_class)
        student.stu_id = new_stu_id
        student.password = new_password
        student.name = new_name
        student.sex = new_sex
        idnum.idnumber = new_idnumber
        student.birthday = new_birthday
        student.entryday = new_entryday
        student.credit = new_credit
        student.outlook_id = outlook
        student.grade_id = grade
        student.native_id = new_address[2]
        student.nation_id = new_address[0]
        student.Class_id = new_class[2]
        
        student.save()
        idnum.save()

        ret={
            'code': 1000
        }
        return Response(ret)