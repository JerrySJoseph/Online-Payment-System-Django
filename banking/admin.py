from django.contrib import admin

# Register your models here.
from .models import TransferRequest

admin.site.register(TransferRequest)