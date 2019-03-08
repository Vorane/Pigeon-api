from django.dispatch import receiver
from .models import Wallet, PaymentTransaction
from .view_model import *
from .signals import *

@receiver(updateAvailableBalance)
def on_new_request(sender, **kwargs):
    wallet_id = kwargs.get('wallet_id')
    print('calling update balance')
    updateAvailableBalance(wallet_id)


