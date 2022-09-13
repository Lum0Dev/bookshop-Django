from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy

from .models import *
from .utils import *
from .forms import *


class ShopHome(ListView):
    model = Books
    template_name = 'books/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class BooksCatalog(DataMixin, ListView):
    model = Books
    template_name = 'books/catalog.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Каталог')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Books.objects.filter(is_published=True)

def about(request):
    return render(request, 'books/about.html', {'title': 'О магазине'})

class ShowProduct(DataMixin, DetailView):
    model = Books
    template_name = 'books/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'], 
            cat_selected=context['product'].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

class BooksCategory(DataMixin, ListView):
    model = Books
    template_name = 'books/catalog.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['products'][0].cat), 
            cat_selected=context['products'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Books.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')