"""
   urls for Authentication

   """

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# URL patterns for the application
urlpatterns = [
    # Path for the login page
    path('', views.logIn, name='logIn'),

    # Path for the registration page
    path('register/', views.register, name='register'),
]

# Add static URL patterns for serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
