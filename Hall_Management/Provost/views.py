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
from openpyxl import load_workbook
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
import codecs
def provost(request):
    return render(request,'provost.html')
def addStudent(request):
    sessions=Session.objects.filter()
    provost=Provost.objects.get(email=request.user.email)
    hall=Hall.objects.get(provost=provost)
    if 'add' in request.POST:
        csv=Session.objects.get(session=request.POST.get('session')).csvFile
        wb = load_workbook(csv)
        ws = wb.active
        for row in ws.iter_rows(min_row=2, values_only=True):
            print(row)
    queryDict={}
    for o in sessions:
        session=Session.objects.get(session=o.session)
        ifPresent=Student.objects.filter(session=session,hall=hall)
        if ifPresent:
            queryDict[o]=1
        else:
            queryDict[o]=0
    context={
        'queryDict':queryDict
    }
    return render(request,'addStudent.html',context)