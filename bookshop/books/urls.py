from django.urls import path

from .views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('catalog/', BooksCatalog.as_view(), name='catalog'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('category/<slug:cat_slug>/', BooksCategory.as_view(), name='category')
]