# Generated by Django 4.1.7 on 2023-03-31 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_alter_transaction_recipient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='base_currency',
            new_name='currency',
        ),
    ]
