from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# Define urlpatterns for the Varsity_Admin app

urlpatterns = [
    # Define the URL pattern for the varsityAdmin view
    path('', views.varsityAdmin, name='varsityAdmin'),
]

# Add static and media URL patterns for serving static and media files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
