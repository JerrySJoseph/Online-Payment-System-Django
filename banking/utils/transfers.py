from wallet.models import Wallet
from wallet.utils.wallet import balance_check,deduct_money_from_wallet,add_money_to_wallet
from transaction.models import TransactionType, TransactionStatus
from django.contrib.auth.models import User
from transaction.utils.transactions import create_transaction,_generate_transaction_id
from ..models import TransferRequest
from django.db.models import Q

import decimal



def transfer_money_by_id(sender_id, recipient_id, amount, currency):
    if not type(amount)=='Decimal':
        amount=decimal.Decimal(amount)
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

def create_transfer_request(sender_id:int, recipient_id:int,amount,currency):
    rid=_generate_transaction_id()
    sender=User.objects.get(id=sender_id)
    recipient=User.objects.get(id=recipient_id)
    tr_request=TransferRequest(
        rid=rid,
        sender=sender,
        recipient=recipient,
        source=sender,
        amount=decimal.Decimal(amount),
        currency=currency,
    )
    tr_request.save()

def get_transfer_requests_by_id_qs(user_id:int)->list:
    return list(get_transfer_requests_by_id(user_id))

def get_transfer_requests_by_id(user_id:int,group='all')->list:
    
    if group=='sent':
        query=Q(sender_id__exact=user_id)
    elif group=='recieved':
        query=Q(recipient_id__exact=user_id)
    else :
        query=Q(sender_id__exact=user_id)|Q(recipient_id__exact=user_id)
    transactions=TransferRequest.objects.filter(
        query
    )
    return transactions.all()

def get_transfer_request_by_id(rid:int):
    return TransferRequest.objects.get(id=rid)

def withdraw_transfer_request(rid:int):
    request=get_transfer_request_by_id(rid)
    request.delete()
    return True