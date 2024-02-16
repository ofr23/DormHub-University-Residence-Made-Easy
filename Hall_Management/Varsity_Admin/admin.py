from django.contrib import admin
from .models import Hall, VarsityAdmin, Room

# Register the Hall, VarsityAdmin, and Room models in the Django admin site
admin.site.register(Hall)
admin.site.register(VarsityAdmin)
admin.site.register(Room)
