# Generated by Django 4.1.7 on 2023-03-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_wallet_balance_alter_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(choices=[('GBP', 'British Pound'), ('USD', 'United States Dollar'), ('EUR', 'Euro')], max_length=5),
        ),
    ]
