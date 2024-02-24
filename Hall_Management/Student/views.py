from django.shortcuts import render, redirect
from .models import *
import datetime

def student(request):
    return render(request,'student.html')