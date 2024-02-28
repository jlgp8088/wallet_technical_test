from django.urls import path, include
from .views import create_fiat_payment

urlpatterns = [
    path('fiat-payment/', create_fiat_payment, name='create_fiat_payment'),
]
