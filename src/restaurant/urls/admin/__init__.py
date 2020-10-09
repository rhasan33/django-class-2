from django.urls import path

from restaurant.views import AdminDRFRestaurantView, AdminRestaurantGetUpdateDestroyView

urlpatterns = [
    path('', AdminDRFRestaurantView.as_view(), name='restaurant-admin-create-list'),
    path('/<int:pk>', AdminRestaurantGetUpdateDestroyView.as_view(), name='restaurant-admin-get-update'),
]
