from ..models import Transaction
from django.db.models import Q
from django.contrib.auth.models import User
from transaction.models import TransactionType, TransactionStatus
import uuid


def get_transactions_by_id_qs(user_id:int)->list:
    return list(get_transactions_by_id(user_id))

def get_transactions_by_id(user_id:int)->list:
    transactions=Transaction.objects.filter(
        Q(source__exact=user_id)
    )
    return transactions.all()



def create_transaction(transaction_id:str,source:User,sender: User, recipient: User, type: TransactionType, status: TransactionStatus, amount, currency,balance):
    
    transaction=Transaction(
        tid=transaction_id,
        source=source,
        type=type,
        sender=sender,
        recipient=recipient,
        amount=amount,
        currency=currency,
        status=status,
        balance=balance
    )
    transaction.save()


def _generate_transaction_id():
    return uuid.uuid4()