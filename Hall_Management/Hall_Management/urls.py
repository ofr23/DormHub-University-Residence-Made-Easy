from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hallAdmin/', include('Hall_Admin.urls')),
    path('varsityAdmin/', include('Varsity_Admin.urls')),
    path('provost/', include('Provost.urls')),
    path('staff/', include('Staff.urls')),
    path('student/', include('Student.urls')),
    path('authentication/', include('Authentication.urls')),
]


# Serve static and media files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
