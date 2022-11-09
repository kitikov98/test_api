from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path

from .views import TransactionView, CategoryView, SingleCategoryView, UserBView, SendStatisticView

router = DefaultRouter()
router.register(r'transactions', TransactionView, basename='Transactions')
# router.register(r'category', CategoryView, basename='Category')

urlpatterns = [
    path('category/', CategoryView.as_view()),
    # path('transactions/', TransactionView.as_view()),
    path('userb/', UserBView.as_view()),
    path('sendstat/', SendStatisticView.as_view()),
    path('category/<int:pk>/', SingleCategoryView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + router.urls


