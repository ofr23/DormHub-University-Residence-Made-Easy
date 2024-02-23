from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
<<<<<<< HEAD
=======
    # Example path including app-specific URLs
>>>>>>> f3f61727b63cb6afa26d1f4171b20472953bd74b
]

# Static and media URLs for development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
