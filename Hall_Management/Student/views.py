from django.shortcuts import render, redirect
from .models import *
import datetime

def student(request):
    student=Student.objects.get(email=request.user.email)
    hall=Hall.objects.get(hallId=student.hall.hallId)
    room=student.room.roomId
    requests=RepairRequest.objects.filter(student=student,hall=hall)
    if 'change' in request.POST:
        createRequest=SwapRequest(
            hall=hall,
            student=student,
            reason=request.POST.get('reason'),
        )
        createRequest.save()
        createRequest.noOfRequests+=1
        createRequest.save()
        return redirect('/student')
    if 'repair' in request.POST:
        requestId=len(RepairRequest.objects.filter())+1
        createRequest=RepairRequest(
            hall=hall,
            student=student,
            reason=request.POST.get('reason'),
            requestType=int(request.POST.get('type')),
            requestId=requestId
        )
        createRequest.save()
        return redirect('/student')
    context={
        'room':room,
        'requests':requests
    }
    return render(request,'student.html',context)