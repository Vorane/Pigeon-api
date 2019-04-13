from .models import Wallet, PaymentTransaction, OutletWallet
from orders.models import Order
from store_listing.models import Outlet

def updateAvailableBalance(wallet_id):
    """ Function to update available balance """
    wallet = Wallet.objects.filter(wallet_id=wallet_id).get()
    if wallet:
        orders = Order.objects.filter(wallet=wallet,order_status="served").get()
        total_amount = 0
        for order in orders:
            total_amount+= order.totalAmount()
        print('Total amount for orders is {}'.format(total_amount))
        wallet.available_balance-=total_amount
        wallet.save()

def transferPaymentToOutlet(amount, outlet_id):
    outlet = Outlet.objects.filter(id=outlet_id)
    try:
        if outlet :
            outletWallet = OutletWallet.objects.filter(outlet=outlet_id)
            try:
                outlet.wallet = None
            except OutletWallet.DoesNotExist:
                raise Exception("The wallet account for {} does not exist".format(outlet.display_name))
    except Outlet.DoesNotExist:
        raise Exception("The outlet with this id does not exist")