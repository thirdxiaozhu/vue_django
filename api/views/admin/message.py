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
import json

class getSavelist(APIView):
	def get(self, request, *args, **kwargs):
		messages = models.Message.objects.filter(towho="admin")

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
		messages = models.Message.objects.filter(id = mes_id).first()
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
		messages = models.Message.objects.filter(id = mes_id).first()
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
        admin = models.AdminInfo.objects.filter(adm_id = 1).first()

        if form['option'] == "1":
            student = models.StudentInfo.objects.filter(stu_id = form['towho']).first()
            if student:
                models.Message.objects.create(
                    fromwho = "admin",
                    towho = "student",
                    student = student,
                    admin = admin,
                    messagetype = models.MessageType.objects.get(id = 3),
                    title = form['title'],
                    content = form['content'],
                )
                return Response({'code': 1000})
            else:
                return Response({'code': 1001, 'error': "找不到该学生，请核对学号"})
        else :
            teacher = models.TeacherInfo.objects.filter(tea_id = form['towho']).first()
            if teacher:
                models.Message.objects.create(
                    fromwho = "admin",
                    towho = "teacher",
                    admin = admin,
                    teacher = teacher,
                    messagetype = models.MessageType.objects.get(id = 3),
                    title = form['title'],
                    content = form['content'],
                )
                return Response({'code': 1000})
            else:
                return Response({'code': 1001, 'error': "找不到该教师，请核对教工号"})


class getSendlist(APIView):
    def get(self, request, *args, **kwargs):
        admin = models.AdminInfo.objects.filter(id = 1).first()
        messages = models.Message.objects.filter(fromwho="admin")

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(messages, request, self)
        messagelist = ser.MessagelistSerializers(page_role, many=True)

        print(messages.count())
        ret = {
            'code': 1000,
            'messages': messagelist.data,
            'total': messages.count()
        }
        return Response(ret)