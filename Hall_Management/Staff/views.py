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
from .models import *
from Student.models import *
from Hall_Admin.models import *
from openpyxl import load_workbook
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
import codecs

def staff(request):
    if 'visitor' in request.POST:
        return redirect('/staff/visitorToday')
    return render(request,'staff.html')
def visitorToday(request):
    today=datetime.datetime.now().date()
    staff=Staff.objects.get(email=request.user.email)
    visitorList=Visitor.objects.filter(date=today,hall=staff.hall)
    if 'add' in request.POST:
        newId=len(Visitor.objects.filter())+1
        newRecord=Visitor(
            date=today,
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            visitorId=newId,
            visit=request.POST.get('visit'),
            arrival=datetime.datetime.now().time(),
            hall=staff.hall
        )
        newRecord.save()
        return redirect('/staff/visitorToday/')
    if 'departure' in request.POST:
        record=Visitor.objects.get(
            visitorId=int(request.POST.get('departure')),
            hall=staff.hall
        )
        record.departure=datetime.datetime.now().time()
        record.save()
        return redirect('/staff/visitorToday/')
    cont={
        'hall':staff.hall,
        'today':today,
        'visitorList':visitorList
    }
    return render(request,'visitorToday.html',cont)