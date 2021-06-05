from rest_framework import renderers
from rest_framework.versioning import QueryParameterVersioning
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning

class CourseView(APIView):
    versioning_class =  URLPathVersioning
    def get(self,request,*args,**kwargs):
        ret = {
            'code': 1000,
            'data':[
                {'id':1 , 'title':'abc'},
                {'id':2 , 'title':'def'},
                {'id':3 , 'title':'hgi'},
            ]
        }
        return Response(ret)