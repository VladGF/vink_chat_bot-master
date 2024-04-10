from datetime import datetime

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Product, Question, Order
from .serializers import ProductSerializer
from .services import yandex_gpt


class ProductInfoAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_number'

    def retrieve(self, request, *args, **kwargs):
        instance: Product = self.get_object()
        question_for_database = (
            f"Получить информацию по товару {instance.product_number}."
        )
        Question.objects.create(
            description=question_for_database,
            date=datetime.now(),
            is_done=False
        )
        is_available_Moscow = ""
        is_available_Saint_Petersburg = ""
        if instance.is_available_Moscow is True:
            is_available_Moscow = "товар есть в наличии в Москве"
        if instance.is_available_Saint_Petersburg is True:
            is_available_Saint_Petersburg = "товар есть в наличии в Санкт Петербурге"
        question = (
            f"Расскажи от своего именни консультанта подробно"
            f" о том, что у нас в каталоге есть {instance.name}, "
            f"его артикул {instance.product_number}, его "
            f"цена {instance.price} рублей, {is_available_Moscow},"
            f" {is_available_Saint_Petersburg}. Не придумывай "
            "особо ничего лишнего, пиши четко и ясно.")
        result_text = yandex_gpt(question)
        return Response({"text": result_text})


class ProductInfoDefaultAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"text": "Пожалуйста, введите артикул товара."})


class ProductAvailableAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_number'

    def retrieve(self, request, *args, **kwargs):
        instance: Product = self.get_object()
        question_for_database = (
            f"Проверить наличие товара {instance.product_number}."
        )
        Question.objects.create(
            description=question_for_database,
            date=datetime.now(),
            is_done=False
        )
        is_available_Moscow = ""
        is_available_Saint_Petersburg = ""
        if instance.is_available_Moscow is True:
            is_available_Moscow = "есть в наличии в Москве"
        if instance.is_available_Saint_Petersburg is True:
            is_available_Saint_Petersburg = "есть в наличии в Санкт Петербурге"
        question = (
            f"Расскажи от своего именни консультанта подробно"
            f" о том, что товар {instance.name} {is_available_Moscow},"
            f"{is_available_Saint_Petersburg}. Не придумывай "
            "особо ничего лишнего, пиши четко и ясно.")
        result_text = yandex_gpt(question)
        return Response({"text": result_text})


class OrderInfoAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance: Order = self.get_object()
        question_for_database = (
            f"Получить информацию по заказу {instance.pk}."
        )
        Question.objects.create(
            description=question_for_database,
            date=datetime.now(),
            is_done=False
        )
        products_names = ", ".join([product.name for product in
                                   instance.products.all()])
        question = (
            f"Расскажи от своего именни консультанта подробно"
            f" о даннои заказе. Дата оформления {instance.registration_date}, "
            f" товары: {products_names},"
            f"дата доставки {instance.delivery_date},"
            f" номер курьера {instance.delivery_id}, "
            f"Номер машины {instance.car_id}, описание"
            f" {instance.description}.  Не придумывай "
            "особо ничего лишнего, пиши четко и ясно.")
        result_text = yandex_gpt(question)
        return Response({"text": result_text})


class OrderInfoDefaultAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"text": "Пожалуйста, введите номер заказа."})


class OwnQuestionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        question_text = data.get('text', '')

        if not question_text:
            return Response({"error": "Текст вопроса отсутствует"},
                            status=status.HTTP_400_BAD_REQUEST)

        result_text = yandex_gpt(question_text)

        return Response({"text": result_text}, status=status.HTTP_200_OK)


class ValueBotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        Question.objects.create(
            description=request.data["description"],
            date=datetime.now(),
            is_done=request.data["is_done"]
        )
        return Response({"text": "Сейчас переведем на оператора"})
