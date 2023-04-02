from django.db import models
from django.contrib.auth.models import User
from account.models import Currency


class Wallet(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='wallet')
    balance=models.IntegerField(default=1000)
    currency=models.CharField(max_length=5,choices=Currency.choices)

    def __str__(self) -> str:
        return self.user.username