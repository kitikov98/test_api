from datetime import datetime
from rest_framework import serializers
from .models import Transaction, DefaultCategory
from django.db.models import Sum




class CategoryDefSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DefaultCategory
        fields = ('cat_name', 'user',)

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cat_name = serializers.CharField(min_length=1)

    class Meta:
        model = DefaultCategory
        fields = ('cat_name', 'user',)

class TransactionSerializer(serializers.ModelSerializer):
    # username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username = serializers.ReadOnlyField(source='username.username')
    user_email = serializers.ReadOnlyField(source='username.email')
    user_email = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Transaction
        fields = ('category', 'summ', 'organisation', 'description', 'time', 'username', 'user_email')

class UserBSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1)
    # username = serializers.ReadOnlyField(source='username.username')
    user_balance = serializers.SerializerMethodField()
    time = serializers.DateTimeField(default=datetime.now())
    user_email = serializers.ReadOnlyField(source='username.email')
    # user_email = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_user_balance(self, obj):
        transaction = Transaction.objects.all()
        user_balance = transaction.aggregate(Sum('summ'))['summ__sum']
        return user_balance
