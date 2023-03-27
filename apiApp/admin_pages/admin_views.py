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
    pageData['total_students'] = pageData['id'].apply( lambda x : user_login.objects.filter(batch_id = x).values().count())
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

@api_view(['POST'])
def adminAssestmentBatchList(request):
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
    res = {}
    batch_obj = batch_creation.objects.values()
    batch_obj = pd.DataFrame(batch_obj)
    batch_obj['batch_id'] = batch_obj['id']
    batch_obj['batch_name'] = batch_obj['id'].apply(lambda x : 'Batch '+ str(x))
    batch_obj['total_assignemnts'] = batch_obj['assignment_array'].apply(lambda x : len(eval(x)))
    batch_obj['total_students'] = batch_obj['id'].apply( lambda x : user_login.objects.filter(batch_id = x).values().count())
    batch_obj = batch_obj[['batch_id','batch_name','total_assignemnts','total_students']]
    batch_obj = batch_obj.to_dict(orient='records')
    res['assestment_batch'] = batch_obj
    return Response(res)

@api_view(['POST'])
def assigmentModalView(request):
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
    res = {}
    allAssignmentList = set_of_test.objects.annotate(assignment_name = F('name'),assignment_id = F('id')).values('assignment_name','assignment_id')
    res['allAssignmentList'] = allAssignmentList
    batch_assignments = eval(batch_creation.objects.filter(id = batch_id).values().last()['assignment_array'])
    currentAssignmentList = set_of_test.objects.filter(id__in = batch_assignments).annotate(assignment_name = F('name'),assignment_id = F('id'))\
                                                                                  .values('assignment_name','assignment_id')
    res['currentAssignmentList'] = currentAssignmentList
    return Response(res)

@api_view(['POST'])
def addAssignmentToBatch(request):
    data = request.data
    try:
        token = data['token']
        user_login.objects.get(token = token)
    except:
        res = {
                'status':False,
                'message': 'Authentication failed'
              }
        return Response(res)
    batch_id = data['batch_id']
    assignment_id = data['assignment_id']
    try:
        set_of_test.objects.get(id = assignment_id)
    except:
        res = {
                'status':False,
                'message': 'Something went wrong'
              }
        return Response(res)
    batch_assignments = eval(batch_creation.objects.filter(id = batch_id).values().last()['assignment_array'])
    if assignment_id in batch_assignments:
        res = {
                'status':False,
                'message': 'Assignment already in batch'
              }
        return Response(res)
    else:
        batch_assignments.append(str(assignment_id))
        batch_creation.objects.filter(id = batch_id).update(assignment_array = str(batch_assignments))
        student_list = user_login.objects.filter(batch_id = batch_id).values_list('id',flat=True)
        for i in student_list:
            test_obj = test_assigned(
                                    user_id = str(i),
                                    set_of_test_id = str(assignment_id),
                                )
            test_obj.save()
        res = {
                'status':True,
                'message':'Assigmnet assigned to batch successfully'
              }
        return Response(res)
