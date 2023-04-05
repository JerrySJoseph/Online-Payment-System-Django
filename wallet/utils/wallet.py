from ..models import Wallet
from .exceptions.TransactionException import TransferException
import decimal
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

def deduct_money_from_wallet(wallet: Wallet, amount:decimal.Decimal, currency):
    amount_in_base_currency = amount*decimal.Decimal(conversion[currency][wallet.currency])
    wallet.balance -= decimal.Decimal(amount_in_base_currency)
    wallet.save()
    return wallet.balance


def add_money_to_wallet(wallet: Wallet, amount:decimal.Decimal, currency):
    amount_in_base_currency = amount*decimal.Decimal(conversion[currency][wallet.currency])
    wallet.balance += decimal.Decimal(amount_in_base_currency)
    wallet.save()
    return wallet.balance

def balance_check(sender_id, amount:decimal.Decimal, currency):
    sender_wallet = Wallet.objects.get(user_id=sender_id)
    sender_balance = sender_wallet.balance * decimal.Decimal(conversion[sender_wallet.currency][currency])
    required_balance = amount*decimal.Decimal(conversion[currency][sender_wallet.currency])

    if amount > sender_balance:
        raise TransferException(
            f'Insufficient funds: You require {required_balance} in {sender_wallet.currency} to proceed with this transaction.')
    return {
        'balance': sender_balance-required_balance,
        'currency': sender_wallet.currency,
        'success': True
    }
