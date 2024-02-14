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
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
import codecs
def hallAdmin(request):
    # if 'session' in request.POST:
       
    #     newSession=Session(
    #         session=request.POST.get('sess'),
    #         csvFile=request.FILES.get('csv')
    #     )
    #     newSession.save()
    #     with codecs.open(newSession.csvFile, 'r', encoding='ISO-8859-1') as f:
    #         df = pd.read_csv(f)
    #         print(df.values)
    #     return redirect('/hallAdmin')
    return render(request,'hallAdmin.html')