from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from api import models
import uuid

class login(APIView):
    def post(self,request,*args,**kwargs):
        usertype = request.GET.get('radio')
        userid = request.GET.get('userid')
        password  =request.GET.get('password')
        print(userid)
        if usertype == "1":
            user = models.StudentInfo.objects.filter(stu_id = userid, password = password).first()
            if user:
                uid = str(uuid.uuid4())
                token = models.Usertoken.objects.update_or_create(userid = user.id, defaults={'token':uid})
                user.token_id = token[0].id #token返回的是元组，该元组第一个才是查到的字段
                user.save()
                print(user.token)
                ret = {
                    'code': 1000,
                    'name': user.name,
                    'token': uid
                }
            else:
                ret = {
                    'code': 1001,
                    'error':"用户名和密码错误"
                }
            return Response(ret)
        if usertype == "2":
            user = models.TeacherInfo.objects.filter(tea_id = userid, password = password).first()
            if user:
                uid = str(uuid.uuid4())
                token = models.Usertoken.objects.update_or_create(userid = user.id, defaults={'token':uid})
                user.token_id = token[0].id #token返回的是元组，该元组第一个才是查到的字段
                user.save()
                print(user.token)
                ret = {
                    'code': 1000,
                    'name': user.name,
                    'token': uid
                }
            else:
                ret = {
                    'code': 1001,
                    'error':"用户名和密码错误"
                }
            return Response(ret)
        if usertype == "3":
            user = models.AdminInfo.objects.filter(adm_id = userid, password = password).first()
            if user:
                uid = str(uuid.uuid4())
                token = models.Usertoken.objects.update_or_create(userid = user.id, defaults={'token':uid})
                user.token_id = token[0].id #token返回的是元组，该元组第一个才是查到的字段
                user.save()
                print(user.token)
                ret = {
                    'code': 1000,
                    'name': "管理员",
                    'token': uid
                }
            else:
                ret = {
                    'code': 1001,
                    'error':"用户名和密码错误"
                }
            return Response(ret)
