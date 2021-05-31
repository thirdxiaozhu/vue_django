from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
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
            'stu_id': student.stu_id,
            'password': student.password,
            'name': student.name,
            'sex': student.sex,
            'idnumber': student.IDnumber.idnumber,
            'grade': student.grade,
            'birthday': student.birthday,
            'entryday': student.entrytime,
            'credit': student.credit,
            'outlook': student.outlook_id,
            'address':location,
            'class' : classes,
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

        print(student)
        return Response(ret)

class editstuoptions(APIView):
    def get(self, request, *args, **kwargs):
        outlooks = models.Outlook.objects.all()
        outlooklist = []
        for i in outlooks:
            data={
                'value': str(i.id),
                'label': i.name,
            }
            outlooklist.append(data)

        ret={
            'code': 1000,
            'outlooklist':outlooklist,
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