from .models import Wallet, PaymentTransaction
from orders.models import Order

def updateAvailableBalance(wallet_id):
    """ Function to update available balance """
    wallet = Wallet.objects.filter(wallet_id=wallet_id).get()
    if wallet:
        orders = Order.objects.filter(wallet=wallet,order_status="pending").get()
        total_amount = 0
        for order in orders:
            total_amount+= order.totalAmount()
        print('Total amount for orders is {}'.format(total_amount))
        wallet.available_balance-=total_amount
        wallet.save()

