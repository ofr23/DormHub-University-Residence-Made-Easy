from django.contrib import admin
from .models import *

# Register the Student and Session models in the Django admin site
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(SwapRequest)
admin.site.register(RepairRequest)