from django.urls import path, include

urlpatterns = [
    path('admin/', include('restaurant.urls.admin'), name='restaurant-admin-urls')
]
