"""
Django Admin Registration

This module provides registration of models in the Django admin site.
"""

from django.contrib import admin
from .models import Staff, Visitor


class StaffAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Staff model in the Django admin site.

    Inherits from admin.ModelAdmin to provide customization options for the Staff model.
    """
    pass


class VisitorAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Visitor model in the Django admin site.

    Inherits from admin.ModelAdmin to provide customization options for the Visitor model.
    """
    pass


# Register the Staff and Visitor models in the Django admin site
admin.site.register(Staff, StaffAdmin)
admin.site.register(Visitor, VisitorAdmin)
