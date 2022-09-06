from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('catalog/', catalog, name='catalog'),
    path('login/', login, name='login'),
    path('product/<slug:product_slug>/', show_product, name='product'),
    path('category/<slug:cat_slug>/', show_category, name='category')
]