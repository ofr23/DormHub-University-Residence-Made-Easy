from Hall_Admin.models import *
from Provost.models import *
from Staff.models import *
from Student.models import *
from Varsity_Admin.models import *
from django.shortcuts import render, redirect


def varsityAdmin(request):
    """
    View function for the varsity admin page.

    Handles addition of new sessions, halls, and associated staff.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the varsity admin page content.
    """

    # Check if a new session is being added
    if 'session' in request.POST:
        # Create a new session object with data from the form
        newSession = Session(
            session=request.POST.get('sess'),
            csvFile=request.FILES.get('csv')
        )
        # Save the new session object to the database
        newSession.save()
        # Redirect to the varsityAdmin page
        return redirect('/varsityAdmin')

    # Get lists of provosts, hall admins, and staff for rendering in the template
    provostList = Provost.objects.all()
    adminList = HallAdmin.objects.all()
    staffList = Staff.objects.all()

    # Check if a new hall is being added
    if 'hall' in request.POST:
        # Get the selected provost and hall admin from the form data
        provost = Provost.objects.get(email=request.POST.get('provost'))
        admin = HallAdmin.objects.get(email=request.POST.get('admin'))
        # Create a new hall object with data from the form
        newHall = Hall(
            hallId=int(request.POST.get('id')),
            name=request.POST.get('name'),
            provost=provost,
            hallAdmin=admin
        )
        # Save the new hall object to the database
        newHall.save()
        # Redirect to the varsityAdmin page
        return redirect('/varsityAdmin')

    # Prepare context data to pass to the template
    context = {
        'provostList': provostList,
        'adminList': adminList,
        'staffList': staffList
    }

    # Render the varsityAdmin template with the context data
    return render(request, 'varsityAdmin.html', context)