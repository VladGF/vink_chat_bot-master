import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Order, Product, Order_Products


class Command(BaseCommand):
    help = 'Заполнить таблицу Order данными из файла orders.csv'

    def handle(self, *args, **options):
        file_path = 'data/orders.csv'

        Order_Products.objects.all().delete()
        Order.objects.all().delete()

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                order = Order(
                    registration_date=datetime.strptime(
                        row['Дата оформления'], '%Y-%m-%d %H:%M:%S'),
                    delivery_date=datetime.strptime(
                        row['Дата доставки'], '%Y-%m-%d %H:%M:%S'),
                    delivery_id=row['Номер доставщика'],
                    car_id=row['Номер машины'],
                    description=row['описание']
                )
                order.save()

                # Обработка продуктов в заказе
                product_ids = row['Товары'].split(';')
                quantities = row['Количество'].split(';')
                prices = row['Цены'].split(';')
                for product_id, quantity, price in zip(
                     product_ids, quantities, prices):
                    product = Product.objects.get(id=int(product_id))
                    order_product = Order_Products(
                        order=order,
                        product=product,
                        quantity=int(quantity),
                        price=float(price)
                    )
                    order_product.save()

        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
