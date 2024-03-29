from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers
from api import models, page
from api import serializers4stu as ser
import json


class initStudentInfo(APIView):
    def get(self , request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        student = models.StudentInfo.objects.filter(stu_id = stu_id).first()

        studentinfo = ser.StudentInfoSerializers(student, many=False)
        ret={
            'code': 1000,
            'form': studentinfo.data
        }
        return Response(ret)


class getCourseList(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        major = models.StudentInfo.objects.filter(stu_id = stu_id).first().Major.id
        courses = models.MajorInfo.objects.filter(id=major).first().course.all()

        courseinfo = ser.CourseinfoSerializers(courses, many=True)

        ret = {
            'code': 1000,
            'courselist': courseinfo.data
        }

        return Response(ret)

class initCourseList(APIView):
    def get(self, request, *args, **kwargs):
        mod = request.GET.get('mod')
        student = models.StudentInfo.objects.filter(stu_id = request.GET.get('stu_id')).first()
        #找到已经被选择的课程，排除,返回的QuerySet需要转换成列表
        #haveselecteds = student.mainrelation_set.values_list('course_id', flat=True)
        haveselecteds = models.Student2Relation.objects.filter(student=student).values_list('relation__course_id', flat=True)
        
        if mod == "1":
            major = student.Major
            courses = major.course.filter(betyear = student.grade.id).exclude(id__in = list(haveselecteds)).order_by('id')
        elif mod == "2":
            courses = models.Course.objects.all().exclude(id__in = list(haveselecteds)).order_by('id')
        else:
            courses = models.Course.objects.filter(college=request.GET.get('college')).exclude(id__in = list(haveselecteds)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(courses, request, self)
        courselist = ser.CourseinfoSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'form': courselist.data,
            'total': courses.count()
        }
        return Response(ret)


class getRelations(APIView):
    def get(self, request, *args, **kwargs):
        relations = models.MainRelation.objects.filter(course = request.GET.get('id')).order_by('id')
        relationlist = ser.RelationlistSerializers(relations, many = True)

        rel_id = []
        for i in relations:
            rel_id.append(i.id)

        ret = {
            'code': 1000,
            'tableData': relationlist.data,
            'rel_id': rel_id
        }

        return Response(ret)


class updateChoice(APIView):
    def post(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.data.get('stu_id')).first()
        relation = models.MainRelation.objects.filter(id = request.data.get('id')).first()
        models.Student2Relation.objects.create(relation=relation,student=student)
        return Response({'code': 1000})


class getScheduled(APIView):
    def get(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.GET.get('stu_id')).first()
        #relations = student.mainrelation_set.all().order_by('id')
        relations = models.Student2Relation.objects.filter(student=student).values_list('relation', flat=True)

        relations = models.MainRelation.objects.filter(id__in = list(relations)).order_by('id')

        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(relations, request, self)
        relationlist = ser.RelationlistSerializers(page_role, many = True)

        ret = {
            'code': 1000,
            'scheduledlist': relationlist.data,
            'total':relations.count()
        }

        return Response(ret)


class deleteScheduled(APIView):
    def post(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.data.get('stu_id')).first()
        models.Student2Relation.objects.filter(relation = request.data.get('id'), student=student).first().delete()

        ret = {
            'code': 1000,
        }

        return Response(ret)

class getCollegelist(APIView):
    def get(self, request, *args, **kwargs):
        colleges = models.CollegeInfo4tc.objects.all().order_by('id')
        collegelist = ser.College4tclistSerializers(colleges, many=True)

        ret = {
            'code': 1000,
            'colleges': collegelist.data,
        }

        return Response(ret)


class initCourseInfo(APIView):
    def get(self,request,*args,**kwargs):
        cou_id = request.GET.get('cou_id')
        course = models.Course.objects.filter(cou_id = cou_id).first()
        courselist = ser.Courseinfo4plandrawSerializers(course, many=False)

        ret = {
            'code': 1000,
            'form': courselist.data,
        }
        return Response(ret)



class getCourses(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        major = models.StudentInfo.objects.filter(stu_id = stu_id).first().Major.id
        functions = models.Function.objects.all().order_by('id')
        functionlist = ser.FunctionlistSerializers(functions, many = True)

        courses = models.MajorInfo.objects.filter(id=major).first().course.all().order_by('betyear','id')
        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(courses, request, self)
        courseinfo = ser.Courseinfo4planSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'courselist': courseinfo.data,
            'functions':functionlist.data,
            'total': courses.count()
        }

        return Response(ret)


class filterCourses(APIView):
    def get(self, request, *args, **kwargs):
        stu_id = request.GET.get('stu_id')
        major = models.StudentInfo.objects.filter(stu_id = stu_id).first().Major.id

        courses = models.MajorInfo.objects.filter(id=major).first().course.all().order_by('betyear','id')
        pages = page.MyLimitOffsetPagination()
        page_role = pages.paginate_queryset(courses, request, self)

        courseinfo = ser.Courseinfo4planSerializers(page_role, many=True)

        ret = {
            'code': 1000,
            'courselist': courseinfo.data,
            'total': courses.count()
        }

        return Response(ret)


class getTestlist(APIView):
    def get(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.GET.get('stu_id')).first().id
        if request.GET.get('type') == "1" :
            print('aaa')
            relations = models.Student2Relation.objects.filter(student = student).values_list('relation', flat=True)
        
            relations = models.MainRelation.objects.filter(id__in = relations).order_by('id')
            relationlist = ser.Relationlist4testSerializers(relations, many=True)
        
            print(relationlist.data)
            ret = {
                'code': 1000,
                'relations': relationlist.data
            }
            return Response(ret)
        else:
            relations = models.Student2Relation.objects.filter(student = student).order_by('id')
            relationlist = ser.GradeSerializers(relations, many=True)
            ret = {
                'code': 1000,
                'relations': relationlist.data
            }
            return Response(ret)


class applyChangepasswd(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data.get('stu_id'))
        student = models.StudentInfo.objects.filter(stu_id = request.data.get('stu_id')).first()
        admin = models.AdminInfo.objects.filter(id = 1).first()
        models.Message.objects.create(
            fromwho = "student",
            towho = "admin",
            student = student,
            admin = admin,
            messagetype = models.MessageType.objects.get(id = 1),
            title = str(student.stu_id) + " " + student.name + "申请修改密码",
        )

        return Response({'code': 1000})

class getSendlist(APIView):
    def get(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.GET.get('stu_id')).first()
        messages = models.Message.objects.filter(Q(fromwho="student") & Q(student = student)).order_by('id')

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


class postMessage(APIView):
    def post(self, request, *args, **kwargs):
        form = json.loads(request.data.get('form'))
        student = models.StudentInfo.objects.filter(stu_id = request.data.get('stu_id')).first()
        print(student)

        if form['option'] == "1":
            teacher = models.TeacherInfo.objects.filter(tea_id = form['towho']).first()
            if teacher:
                models.Message.objects.create(
                    fromwho = "student",
                    towho = "teacher",
                    student = student,
                    teacher = teacher,
                    messagetype = models.MessageType.objects.get(id = 3),
                    title = form['title'],
                    content = form['content'],
                )
                return Response({'code': 1000})
            else:
                return Response({'code': 1001, 'error': "找不到该教师，请核对教工号"})
        else :
            admin = models.AdminInfo.objects.filter(id = 1).first()
            models.Message.objects.create(
                fromwho = "student",
                towho = "admin",
                student = student,
                admin = admin,
                messagetype = models.MessageType.objects.get(id = 3),
                title = form['title'],
                content = form['content'],
            )
            return Response({'code': 1000})


class getSavelist(APIView):
    def get(self, request, *args, **kwargs):
        student = models.StudentInfo.objects.filter(stu_id = request.GET.get('stu_id')).first()
        print(student)
        messages = models.Message.objects.filter(Q(towho="student") & Q(student = student)).order_by('id')
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