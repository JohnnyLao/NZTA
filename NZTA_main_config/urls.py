"""
URL configuration for NZTA_main_config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# languages urls
from django.conf.urls.i18n import i18n_patterns

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('content.urls', namespace='index')),
    prefix_default_language=True
)

# enable media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# enable debug-toolbar DEBUG=True
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
