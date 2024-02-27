from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User as DjangoUser
from .models import Users
from rest_framework import status
from .serializers import AdminUserSerializer, UserSerializer
from django.db import IntegrityError
from auth.decorators import attach_user_to_request
@api_view(['POST'])
def create_user(request):
    serializer = AdminUserSerializer(data=request.data)
    if serializer.is_valid():
      name = request.data.get('name')
      email = request.data.get('email')
      password = request.data.get('password')
      try:
          admin_user = DjangoUser.objects.create_superuser(username=email, email=email, password=password)
          user = Users(name=name, email=email, user_login= admin_user)
          user.save()
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
    serializer = UserSerializer(currentUser)  
    return Response(serializer.data)