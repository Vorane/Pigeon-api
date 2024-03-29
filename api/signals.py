from django.conf import settings
import django.dispatch

updateAvailableBalance = django.dispatch.Signal(providing_args=["wallet_id","phone_number"])
sendSMSReceipt = django.dispatch.Signal(providing_args=["message","phone_number"])
transferPayment = django.dispatch.Signal(providing_args=["amount", "source_wallet_id", "outlet_id"])
