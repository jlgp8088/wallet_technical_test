from functools import wraps
from django.contrib.auth.models import User
from users.models import Users  # Importa tu modelo de usuario personalizado si lo tienes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

def attach_user_to_request(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                request.current_user = Users.objects.get(user_login=request.user.id)  # Reemplaza con tu modelo de usuario personalizado si es necesario
            except Users.DoesNotExist:
                return Response({"error": "El usuario no existe"}, status=HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "El usuario no está autenticado"}, status=HTTP_401_UNAUTHORIZED)
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
