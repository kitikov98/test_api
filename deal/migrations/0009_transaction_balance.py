# Generated by Django 4.1.3 on 2022-11-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0008_remove_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]