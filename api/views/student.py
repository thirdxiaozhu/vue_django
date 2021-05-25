from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from api import models

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