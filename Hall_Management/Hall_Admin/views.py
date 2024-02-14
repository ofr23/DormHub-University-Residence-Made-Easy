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
def hallAdmin(request):
    admin=HallAdmin.objects.get(email=request.user.email)
    hall=Hall.objects.get(hallAdmin=admin)
    changeStructure=0
    rooms=Room.objects.filter(hall=hall)
    if rooms:
        changeStructure=1
    colors={
        1:'crimson',
        2:'indigo',
        3:'orange',
        4:'cornflowerblue',
        5:'coral',
        6:'seagreen',
        7:'yellow',
    }
    if 'change' in request.POST:
        numberOfFloors=int(request.POST.get('floor'))+1
        for x in range(1,numberOfFloors):
            ca=x*100 
            da=ca+30+1
            for i in range(ca,da):
                newRoom=Room(
                    hall=hall,
                    roomId=i,
                    capacity=int(request.POST.get('capacity')),
                    color=colors[int(i/100)]
                )
                newRoom.save()
        return redirect('/hallAdmin')
    queryDict={}
    for o in range(1,8):
        queryDict[o]=[]
    rooms=Room.objects.filter(hall=hall)
    for room in rooms:
        queryDict[int(room.roomId/100)].append(room)
    context={
        'hall':hall,
        'changeStructure':changeStructure,
        'queryDict':queryDict
    }
    return render(request,'hallAdmin.html',context)
