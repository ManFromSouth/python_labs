from django.shortcuts import render
from django.http import HttpResponse
from django import template
# Create your views here.


def home(request):
    return render(request, 'Templates/static_handler.html')
    # Не привет мир, потому что проблемы с кодировкой, по крайней мере в моем браузере


def hello(request):
    return HttpResponse(u'Привет, мир!')
    # А так работает
