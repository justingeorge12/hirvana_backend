

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import  TokenRefreshView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('register', RegisterUserView.as_view(), name='register'),
]

