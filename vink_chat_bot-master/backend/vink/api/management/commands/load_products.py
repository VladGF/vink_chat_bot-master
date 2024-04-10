import csv
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = 'Заполнить таблицу Product данными из файла products.csv'

    def handle(self, *args, **options):
        file_path = 'data/products.csv'  # Путь к вашему файлу CSV

        # Очищаем таблицу перед заполнением
        Product.objects.all().delete()

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    name=row['Название товара'],
                    product_number=row['Артикул товара'],
                    price=float(row['Цена товара']),
                    measurement_unit=row['Единица измерения'],
                    is_available_Moscow=row['Доступность в Москве'].lower() == 'true',
                    is_available_Saint_Petersburg=row['Доступность в Спб'].lower() == 'true'
                )
                product.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
