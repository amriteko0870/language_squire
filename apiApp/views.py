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

#----------------------------extra---------------------------------------------------

@api_view(['POST'])
def userSignUp(request,format=None):
    # --------------------------- Get field from frontend -------------------------------------
    try:
        first_name = request.data['first_name']
    except:
        return Response({'status':False,
                         'error':'first name is not recieved'})

    try:
        last_name = request.data['last_name']
    except:
        return Response({'status':False,
                         'error':'last name is not recieved'})

    try:
        email = request.data['email']
    except:
        return Response({'status':False,
                         'error':'email is not recieved'})
    
    try:
        phone_code = request.data['phone_code']
    except:
        return Response({'status':False,
                         'error':'phone code is not recieved'})

    try:
        phone_no = request.data['phone_no']
    except:
        return Response({'status':False,
                         'error':'phone no is not recieved'})

    try:
        age = request.data['age']
    except:
        return Response({'status':False,
                         'error':'age is not recieved'})

    try:
        gender = request.data['gender']
    except:
        return Response({'status':False,
                         'error':'gender is not recieved'})

    try:
        password = request.data['password']
    except:
        return Response({'status':False,
                         'error':'password is not recieved'})

    # ------------------- make token and encrypt password --------------------------------------
    enc_password = make_password(password)
    token = make_password(email+password)

    #------------------------- Adding into database --------------------------------------------
    data = user_login(
                        first_name = first_name,
                        last_name = last_name,
                        email = email,
                        phone_code = phone_code,
                        phone_no = phone_no,
                        age = age,
                        gender = gender,
                        password = enc_password,
                        user_type = 'u',
                        active_course = 'n/a',
                        payment_status = False,
                        token = token
                    )
    data.save()
    
    return Response({
                        'status':True,
                        'message':'sign up successfull',
                    })

        


@api_view(['POST'])
def userSignIn(request,format=None):
    try:
        email = request.data['email']
    except:
        return Response({'status':False,
                         'error':'email is not recieved'})
    try:
        password = request.data['password']
    except:
        return Response({'status':False,
                         'error':'password is not recieved'})
    
    try:
        user = user_login.objects.get(email = email)
    except:
        return Response({'status':False,
                     'message':'Invalid credentials'})

    if check_password(password,user.password):
        return Response({'status':True,
                        'message':'user sign in successfull',
                        'first_name':user.first_name,
                        'last_name':user.last_name,
                        'email':user.email,
                        'token':user.token,
                        'user_type':user.user_type})
    else:
        return Response({'status':False,
                     'message':'Invalid credentials'})


@api_view(['POST'])
def userProfile(request,format=None):
    if request.method == 'POST':
        try:
            token = request.data['token']   
            user = user_login.objects.get(token = token)
        except:
            res = {
                    'status': False,
                    'message': 'something went wrong',
                  }
            return Response(res)
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        phone_code = user.phone_code
        phone_no = user.phone_no
        age = user.age
        gender = user.gender
        
        res = {
                'status':True,
                'message': 'profile generated successfully',
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'phone_code':phone_code,
                'phone_no':phone_no,
                'age':age,
                'gender':gender,
              }
        return Response(res)


@api_view(['POST'])
def userCurriculum(request,format=None):
    if request.method == 'POST':
        try:
            token = request.data['token']   
            user = user_login.objects.get(token = token)
        except:
            res = {
                    'status': False,
                    'message': 'something went wrong',
                    }
            return Response(res)
        
        pageData = []
        curriculum_list = curriculum.objects.values()
        for i in curriculum_list:
            single_section = {}
            single_section['id'] = i['id']
            single_section['sectionName'] = str(i['name']).capitalize()
            single_section['path'] = 'media/img/' + i['name']
            single_section['image_array'] = os.listdir('media/img/' + i['name'])
            pageData.append(single_section)
        res = {
                'status': True,
                'message':'curriculum generated successfully',
                'pageData':pageData
              }
        return Response(res)
    