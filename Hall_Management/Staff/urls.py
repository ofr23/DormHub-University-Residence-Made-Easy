"""
Django URL Configuration Documentation

This module defines URL patterns for various views and static/media file serving during development.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # URL pattern for the main staff view
    path('', views.staff, name='staff'),
    path('repairRequests/',views.repairRequests,name='repairRequests'),
    # URL pattern for the visitorToday view
    path('visitorToday/', views.visitorToday, name='visitorToday'),
]
"""
URL Patterns:

1. Staff View:
   - URL: /
   - View: views.staff
   - Name: 'staff'
   - Description: Renders the main staff view.

2. Visitor Today View:
   - URL: /visitorToday/
   - View: views.visitorToday
   - Name: 'visitorToday'
   - Description: Renders the view for visitors today.

Static and Media File Serving:
- Static files (e.g., CSS, JavaScript) are served through the STATIC_URL and STATIC_ROOT settings.
- Media files (e.g., uploaded user files) are served through the MEDIA_URL and MEDIA_ROOT settings.

Note: 
- During development, Django serves static and media files using these URL patterns.
- In production, these URL patterns might be handled differently (e.g., by a web server or CDN).
"""
# Static URL patterns for serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
