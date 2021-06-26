from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from rest_framework import serializers
from api import models, page
from api import serializers as ser
from api import serializers4tea as ser_tea
import json


class initTeacherInfo(APIView):
    def get(self , request, *args, **kwargs):
        tea_id = request.GET.get('tea_id')
        teacher = models.TeacherInfo.objects.filter(tea_id = tea_id).first()

        teacherinfo = ser.TeacherInfoSerializers(teacher, many=False)
        print(teacherinfo.data)
        ret={
            'code': 1000,
            'form': teacherinfo.data
        }
        return Response(ret)


class getScheduled(APIView):
    def get(self, request, *args, **kwargs):
        tea_id = request.GET.get('tea_id')

        id = models.TeacherInfo.objects.filter(tea_id=tea_id).first().id
        relations = models.MainRelation.objects.filter(teacher_id = id).order_by('id')
        relationlist = ser.RelationlistSerializers(relations, many = True)

        print(relationlist.data)
        ret = {
            'code': 1000,
            'relationlist': relationlist.data
        }
        return Response(ret)



class initStudentList(APIView):
    def get(self , request, *args, **kwargs):
        #students = models.MainRelation.objects.filter(id = request.GET.get('relation_id')).first().student.all().order_by('id')
        students = models.Student2Relation.objects.filter(relation = request.GET.get('relation_id')).values_list('student', flat=True)
        students = models.StudentInfo.objects.filter(id__in = list(students)).order_by('id')
        studentlist = ser_tea.StudentlistSerializers(students, many=True)


        ret={
            'code': 1000,
            'students': studentlist.data
        }
        return Response(ret)


class ifarrange(APIView):
    def get(self , request, *args, **kwargs):
        print(request.GET.get('id'))
        isarranged = models.MainRelation.objects.filter(id = request.GET.get('id')).first().course.isarranged
        print(isarranged)
        if isarranged:
            return Response({'code': 1000})
        else:
            return Response({'code': 1001})


class getScheduled4test(APIView):
    def get(self, request, *args, **kwargs):
        tea_id = request.GET.get('tea_id')

        id = models.TeacherInfo.objects.filter(tea_id=tea_id).first().id
        relations = models.MainRelation.objects.filter(teacher_id = id).order_by('id')
        relationlist = ser.Relationlist4testSerializers(relations, many = True)

        print(relationlist.data)
        ret = {
            'code': 1000,
            'relationlist': relationlist.data
        }
        return Response(ret)

class updateGrade(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get('tableData')
        relation = request.data.get('relation')
        data = json.loads(data)
        for i in data:
            change = models.Student2Relation.objects.filter(Q(relation = relation) & Q(student = i['id'])).first()
            change.grade = i['grade']
            change.save()    
            
        return Response({'code': 1000})