from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # URL pattern for the Provost dashboard
    path('', views.provost, name='provost'),
    path('swapRequests/',views.swapRequests,name='swapRequests'),
    # URL pattern for adding a student
    path('addStudent/', views.addStudent, name='addStudent'),
]

# Serve static and media files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
