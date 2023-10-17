from django.conf import settings
from django.utils import translation
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.exceptions import Resolver404
from django.urls import resolve
from urllib.parse import urlparse


# main page class
class MainPage(TemplateView):
    template_name = 'content/index.html'


class Product_rw(TemplateView):
    template_name = 'content/product_rw.html'

class Product_piping(TemplateView):
    template_name = 'content/product_piping.html'


class Product_iron_casting(TemplateView):
    template_name = 'content/product_iron_casting.html'


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(
            f"{view.namespace}:{view.url_name}", args=view.args, kwargs=view.kwargs
        )
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response