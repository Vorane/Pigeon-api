from django.dispatch import receiver
from .models import Wallet, PaymentTransaction
from .view_model import *
from .signals import *
from .sms import send_sms

@receiver(updateAvailableBalance)
def on_new_request(sender, **kwargs):
    wallet_id = kwargs.get('wallet_id')
    print('calling update balance')
    updateAvailableBalance(wallet_id)

@receiver(sendSMSReceipt)
def send_sms_notification(sender, **kwargs):
    message = kwargs.get('message')
    phone_number = kwargs.get('phone_number')
    send_sms(message, phone_number)


