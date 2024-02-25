import datetime

from Student.models import *
from django.shortcuts import render, redirect

from .models import Staff, Visitor


def staff(request):
    """
    View function for rendering the staff page.

    If 'visitor' is in the POST request, redirects to 'visitorToday' page.
    Otherwise, renders the 'staff.html' template.

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    if 'visitor' in request.POST:
        return redirect('/staff/visitorToday')
    if 'requests' in request.POST:
        return redirect('/staff/repairRequests')
    return render(request, 'staff.html')


def visitorToday(request):
    """
    View function for rendering the visitorToday page.

    Retrieves today's date and the staff member.
    Retrieves the list of visitors for today in the staff member's hall.
    If 'add' is in the POST request, adds a new visitor record.
    If 'departure' is in the POST request, updates the departure time of the visitor.
    Renders the 'visitorToday.html' template with the context.

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    today = datetime.datetime.now().date()
    staff = Staff.objects.get(email=request.user.email)
    visitorList = Visitor.objects.filter(date=today, hall=staff.hall)

    if 'add' in request.POST:
        newId = len(Visitor.objects.filter()) + 1
        newRecord = Visitor(
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
        record = Visitor.objects.get(
            visitorId=int(request.POST.get('departure')),
            hall=staff.hall
        )
        record.departure = datetime.datetime.now().time()
        record.save()
        return redirect('/staff/visitorToday/')

    context = {
        'hall': staff.hall,
        'today': today,
        'visitorList': visitorList
    }
    return render(request, 'visitorToday.html', context)


def repairRequests(request):
    """
    View function for rendering the repairRequests page.

    Retrieves staff member and repair requests for the staff member's hall.
    If 'schedule' is in the POST request, updates the date of the repair request.
    Renders the 'repairRequests.html' template with the context.

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    staff = Staff.objects.get(email=request.user.email)
    hall = Hall.objects.get(hallId=staff.hall.hallId)
    requests = RepairRequest.objects.filter(hall=hall)

    if 'schedule' in request.POST:
        req = RepairRequest.objects.get(requestId=int(request.POST.get('schedule')))
        req.date = request.POST.get('date')
        req.save()
        return redirect('/staff/repairRequests')

    context = {
        'requests': requests
    }
    return render(request, 'repairRequests.html', context)
