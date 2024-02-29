from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from transactions.serializers import FiatPaymentSerializar, BlockchainPaymentSerializar
from auth.decorators import attach_user_to_request
from transactions.domain.payments import create_fiat_payment_process, confirm_fiat_payment_process, create_blockchain_payment_process
from api.serializers import hashSerializar
from coins.models import CryptoCoin

# Create your views here.

@api_view(['POST'])
@attach_user_to_request
def create_fiat_payment(request):
  currentUser = request.current_user
  dataFiatPayment = FiatPaymentSerializar(data=request.data)
  if dataFiatPayment.is_valid():
      amount = dataFiatPayment.data['amount']
      coin_code = dataFiatPayment.data['coincode']
      wallet_destiny = dataFiatPayment.data['destiny']
      try:
          response = create_fiat_payment_process(amount=amount, coin_code=coin_code, user=currentUser, destiny=wallet_destiny)
          return Response(response, status=status.HTTP_201_CREATED)
      except Exception as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(dataFiatPayment.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@attach_user_to_request
def confirm_fiat_payment(request):
  currentUser = request.current_user
  dataFiatConfirmation = hashSerializar(data=request.data)
  if dataFiatConfirmation.is_valid():
      hash = dataFiatConfirmation.data['hash']
      try:
          response = confirm_fiat_payment_process(hash=hash, user=currentUser)
          return Response(response, status=status.HTTP_201_CREATED)
      except Exception as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(dataFiatConfirmation.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['POST'])
@attach_user_to_request
def create_blockchain_payment(request):
  currentUser = request.current_user
  dataBlockChain = BlockchainPaymentSerializar(data=request.data)
  if dataBlockChain.is_valid():
      amount = dataBlockChain.data['amount']
      coin_code = dataBlockChain.data['coin']
      wallet_destiny = dataBlockChain.data['destiny']
      try:
          coin = CryptoCoin.objects.get(code=coin_code)
          response = create_blockchain_payment_process(amount=amount, coin=coin, user=currentUser, destiny=wallet_destiny)
          return Response(response, status=status.HTTP_201_CREATED)
      except Exception as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(dataBlockChain.errors, status=status.HTTP_400_BAD_REQUEST)
