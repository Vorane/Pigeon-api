from django.dispatch import receiver
from .models import Wallet, PaymentTransaction
from .view_model import *
from .signals import *

@receiver(updateAvailableBalance)
def on_new_request(sender, **kwargs):
    wallet_id = kwargs.get('wallet_id')
    phone_number = kwargs.get('phone_number')
    updateAvailableBalance(wallet_id, phone_number)


