from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Hall)
admin.site.register(VarsityAdmin)
admin.site.register(Room)