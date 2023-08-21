from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name=""),
    path("jwt/refresh/", CustomTokenRefreshView.as_view(), name=""),
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name=""),
    path("logout/", LogoutView.as_view(), name=""),
]
