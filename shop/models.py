from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


User = get_user_model()

# 1.Category
# 2.Product
# 3.CartProduct #  продукт в корзина
# 4.Cart корзина
# 5.Customer


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True  # Невозможно создать миграцию, необходим класс-потомок служит шаблоном/каркасом

    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Notebook(Product):
    diagonal = models.FloatField(verbose_name='Диагональ')
    display = models.FloatField(verbose_name='Дисплей')
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model


class Smartphone(Product):
    diagonal = models.FloatField(verbose_name='Диагональ')
    display = models.FloatField(verbose_name='Дисплей')
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model


class CartProduct(models.Model):  # Продукты в корзине

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')  # Contentype видит все модели,
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return f'Продукт {self.content_object} в корзине'

# p = NotebookProduct.objects.get(pk=1)
# cp = CartProduct.objects.create(content_object=p) pk пойдет в object_id


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return f'{self.id}'


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return f'Покупатель {self.user.username}'

