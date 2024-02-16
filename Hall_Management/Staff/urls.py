from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # URL pattern for staff view
    path('', views.staff, name='staff'),

    # URL pattern for visitorToday view
    path('visitorToday/', views.visitorToday, name='visitorToday'),
]

# Add static and media URL patterns for serving static and media files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
