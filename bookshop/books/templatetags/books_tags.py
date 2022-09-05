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