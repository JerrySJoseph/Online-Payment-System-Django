from django.db import models
from django.contrib.auth.models import User
from account.models import Currency


class Wallet(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='wallet')
    balance=models.DecimalField(default=1000,decimal_places=2,max_digits=10)
    currency=models.CharField(max_length=5,choices=Currency.choices,default=Currency.USD)

    def __str__(self) -> str:
        return self.user.username