from django.db import models


class Product(models.Model):
    name = models.CharField('Название товара', max_length=200)
    product_number = models.CharField(
        'Артикул товара', max_length=100, unique=True)
    price = models.FloatField('Цена товара')
    measurement_unit = models.CharField('Единица измерения', max_length=50)
    is_available_Moscow = models.BooleanField('Доступность в Москве')
    is_available_Saint_Petersburg = models.BooleanField('Доступность в Спб')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    registration_date = models.DateTimeField('Дата оформления')
    products = models.ManyToManyField(Product, through='Order_Products')
    delivery_date = models.DateTimeField('Дата доставки')
    delivery_id = models.CharField('Номер доставщика', max_length=100)
    car_id = models.CharField('Номер машины', max_length=50)
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Order_Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество товара в заказе')
    price = models.FloatField('Цена товара в заказе')

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'


class Question(models.Model):
    description = models.TextField('Текст вопроса')
    date = models.DateTimeField('Дата')
    is_done = models.BooleanField('Решен ли вопрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
