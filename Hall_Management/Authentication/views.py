from Hall_Admin.models import *
from Staff.models import *
from Student.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from Provost.models import *

def logIn(request):
    """
    Handles the login functionality.
    """
    if 'login' in request.POST:
        if request.POST.get('type') == '1':
            user = Provost.objects.get(email=request.POST.get('email'))
            login(request, authenticate(request, username=user.username, password=user.password))
            redirectUrl = "/provost/addStudent"
            return redirect(redirectUrl)
        if request.POST.get('type') == '2':
            user = HallAdmin.objects.get(email=request.POST.get('email'))
            login(request, authenticate(request, username=user.username, password=user.password))
            redirectUrl = "/hallAdmin/"
            return redirect(redirectUrl)
        if request.POST.get('type') == '3':
            user = Student.objects.get(email=request.POST.get('email'))
            login(request, authenticate(request, username=user.username, password=user.password))
            redirectUrl = "/student" 
            return redirect(redirectUrl)
        if request.POST.get('type') == '4':
            user = Staff.objects.get(email=request.POST.get('email'))
            login(request, authenticate(request, username=user.username, password=user.password))
            redirectUrl = "/staff"
            return redirect(redirectUrl)
    return render(request, 'logIn.html')


def register(request):
    """
    Handles the registration functionality.
    """
    if 'register' in request.POST:
        if request.POST.get('type') == '1':
            newUser = Provost(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            newUser.save()
            user = User.objects.create_user(username=newUser.username, email=newUser.email, password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type') == '2':
            newUser = HallAdmin(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            newUser.save()
            user = User.objects.create_user(username=newUser.username, email=newUser.email, password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type') == '3':
            newUser = Student.objects.get(email=request.POST.get('email'))
            newUser.username=request.POST.get('username')
            newUser.password=request.POST.get('password')
            newUser.save()
            user = User.objects.create_user(username=newUser.username, email=newUser.email, password=newUser.password)
            return redirect('/authentication')
        if request.POST.get('type') == '4':
            newUser = Staff(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            newUser.save()
            user = User.objects.create_user(username=newUser.username, email=newUser.email, password=newUser.password)
            return redirect('/authentication')
    return render(request, 'register.html')
