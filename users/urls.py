from django.urls import path
from .views import create_user, get_info_user



urlpatterns = [
    path('', get_info_user, name='get_info_user'),
    path('create', create_user, name='create_user'),
]
