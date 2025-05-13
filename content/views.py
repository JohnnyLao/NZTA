from urllib.parse import urlparse
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views.generic import TemplateView


class MainPage(TemplateView):

    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ru':
            return ['content/index.html',]
        elif self.request.LANGUAGE_CODE == 'en':
            return ['content/index-en.html',]
        else:
            return ['content/index.html',]


class Product_rw(TemplateView):
    template_name = "content/product_rw.html"

    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ru':
            return ['content/product_rw.html',]
        elif self.request.LANGUAGE_CODE == 'en':
            return ['content/product_rw-en.html',]
        else:
            return ['content/index.html',]


class Product_piping(TemplateView):
    template_name = "content/product_piping.html"

    def get_template_names(self):
        if self.request.LANGUAGE_CODE == 'ru':
            return ['content/product_piping.html',]
        elif self.request.LANGUAGE_CODE == 'en':
            return ['content/product_piping-en.html',]
        else:
            return ['content/index.html',]


class Product_iron_casting(TemplateView):
    template_name = "content/product_iron_casting.html"

    def get_template_names(self):
        print(self.request.LANGUAGE_CODE)
        if self.request.LANGUAGE_CODE == 'ru':
            return ['content/product_iron_casting.html', ]
        elif self.request.LANGUAGE_CODE == 'en':
            return ['content/product_iron_casting-en.html', ]
        else:
            return ['content/index.html',]


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

    translation.activate(language)
    response = redirect(reverse('index:main_page'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)

    return response

