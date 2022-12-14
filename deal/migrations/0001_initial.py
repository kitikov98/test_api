# Generated by Django 4.1.3 on 2022-11-05 10:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ', models.FloatField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('organisation', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='deal.category')),
            ],
        ),
    ]
