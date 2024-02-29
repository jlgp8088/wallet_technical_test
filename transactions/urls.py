from django.urls import path
from .views import create_fiat_payment,confirm_fiat_payment, create_blockchain_payment, report_fees

urlpatterns = [
    path('fiat-payment/', create_fiat_payment, name='create_fiat_payment'),
    path('fiat-payment-confirm/', confirm_fiat_payment, name='confirm_fiat_payment'),
    path('blockchain-payment/', create_blockchain_payment, name='create_blockchain_payment'),
    path('report-fees/', report_fees, name='report_fees'),
]
