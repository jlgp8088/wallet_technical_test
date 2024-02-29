from rest_framework import serializers
from users.serializers import AdminUserSerializer
from transactions.models import FiatPayment
from coins.models import CryptoCoin
from utils.views import validate_address
class FiatPaymentSerializar(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    coincode = serializers.CharField(max_length=3)
    destiny = serializers.CharField(max_length=42)
    user = AdminUserSerializer(many=False, required=False)
    created_at = serializers.DateTimeField(required=False)
    processed = serializers.BooleanField(required=False)

    def validate_destiny(self, value):
        if validate_address(value):
            raise serializers.ValidationError("invalid address structure")
        return value

class TradeSerializar(serializers.Serializer):
    # fiat_payment = FiatPaymentSerializar(many=False)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    processed = serializers.BooleanField()

class BlockchainPaymentSerializar(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    coin = serializers.CharField(max_length=3)
    destiny = serializers.CharField(max_length=42)

    def validate_coin(self, value):
        try:
            CryptoCoin.objects.get(code=value)
        except CryptoCoin.DoesNotExist:
            raise serializers.ValidationError("Invalid Crypto")
        
        return value
    
    def validate_destiny(self, value):
        if validate_address(value):
            raise serializers.ValidationError("invalid address structure")
        return value

class FiatPaymentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiatPayment
        fields = ['amount_fiat','fiat_code', 'processed_date']
