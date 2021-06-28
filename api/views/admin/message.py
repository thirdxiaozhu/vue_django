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

class getSendlist(APIView):
	def get(self, request, *args, **kwargs):
		messages = models.Message.objects.filter(towho="admin").order_by('id')

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