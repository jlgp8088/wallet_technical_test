from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import FiatPaymentSerializar
from auth.decorators import attach_user_to_request
from transactions.domain.fiatPayment import create_payment_process
# Create your views here.

@api_view(['POST'])
@attach_user_to_request
def create_fiat_payment(request):
  currentUser = request.current_user
  dataFiatPayment = FiatPaymentSerializar(data=request.data)
  if dataFiatPayment.is_valid():
      amount = dataFiatPayment.data['amount']
      coin_code = dataFiatPayment.data['coincode']
      try:
          response = create_payment_process (amount=amount, coin_code=coin_code, user=currentUser)
          return Response(response, status=status.HTTP_201_CREATED)
      except Exception as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  else:
    return Response(dataFiatPayment.errors, status=status.HTTP_400_BAD_REQUEST)
