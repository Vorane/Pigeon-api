from rest_framework.serializers import ModelSerializer

from api.models import Wallet


class WalletInlineSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("id", "phone_number")
