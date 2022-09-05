from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


def index(request):
    products = Books.objects.all()
    context = {
        'products': products,
        'title': 'Главная страница',
        'cat_selected': 0
    }

    return render(request, 'books/index.html', context=context)

def catalog(request):
    products = Books.objects.all()
    context = {
        'products': products,
        'title': 'Каталог',
        'cat_selected': 0
    }

    return render(request, 'books/catalog.html', context=context)

def about(request):
    return render(request, 'books/about.html', {'title': 'О магазине'})

def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')

def show_product(request, product_id):
    return HttpResponse(f'<h1>Продукт: {product_id}</h1>')

def show_category(request, cat_id):
    products = Books.objects.filter(cat_id=cat_id)

    if len(products) == 0:
        raise Http404()

    context = {
    'products': products,
    'title': 'Отображение по категориям',
    'cat_selected': cat_id
    }

    return render(request, 'books/catalog.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')