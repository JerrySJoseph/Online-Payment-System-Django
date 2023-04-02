from wallet.models import Wallet
from wallet.utils.wallet import balance_check,deduct_money_from_wallet,add_money_to_wallet
from transaction.models import TransactionType, TransactionStatus
from django.contrib.auth.models import User
from transaction.utils.transactions import create_transaction,_generate_transaction_id




def transfer_money_by_id(sender_id, recipient_id, amount, currency):
    balance_check(sender_id,amount,currency)
    #raise TransferException('Some random transfer exception')
    return _transfer_money_by_id(sender_id,recipient_id,amount,currency)

def _transfer_money_by_id(sender_id, recipient_id, amount, currency):

    sender=User.objects.get(id=sender_id)
    recipient=User.objects.get(id=recipient_id)

    # deduct money from sender wallet
    sender_wallet = Wallet.objects.get(user_id=sender.id)
    sender_balance=deduct_money_from_wallet(sender_wallet, amount, currency)

    # add money to recipient wallet
    recipient_wallet = Wallet.objects.get(user_id=recipient.id)
    recipient_balance=add_money_to_wallet(recipient_wallet, amount, currency)

    tid=_generate_transaction_id()
    # create sender debit transaction
    create_transaction(tid,sender,sender,recipient,TransactionType.DEBIT,TransactionStatus.SUCCESS,amount,currency,sender_balance)
    
    # create recipient credit transaction
    create_transaction(tid,recipient,sender,recipient,TransactionType.CREDIT,TransactionStatus.SUCCESS,amount,currency,recipient_balance)
    
    return True

