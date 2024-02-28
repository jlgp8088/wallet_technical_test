from rest_framework import serializers
from users.serializers import AdminUserSerializer

class FiatPaymentSerializar(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    coincode = serializers.CharField(max_length=3)
    user = AdminUserSerializer(many=False, required=False)
    created_at = serializers.DateTimeField(required=False)
    processed = serializers.BooleanField(required=False)

class TradeSerializar(serializers.Serializer):
    # fiat_payment = FiatPaymentSerializar(many=False)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    processed = serializers.BooleanField()

class BlockchainPaymentSerializar(serializers.Serializer):
    trade = TradeSerializar(many=False)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    fee_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    processed = serializers.BooleanField()



