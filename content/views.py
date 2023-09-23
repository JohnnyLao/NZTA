from django.views.generic import TemplateView


# main page class
class MainPage(TemplateView):
    template_name = 'content/index.html'
