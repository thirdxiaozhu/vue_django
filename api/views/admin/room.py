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


class roomList(APIView):
    def get(self, request, *args, **kwargs):
        room = models.ClassRoom.objects.all().order_by('id')
        buildings = models.Building.objects.all()
        functions = models.Function.objects.all().order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(room, request, self)
        roomlist = ser.RoomlistSerializers(page_role, many = True)

        buildings = ser.BuildinglistSerializers(buildings, many=True)
        functionlist = ser.FunctionlistSerializers(functions, many=True)

        ret = {
            'code': 1000,
            'roomlist': roomlist.data,
            'buildings': buildings.data,
            'functions': functionlist.data,
            'total':room.count()
        }

        return Response(ret)


class getFunctions(APIView):
    def get(self, request, *args, **kwargs):
        functions = models.Function.objects.all()
        functionlist = ser.FunctionlistSerializers(functions, many=True)

        ret = {
            'code': 1000,
            'functions': functionlist.data,
        }
        
        return Response(ret)

class getRoomInfo(APIView):
    def get(self, request, *args, **kwargs):
        print("aaaa" + request.GET.get('roomname'))
        room = models.ClassRoom.objects.filter(name = request.GET.get('roomname')).first()
        ret = {
            'code': 1000,
            'capacity': room.capacity,
            'function' : room.function_id
        }

        return Response(ret)


class filterRoom(APIView):
    def get(self, request, *args, **kwargs):
        building = request.GET.get('building')
        function = request.GET.get('function')
        capacity = request.GET.get('capacity')

        #做一次空值转换
        if capacity == '':
            capacity = 0
        capacity = int(capacity)-1

        if building == '' and function == '':
            rooms = models.ClassRoom.objects.filter(capacity__gt = capacity-1).order_by('id')
        elif function == '':
            rooms = models.ClassRoom.objects.filter(Q(capacity__gt = capacity-1) & Q(building_id = building)).order_by('id')
        elif building == '':
            rooms = models.ClassRoom.objects.filter(Q(capacity__gt = capacity-1) & Q(function_id = function)).order_by('id')
        else:
            rooms = models.ClassRoom.objects.filter(Q(capacity__gt = capacity-1) & Q(function_id = function) & Q(building_id = building)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(rooms, request, self)
        roomlist = ser.RoomlistSerializers(page_role, many = True)

        ret = {
            'code':1000,
            'roomlist': roomlist.data,
            'total': rooms.count()
        }

        return Response(ret)