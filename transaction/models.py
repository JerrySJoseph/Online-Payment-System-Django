from django.db import models
from account.models import Currency
from django.contrib.auth.models import User

class TransactionStatus(models.TextChoices):
        SUCCESS='SUCCESS','Success'
        DECLINED='DECLINED','Declined'
        PENDING='PENDING','Pending'

class TransactionType(models.TextChoices):
        DEBIT='DEBIT','Debit'
        CREDIT='CREDIT','Credit'

# Create your models here.
class Transaction(models.Model):
    tid=models.CharField(max_length=200)
    type=models.CharField(max_length=10,choices=TransactionType.choices)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    recipient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='recipient')
    amount=models.IntegerField()
    currency=models.CharField(max_length=5,choices=Currency.choices,default=Currency.USD)
    status=models.CharField(max_length=10,choices=TransactionStatus.choices,default=TransactionStatus.PENDING)
    datetime=models.DateTimeField(auto_now_add=True)