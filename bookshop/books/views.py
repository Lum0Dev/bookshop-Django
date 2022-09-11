from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView

from .models import *


class ShopHome(ListView):
    model = Books
    template_name = 'books/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class BooksCatalog(ListView):
    model = Books
    template_name = 'books/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Books.objects.filter(is_published=True)

def about(request):
    return render(request, 'books/about.html', {'title': 'О магазине'})

def login(request):
    return HttpResponse(f'<h1>Авторизация</h1>')

class ShowProduct(DetailView):
    model = Books
    template_name = 'books/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product']
        context['cat_selected'] = context['product'].cat_id
        return context

class BooksCategory(ListView):
    model = Books
    template_name = 'books/catalog.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['products'][0].cat)  
        context['cat_selected'] = context['products'][0].cat_id
        return context

    def get_queryset(self):
        return Books.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')