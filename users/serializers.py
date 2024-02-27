from rest_framework import serializers
import re
from .models import Users

class PasswordValidator:
    def __call__(self, password):
        if len(password) < 8:
            raise serializers.ValidationError()
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError()
        if not re.search(r'[a-z]', password):
            raise serializers.ValidationError()
        if not re.search(r'[0-9]', password):
            raise serializers.ValidationError()
        if not re.search(r'[!@#$%^&*()_+=-]', password):
            raise serializers.ValidationError()
        return password

class AdminUserSerializer(serializers.Serializer):
    name  = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(max_length=150, required=True)
    password = serializers.CharField(max_length=10, validators=[PasswordValidator()])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name','email'] 


