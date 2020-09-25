from django.urls import path

from user.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='user-login-view'),
]
