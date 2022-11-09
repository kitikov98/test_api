from rest_framework import viewsets, filters, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView,CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .models import Transaction, DefaultCategory
from .serializer import TransactionSerializer, CategoryDefSerializer, CategorySerializer, UserBSerializer
from .task import send_email


class CategoryView(ListCreateAPIView):
    serializer_class = CategoryDefSerializer
    queryset = DefaultCategory.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
    #Для проверки не забудь убрать
    authentication_classes = (TokenAuthentication, )

class SingleCategoryView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = DefaultCategory.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['summ', 'time']

    # Для проверки не забудь убрать
    authentication_classes = (TokenAuthentication, )

class UserBView(APIView):
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication, )
    def get(self, requset):
        transaction = Transaction.objects.all()
        serializer = UserBSerializer(transaction, many=True)
        return Response(serializer.data[-1])



class SendStatisticView(CreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication, )
    serializer_class = UserBSerializer
    queryset = Transaction.objects.all()


    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = UserBSerializer(transaction, many=True)
        user_name = serializer.data[-1]['username']
        email_adr = serializer.data[-1]['user_email']
        user_balance = serializer.data[-1]['user_balance']
        send_email.delay(user_name, email_adr, user_balance)
        return Response(serializer.data[-1], status=status.HTTP_201_CREATED)

