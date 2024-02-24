# Import the admin module from django.contrib
from django.contrib import admin

# Import the HallAdmin model from the current package (assuming it's in the models.py file)
from .models import HallAdmin

# Register the HallAdmin model with the Django admin site
admin.site.register(HallAdmin)
