from django.urls import path
from .views import FoodItemList, FoodItemDetail

urlpatterns = [
    path('food-items/', FoodItemList.as_view(), name='food-items'),
    path('food-items/<int:pk>/', FoodItemDetail.as_view(), name='food-item-detail'),
]