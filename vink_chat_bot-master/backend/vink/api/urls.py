from django.urls import path
import api.views as views

app_name = 'api'

urlpatterns = [
    path('product/info/<str:product_number>/', views.ProductInfoAPIView.as_view(), name='product-info'),
    path('product/info/', views.ProductInfoDefaultAPIView.as_view(), name='product-info-default'),
    path('product/check/<str:product_number>/', views.ProductAvailableAPIView.as_view(), name='product-info'),
    path('product/check/', views.ProductInfoDefaultAPIView.as_view(), name='product-check-default'),
    path('order/info/<str:pk>/', views.OrderInfoAPIView.as_view(), name='order-info'),
    path('order/info/', views.OrderInfoDefaultAPIView.as_view(), name='order-info-default'),
    path('own_question/', views.OwnQuestionAPIView.as_view(), name='own_question'),
    path('value_bot/', views.ValueBotAPIView.as_view(), name='value_bot'),
]
