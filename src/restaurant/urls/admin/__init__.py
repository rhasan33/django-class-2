from django.urls import path

from restaurant.views import AdminRestaurantView

urlpatterns = [
    path('create-list', AdminRestaurantView.as_view(), name='restaurant-admin-create-list'),
]
