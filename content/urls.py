from django.urls import path
from content.views import MainPage, set_language

app_name = 'content'

# url path
urlpatterns = [
    # main page
    path('', MainPage.as_view(), name='main_page'),
    # languages
    path("set_language/<str:language>", set_language, name="set_language"),
]