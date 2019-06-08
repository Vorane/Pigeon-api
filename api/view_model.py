from .models import Wallet, PaymentTransaction, OutletWallet, TransferTransaction
from orders.models import Order
from store_listing.models import Outlet
from commons.app_constants import AWAITING_FUNDS, READY_FOR_PROCESSING
from orders.orderutils import update_order_status

def updateAvailableBalance(wallet_id):
    """ Function to update available balance """
    wallet = Wallet.objects.filter(wallet_id=wallet_id).get()
    if wallet:
        orders = Order.objects.filter(wallet=wallet,order_status=AWAITING_FUNDS).get()
        total_amount = 0
        for order in orders:
            total_amount+= order.totalAmount()
            update_order_status(order_id=order.id, status=READY_FOR_PROCESSING)
        print('Total amount for orders is {}'.format(total_amount))
        wallet.available_balance-=total_amount
        wallet.save()

def transferPaymentToOutlet(amount, source_wallet_id, outlet_id):
    outlet = Outlet.objects.filter(id=outlet_id)
    try:
        if outlet :
            try:
                outletWallet = OutletWallet.objects.filter(outlet=outlet_id)
                if outletWallet and outletWallet.wallet:
                    outletWallet.wallet.available_balance += amount
                    outletWallet.save()
                    source_wallet = Wallet.objects.filter(id=source_wallet_id)
                    transaction = TransferTransaction(source_wallet = source_wallet, destination_wallet = outletWallet.wallet, amount = amount, isFinished=True, isSuccessFull= True)
                    transaction.save()
                elif outletWallet and outletWallet.wallet is None:
                    wallet = Wallet(phone_number = outlet.name)
                    wallet.save()
                    outletWallet.wallet = wallet
                    outletWallet.save()
                    transferPaymentToOutlet(amount=amount, source_wallet_id=source_wallet_id, outlet_id=outlet_id)
                elif outletWallet is None:
                    try:
                        wallet = Wallet.objects.filter(phone_number=outlet.name)
                    except Wallet.DoesNotExist:
                        wallet = Wallet(phone_number=outlet.name)
                        wallet.save()
                    outletWallet = OutletWallet(outlet=outlet, wallet = wallet)
                    outletWallet.save()
                    transferPaymentToOutlet(amount=amount, source_wallet_id=source_wallet_id, outlet_id=outlet_id)
                else:
                    raise Exception("Could not complete transfer transaction")

            except OutletWallet.DoesNotExist:
                raise Exception("The wallet account for {} does not exist".format(outlet.display_name))
    except Outlet.DoesNotExist:
        raise Exception("The outlet with this id does not exist")