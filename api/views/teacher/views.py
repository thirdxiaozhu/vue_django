from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from django.utils import timezone
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
            print(int(i['grade']))
            if int(i['grade']) < 0 or int(i['grade']) > 100:
                return Response({'code': 1001, 'error': "仅接受处于0-100的正数"})
            change = models.Student2Relation.objects.filter(Q(relation = relation) & Q(student = i['id'])).first()
            change.grade = i['grade']
            change.save()    
            
        return Response({'code': 1000})



class getSendlist(APIView):
    def get(self, request, *args, **kwargs):
        teacher = models.TeacherInfo.objects.filter(tea_id = request.GET.get('tea_id')).first()
        print(teacher)
        messages = models.Message.objects.filter(Q(fromwho="teacher") & Q(teacher = teacher)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(messages, request, self)
        messagelist = ser.MessagelistSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'messages': messagelist.data,
            'total': messages.count()
        }
        return Response(ret)

class replyMessage(APIView):
	def post(self, request, *args, **kwargs):
		mes_id = request.data.get('id')
		messages = models.Message.objects.filter(id = mes_id).order_by('id').first()
		messages.reply = request.data.get('reply')
		messages.isWatched = True
		messages.isFinished = True
		messages.finishtime = timezone.now()
		messages.result = "完成"
		messages.save()

		return Response({'code': 1000})


class rejectMessage(APIView):
	def post(self, request, *args, **kwargs):
		mes_id = request.data.get('id')
		messages = models.Message.objects.filter(id = mes_id).order_by('id').first()
		messages.reply = request.data.get('reply')
		messages.isWatched = True
		messages.isFinished = True
		messages.finishtime = timezone.now()
		messages.result = "驳回"
		messages.save()

		return Response({'code': 1000})

class postMessage(APIView):
    def post(self, request, *args, **kwargs):
        form = json.loads(request.data.get('form'))
        teacher = models.TeacherInfo.objects.filter(tea_id = request.data.get('tea_id')).first()
        print(teacher)

        if form['option'] == "1":
            student = models.StudentInfo.objects.filter(stu_id = form['towho']).first()
            if student:
                models.Message.objects.create(
                    fromwho = "teacher",
                    towho = "student",
                    student = student,
                    teacher = teacher,
                    messagetype = models.MessageType.objects.get(id = 3),
                    title = form['title'],
                    content = form['content'],
                )
                return Response({'code': 1000})
            else:
                return Response({'code': 1001, 'error': "找不到该学生，请核对学号"})
        else :
            admin = models.AdminInfo.objects.filter(id = 1).first()
            models.Message.objects.create(
                fromwho = "teacher",
                towho = "admin",
                admin = admin,
                teacher = teacher,
                messagetype = models.MessageType.objects.get(id = 3),
                title = form['title'],
                content = form['content'],
            )
            return Response({'code': 1000})


class getSavelist(APIView):
    def get(self, request, *args, **kwargs):
        teacher = models.TeacherInfo.objects.filter(tea_id = request.GET.get('tea_id')).first()
        print(teacher)
        messages = models.Message.objects.filter(Q(towho="teacher") & Q(teacher = teacher)).order_by('id')
        print(messages)

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(messages, request, self)

        messagelist = ser.MessagelistSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'messages': messagelist.data,
            'total': messages.count()
        }
        return Response(ret)