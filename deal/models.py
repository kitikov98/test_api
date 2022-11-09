from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

class DefaultCategory(models.Model):
    CAREOFMYSELF = 'Забота о себе'
    PAYMENT ='Зарплата'
    HEALTH = 'Здоровье и фитнес'
    COFFERESTOURANT ='Кафе и рестораны'
    AUTOMOBILE = 'Машина'
    EDUCATION ='Образование'
    RELAX = 'Отдых и развлечения'
    COMMISSION = 'Платежи, комиссии'
    CLOTHESSTAFF = 'Покупки: одежда, техника'
    FOOD = 'Продукты'
    TRANSPORT = 'Проезд'
    UNKNOWN = 'Своя категория'
    all_defcat = [(CAREOFMYSELF, "Забота о себе"),
                (PAYMENT, "Зарплата"),
                (HEALTH,"Здоровье и фитнес"),
                (COFFERESTOURANT,"Кафе и рестораны"),
                (AUTOMOBILE, "Машина"),
                (EDUCATION, "Образование"),
                (RELAX, "Отдых и развлечения"),
                (COMMISSION, "Платежи, комиссии"),
                (CLOTHESSTAFF, "Покупки: одежда, техника"),
                (FOOD, "Продукты"),
                (TRANSPORT, "Проезд"),
                (UNKNOWN,'Своя категория'),
    ]

    cat_name =models.CharField(choices=all_defcat, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_name


class Transaction(models.Model):
    summ = models.FloatField()
    time = models.DateTimeField(default=datetime.now())
    organisation = models.CharField(max_length=255)
    description = models.TextField(max_length=400)
    category = models.ForeignKey(DefaultCategory, related_name='category', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    user_balance = models.FloatField(null=True, blank=True)

