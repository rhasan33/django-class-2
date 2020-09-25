from django.urls import path

from restaurant.views import AdminRestaurantView, AdminDRFRestaurantView

urlpatterns = [
    path('create-list', AdminDRFRestaurantView.as_view(), name='restaurant-admin-create-list'),
]
