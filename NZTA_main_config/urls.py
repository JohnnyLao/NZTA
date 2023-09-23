"""
URL configuration for NZTA_main_config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls', namespace='index'))
]
# enable media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# enable debug-toolbar DEBUG=True
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))