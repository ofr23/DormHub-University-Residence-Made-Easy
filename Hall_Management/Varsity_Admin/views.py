import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
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
def varsityAdmin(request):
    if 'session' in request.POST:
        newSession=Session(
            session=request.POST.get('sess'),
            csvFile=request.FILES.get('csv')
        )
        newSession.save()
        return redirect('/varsityAdmin')
    provostList=Provost.objects.filter()
    adminList=HallAdmin.objects.filter()
    if 'hall' in request.POST:
        provost=Provost.objects.get(provostId=int(request.POST.get('provost')))
        admin=HallAdmin.objects.get(adminId=int(request.POST.get('admin')))
        newHall=Hall(
            hallId=int(request.POST.get('id')),
            name=request.POST.get('name'),
            provost=provost,
            hallAdmin=admin
        )
        newHall.save()
        return redirect('/varsityAdmin')
    cont={
        'provostList':provostList,
        'adminList':adminList
    }
    return render(request,'varsityAdmin.html',cont)
def allSession(request):
    return render(request,'allSession.html')

