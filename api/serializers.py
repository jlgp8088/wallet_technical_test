from rest_framework import serializers

class FiatUsdtSerializar(serializers.Serializer):
    amount_fiat = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    amount_usdt = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    fiat_code = serializers.CharField(max_length=3, required=True)


class trxCryptoSerializar(serializers.Serializer):
    hash = serializers.CharField(min_length=10, max_length=70, required=True)