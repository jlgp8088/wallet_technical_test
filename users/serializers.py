from rest_framework import serializers
import re
from users.models import Users, UserFeeConfiguration

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
    fee_mode = serializers.CharField(max_length=1, required=True)

    def validate_fee_mode(self, value):
        try:
            UserFeeConfiguration.objects.get(mode=value)
        except UserFeeConfiguration.DoesNotExist:
            raise serializers.ValidationError("El fee_mode especificado no existe")
        
        return value


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name','email'] 


class UserFeeConfigurationSerializar(serializers.Serializer):
    user = AdminUserSerializer(many=False)
    mode = serializers.CharField(max_length=1)
    payment_fee_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    trade_fee_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)

