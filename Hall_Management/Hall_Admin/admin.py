from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(HallAdmin)
admin.site.register(Hall)