from django.urls import path
from content.views import MainPage, Product_rw,Product_piping, Product_iron_casting, set_language

app_name = 'content'

# url path
urlpatterns = [
    # main page
    path('', MainPage.as_view(), name='main_page'),
    # product_rw page
    path('badges&Pads', Product_rw.as_view(), name='Product_rw'),
    # product_piping page
    path('piping', Product_piping.as_view(), name='Product_piping'),
    # product_iron_casting page
    path('iron_casting', Product_iron_casting.as_view(), name='Product_iron_casting'),
    # languages
    path("set_language/<str:language>", set_language, name="set_language"),
]