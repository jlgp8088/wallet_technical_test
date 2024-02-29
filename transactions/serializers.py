from rest_framework import serializers
from users.serializers import AdminUserSerializer
import re

class FiatPaymentSerializar(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    coincode = serializers.CharField(max_length=3)
    destiny = serializers.CharField(max_length=42)
    user = AdminUserSerializer(many=False, required=False)
    created_at = serializers.DateTimeField(required=False)
    processed = serializers.BooleanField(required=False)

    def validate_hash_value(self, value):
        # Expresión regular para validar el formato del hash
        regex = r'^0x[a-fA-F0-9]{40}$'

        # Validar el formato del hash utilizando expresiones regulares
        if not re.match(regex, value):
            raise serializers.ValidationError("invalid address structure")

        return value

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



