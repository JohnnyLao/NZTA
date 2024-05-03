from django.urls import path
from django.views.decorators.cache import cache_page

from content.views import (MainPage, Product_iron_casting, Product_piping,
                           Product_rw, robots_txt, set_language, sitemap_xml)
from NZTA_main_config.settings import CACHE_LIFI_TIME

app_name = "content"

# url path
urlpatterns = [
    # main page
    path("", cache_page(CACHE_LIFI_TIME)(MainPage.as_view()), name="main_page"),
    # product_rw page
    path(
        "badges&Pads",
        cache_page(CACHE_LIFI_TIME)(Product_rw.as_view()),
        name="Product_rw",
    ),
    # product_piping page
    path(
        "piping",
        cache_page(CACHE_LIFI_TIME)(Product_piping.as_view()),
        name="Product_piping",
    ),
    # product_iron_casting page
    path(
        "iron_casting",
        cache_page(CACHE_LIFI_TIME)(Product_iron_casting.as_view()),
        name="Product_iron_casting",
    ),
    # languages
    path("set_language/<str:language>", set_language, name="set_language"),
]
