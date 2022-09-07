from django.urls import path

from .views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('catalog/', BooksCatalog.as_view(), name='catalog'),
    path('login/', login, name='login'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('category/<slug:cat_slug>/', BooksCategory.as_view(), name='category')
]