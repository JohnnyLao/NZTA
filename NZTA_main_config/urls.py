"""
URL configuration for NZTA_main_config project.
"""
from django.conf import settings

# languages urls
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse
from django.urls import include, path
from django.views.decorators.cache import cache_page

from NZTA_main_config.settings import CACHE_LIFI_TIME
from content.views import robots_txt, sitemap_xml, ssl_validation

# urls
urlpatterns = [
    # Main pages
    path("", include("content.urls", namespace="index")),
    # robots
    path("robots.txt", cache_page(CACHE_LIFI_TIME)(robots_txt), name="robots"),
    # sitemap
    path("sitemap.xml", cache_page(CACHE_LIFI_TIME)(sitemap_xml), name="sitemap"),
    # ssl
    path(".well-known/pki-validation/92A02BB84FB4BD727D3E40F1502477C0.txt", ssl_validation, name='ss_validation'),
]


# enable debug-toolbar DEBUG=True
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
