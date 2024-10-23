from django.urls import path
from users.views import user_login, user_logout, UserRegisterView, RegisterUserAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("register-user/", RegisterUserAPIView.as_view(), name="register-user"),
    
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
