from django.db import models
from django.contrib.auth.models import User
from account.models import Currency

class TransferRequestStatus(models.TextChoices):
        APPROVED='APPROVED','Approved'
        DENIED='DENIED','Denied'
        PENDING='PENDING','Pending'

# Create your models here.
class TransferRequest(models.Model):
    rid=models.CharField(max_length=200)
    source=models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_source',default=None)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_sender')
    recipient=models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_recipient')
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    currency=models.CharField(max_length=5,choices=Currency.choices,default=Currency.USD)
    status=models.CharField(max_length=10,choices=TransferRequestStatus.choices,default=TransferRequestStatus.PENDING)
    datetime=models.DateTimeField(auto_now_add=True)