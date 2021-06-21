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

class getScheduled(APIView):
    def get(self, request, *args, **kwargs):
        relations = models.MainRelation.objects.all().order_by('id')
        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(relations, request, self)
        relationlist = ser.RelationlistSerializers(page_role, many = True)

        ret = {
            'code': 1000,
            'scheduledlist': relationlist.data,
            'total':relations.count()
        }

        return Response(ret)

class getValidRoom(APIView):
    def get(self, request, *args, **kwargs):
        form = request.GET.get('form')
        form = json.loads(form)
        print(form)
        building = form['building']
        times = form['time']
        courses = [int(n) for n in form['course']]

        course = models.Course.objects.filter(id = courses[1]).first()
        print(course.function_id)

        #遍历获取选中时间占用的教室，并将每次获得的列表存入occupiedroom列表中
        occupiedroom = []
        for i in times:
            timelist = models.ClassTime.objects.filter(id = i).first()
            mainrelation = timelist.mainrelation_set.values_list('classroom_id', flat=True)
            occupiedroom.extend(list(mainrelation))
        print(occupiedroom)

        #最后根据条件，在筛选出来的数据中,再将“同一时间被占用教室列表”（occupiedroom)中的数据排除，并进行最终排序
        classrooms = models.ClassRoom.objects.filter(Q(building_id = building) 
            & Q(function_id = course.function_id) & Q(capacity__gt = int(form['capacity'])-1)).exclude(id__in = occupiedroom).order_by('id')
        print(classrooms)
        roomlist = ser.ClassRoomlistSerializers(classrooms, many=True)

        ret = {
            'code': 1000,
            'roomlist': roomlist.data
        }

        return Response(ret)


class getColCou(APIView):
    def get(self, request, *args, **kwargs):
        ret_type = request.GET.get('type')
        if ret_type == "college":
            colleges = models.CollegeInfo.objects.all().order_by('college_id')

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

        elif ret_type == "course":
            courses = models.Course.objects.filter(college_id = request.GET.get('college_id'))
            courselist = []
            for i in courses:
                data={
                    'value': str(i.id),
                    'label': i.name,
                }
                courselist.append(data)

            ret={
                'code':1000,
                'data': courselist
            }
            return Response(ret)

        else:
            courses = models.Course.objects.filter(id = request.GET.get('course_id')).first()
            teachers = courses.teacherinfo_set.all()
            print(teachers)
            teacherlist = []
            for i in teachers:
                data={
                    'value': str(i.id),
                    'label': i.name,
                    'leaf': 'level >= 2' #设置中止叶节点
                }
                teacherlist.append(data)

            ret={
                'code':1000,
                'data': teacherlist
            }
            return Response(ret)


class getSchBuilding(APIView):
    def get(self, request, *args, **kwargs):
        buildings = models.Building.objects.all().order_by('id')
        times = models.ClassTime.objects.all().order_by('id')

        buildinglist = ser.BuildinglistSerializers(buildings, many=True)
        timelist = ser.ClassTimelistSerializers(times, many=True)


        ret = {
            'code': 1000,
            'buildinglist': buildinglist.data,
            'timelist': timelist.data
        }

        return Response(ret)


class addSchedule(APIView):
    def post(self, request, *args, **kwargs):
        form = request.data.get('form')
        form = json.loads(form)
        print(form)
        building = form['building']
        times = form['time']
        courses = [int(n) for n in form['course']]

        for i in times:
            timelist = models.ClassTime.objects.filter(id = i).first()
            mainrelation = timelist.mainrelation_set.filter(teacher_id = courses[2]).first()
            if mainrelation:
                return Response({'code': 1001})

        new_schedule = models.MainRelation.objects.create(
            classroom_id=form['rooms'],
            course_id = courses[1],
            teacher_id = courses[2],
            stuquantity = form['capacity'],
        )
        new_schedule.classtime.set(form['time'])

        return Response({'code': 1000})