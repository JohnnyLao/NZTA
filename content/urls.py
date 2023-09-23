from django.urls import path
from content.views import MainPage

app_name = 'content'

# url path
urlpatterns = [
    # main page
    path('', MainPage.as_view(), name='main_page')
]