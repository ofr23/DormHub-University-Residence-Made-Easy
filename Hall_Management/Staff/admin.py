from django.contrib import admin
from .models import Staff, Visitor  # Import the Staff and Visitor models

# Register the Staff and Visitor models in the Django admin site
admin.site.register(Staff)
admin.site.register(Visitor)
