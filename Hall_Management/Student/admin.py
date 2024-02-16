from django.contrib import admin
from .models import Student, Session

# Register the Student and Session models in the Django admin site
admin.site.register(Student)
admin.site.register(Session)
