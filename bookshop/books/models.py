from django.db import models
from django.urls import reverse

class Books(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    title_eng = models.CharField(max_length=255, null=True, blank=True, verbose_name='Иностранное название')
    content = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    sale = models.IntegerField(blank=True, default=0, verbose_name='Скидка, %')
    pages_count = models.IntegerField(null=True, blank=True, verbose_name='Страниц')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, verbose_name='Автор')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def get_sale(self):
        price = self.price * (100-self.sale) / 100
        return price

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['time_create', 'title']


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']