import numpy as np
import pandas as pd
import time
from datetime import datetime as dt
import datetime
import re
from operator import itemgetter 
import os
import random


#-------------------------Django Modules---------------------------------------------
from django.http import Http404, HttpResponse, JsonResponse,FileResponse
from django.shortcuts import render
from django.db.models import Avg,Count,Case, When, IntegerField,Sum,FloatField,CharField
from django.db.models import F,Func,Q
from django.db.models import Value as V
from django.db.models.functions import Concat,Cast,Substr
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Min, Max
from django.db.models import Subquery
#----------------------------restAPI--------------------------------------------------
from rest_framework.decorators import parser_classes,api_view
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status

#----------------------------models---------------------------------------------------
from apiApp.models import user_login
from apiApp.models import curriculum
from apiApp.models import set_of_test
from apiApp.models import test_assigned
from apiApp.models import batch_creation

#----------------------------extra---------------------------------------------------

@api_view(['POST'])
def adminBatchList(request):
    data = request.data
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    pageData = batch_creation.objects.values()
    pageData = pd.DataFrame(pageData)
    pageData['batch_id'] = pageData['id']
    pageData['batch_name'] = pageData['id'].apply(lambda x : 'Batch '+ str(x))
    pageData['created_date'] = pageData['date_time'].apply(lambda x : str(x)[:10])
    pageData['created_time'] = pageData['date_time'].apply(lambda x : str(x)[11:19])
    pageData['total_students'] = pageData['student_count']
    pageData = pageData[['batch_id','batch_name','created_date','created_time','total_students']]
    pageData = pageData.to_dict(orient='records')
    return Response(pageData)

@api_view(['POST'])
def adminCreateBatch(request):
    data = request.data
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    batch_creation.objects.create()
    res = {
            'status':True,
            'message':'Batch created successfully'
          }
    return Response(res)

@api_view(['POST'])
def adminDeleteBatch(request):
    data = request.data
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    batch_id = data['batch_id']
    user_login.objects.filter(batch_id = batch_id).update(batch_id = 'u')
    batch_creation.objects.filter(id = batch_id).delete()
    res = {
            'status':True,
            'message':'Batch deleted successfully'
          }
    return Response(res)

@api_view(['POST'])
def adminStudentList(request):
    data = request.data
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    pageData = user_login.objects.filter(user_type = 'u').values()
    pageData = pd.DataFrame(pageData)
    pageData['id'] = pageData['id'] 
    pageData['enrolled_date'] = pageData['date_time'].apply(lambda x : str(x)[:10])
    pageData['enrolled_time'] = pageData['date_time'].apply(lambda x : str(x)[11:19])
    pageData['f_name'] = pageData['first_name']
    pageData['l_name'] = pageData['last_name'] 
    pageData['email'] = pageData['email']
    pageData['batch'] = pageData['batch_id'].apply(lambda x : 'No Batch' if x == 'u' else 'Batch '+str(x) )
    pageData['batch_id'] = pageData['batch_id'].apply(lambda x : 'No Batch' if x == 'u' else str(x) )
    pageData = pageData[['id','enrolled_date','enrolled_time','f_name','l_name','email','batch','batch_id']]
    pageData = pageData.to_dict(orient='records')
    return Response(pageData)

@api_view(['POST'])
def adminUpdateBatch(request):
    data = request.data
    print(data)
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    student_id = data['student_id']
    batch_id = data['batch_id']

    user_login.objects.filter(id = student_id).update(batch_id = batch_id)
    res = {
                'status':True,
                'message': 'Studentt batch updated'
              }
    return Response(res)