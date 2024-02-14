import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.template.loader import get_template,render_to_string
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.db import IntegrityError
from django.contrib import messages
import json
import csv
import random
import pandas as pd
from Student.models import *
from Hall_Admin.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
import codecs
from openpyxl import load_workbook

def logIn(request):
    if 'login' in request.POST:
        if request.POST.get('type')=='1':
            user=Provost.objects.get(email=request.POST.get('email'))
            login(request,authenticate(request,username=user.username,password=user.password))
            redirectUrl="/provost"
            return redirect(redirectUrl)
        if request.POST.get('type')=='1':
            user=HallAdmin.objects.get(email=request.POST.get('email'))
            login(request,authenticate(request,username=user.username,password=user.password))
            redirectUrl="/hallAdmin/"
            return redirect(redirectUrl)
        if request.POST.get('type')=='1':
            login(request,authenticate(request,username=user.username,password=user.password))
            redirectUrl="/aadmin/"+str(user.shopId)
            return redirect(redirectUrl)
        if request.POST.get('type')=='1':
            login(request,authenticate(request,username=user.username,password=user.password))
            redirectUrl="/aadmin/"+str(user.shopId)
            return redirect(redirectUrl)
    return render(request,'logIn.html')
def register(request):
    if 'register' in request.POST:
        if request.POST.get('type')=='1':
            newUser=Provost.objects.get(email=request.POST.get('email'))
            newUser.username=request.POST.get('username')
            newUser.password=request.POST.get('password')
            newUser.save()
            user=User.objects.create_user(username=newUser.username,email=newUser.email,password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type')=='2':
            newUser=HallAdmin.objects.get(email=request.POST.get('email'))
            newUser.username=request.POST.get('username')
            newUser.password=request.POST.get('password')
            newUser.save()
            user=User.objects.create_user(username=newUser.username,email=newUser.email,password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type')=='3':
            newUser=Student.objects.get(email=request.POST.get('email'))
            newUser.username=request.POST.get('username')
            newUser.password=request.POST.get('password')
            newUser.save()
            user=User.objects.create_user(username=newUser.username,email=newUser.email,password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type')=='4':
            newUser=Provost.objects.get(email=request.POST.get('email'))
            newUser.username=request.POST.get('username')
            newUser.password=request.POST.get('password')
            newUser.save()
            user=User.objects.create_user(username=newUser.username,email=newUser.email,password=newUser.password)
            return redirect('/authentication')   
    return render(request,'register.html')