from .models import Wallet, PaymentTransaction

def updateAvailableBalance(wallet_id, phone_number):
    """ Function to update available balance """
    wallet = Wallet.objects.filter(wallet_id=wallet_id).get()
