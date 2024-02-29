from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User as DjangoUser
from users.models import Users, Wallets, UserFeeConfiguration
from rest_framework import status
from .serializers import AdminUserSerializer, UserResponseSerializer
from django.db import IntegrityError
from auth.decorators import attach_user_to_request
from api.exchange import create_wallet
from django.db import transaction


@api_view(['POST'])
def create_user(request):
    serializer = AdminUserSerializer(data=request.data)
    if serializer.is_valid():
      name = serializer.data['name']
      email = serializer.data['email']
      password = serializer.data['password']
      fee_mode = serializer.data['fee_mode']
      try:
        with transaction.atomic():
          fee = UserFeeConfiguration.objects.get(mode=fee_mode)
          admin_user = DjangoUser.objects.create_user(username=email, email=email, password=password)
          user = Users(name=name, email=email, user_login= admin_user, fee_mode=fee)
          address = create_wallet()
          user.save()
          wallet = Wallets.objects.create(address=address, user=user)
          wallet.save()
        return Response({}, status=status.HTTP_201_CREATED)
      except IntegrityError:
          return Response({'error': 'email creado anteriormente'}, status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@attach_user_to_request
def get_info_user(request):
    currentUser= request.current_user
    serializer = UserResponseSerializer(currentUser)  
    return Response(serializer.data)