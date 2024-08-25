from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views.generic import TemplateView


# main page class
class MainPage(TemplateView):
    template_name = "content/index.html"


class Product_rw(TemplateView):
    template_name = "content/product_rw.html"


class Product_piping(TemplateView):
    template_name = "content/product_piping.html"


class Product_iron_casting(TemplateView):
    template_name = "content/product_iron_casting.html"


def robots_txt(request):
    with open("content/templates/content/robots.txt", "r") as file:
        content = file.read()
    return HttpResponse(content, content_type="text")


def sitemap_xml(request):
    with open("content/templates/content/sitemap.xml", "r") as file:
        content = file.read()
        return HttpResponse(content, content_type="application/xml")


def ssl_validation(request):
    with open('content/templates/content/.well-known/pki-validation/92A02BB84FB4BD727D3E40F1502477C0.txt', 'r') as file:
        content = file.read()
        return HttpResponse(content, content_type='text')


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
