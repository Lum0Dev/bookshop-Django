from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('catalog/', catalog, name='catalog'),
    path('login/', login, name='login'),
    path('product/<int:product_id>/', show_product, name='product'),
    path('category/<int:cat_id>/', show_category, name='category')
]