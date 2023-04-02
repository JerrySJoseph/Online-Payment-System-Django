from wallet.models import Wallet
from django.core.exceptions import ValidationError
from .exceptions.TransactionException import TransferException
from transaction.models import TransactionType, Transaction, TransactionStatus
from django.contrib.auth.models import User
import uuid

conversion = {
    'USD': {
        'GBP': 0.82,
        'EUR': 0.93,
        'USD': 1
    },
    'GBP': {
        'GBP': 1,
        'EUR': 1.13,
        'USD': 1.22
    },
    'EUR': {
        'GBP': 0.88,
        'EUR': 1,
        'USD': 1.08
    }
}


def balance_check(sender_id, amount, currency):
    sender_wallet = Wallet.objects.get(user_id=sender_id)
    sender_balance = sender_wallet.balance * conversion[sender_wallet.currency][currency]
    required_balance = amount*conversion[currency][sender_wallet.currency]

    if amount > sender_balance:
        raise TransferException(
            f'Insufficient funds: You require {required_balance} in {sender_wallet.currency} to proceed with this transaction.')
    return {
        'balance': sender_balance-required_balance,
        'currency': sender_wallet.currency,
        'success': True
    }


def transfer_money_by_id(sender_id, recipient_id, amount, currency):
    balance_check(sender_id,amount,currency)
    #raise TransferException('Some random transfer exception')
    return _transfer_money_by_id(sender_id,recipient_id,amount,currency)

def _transfer_money_by_id(sender_id, recipient_id, amount, currency):

    sender=User.objects.get(id=sender_id)
    recipient=User.objects.get(id=recipient_id)

    # deduct money from sender wallet
    sender_wallet = Wallet.objects.get(user_id=sender.id)
    _deduct_money_from_wallet(sender_wallet, amount, currency)

    # add money to recipient wallet
    recipient_wallet = Wallet.objects.get(user_id=recipient.id)
    _add_money_to_wallet(recipient_wallet, amount, currency)

    tid=_generate_transaction_id()
    # create sender debit transaction
    _create_transaction(tid,sender,recipient,TransactionType.DEBIT,TransactionStatus.SUCCESS,amount,currency)
    
    # create recipient credit transaction
    _create_transaction(tid,sender,recipient,TransactionType.CREDIT,TransactionStatus.SUCCESS,amount,currency)
    
    return True


def _deduct_money_from_wallet(wallet: Wallet, amount, currency):
    amount_in_base_currency = amount*conversion[currency][wallet.currency]
    wallet.balance -= amount_in_base_currency
    wallet.save()


def _add_money_to_wallet(wallet: Wallet, amount, currency):
    amount_in_base_currency = amount*conversion[currency][wallet.currency]
    wallet.balance += amount_in_base_currency
    wallet.save()


def _create_transaction(transaction_id:str,sender: User, recipient: User, type: TransactionType, status: TransactionStatus, amount, currency):
    
    transaction=Transaction(
        tid=transaction_id,
        type=type,
        sender=sender,
        recipient=recipient,
        amount=amount,
        currency=currency,
        status=status
    )
    transaction.save()


def _generate_transaction_id():
    return uuid.uuid4()