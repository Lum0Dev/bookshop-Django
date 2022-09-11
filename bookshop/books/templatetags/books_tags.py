from django import template
from books.models import *

register = template.Library()

@register.simple_tag(name='get_cats')
def get_categories(sort=None):
    if not sort:
        return Category.objects.all()
    else:
        return Category.objects.order_by(sort)

@register.simple_tag()
def get_menu():
    menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'О магазине', 'url_name': 'about'},
    {'title': 'Войти', 'url_name': 'login'}
    ]

    return menu

@register.simple_tag(name='get_img')
def get_images(group=None):
    if not group:
        return Books.objects.order_by('pk').filter(is_published=True)[:3]
    elif group == 'first':
        return Books.objects.order_by('-pk').filter(is_published=True)[:4]
    elif group == 'second':
        return Books.objects.order_by('-pk').filter(is_published=True)[4:8]
