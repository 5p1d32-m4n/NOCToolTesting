from django.contrib import admin
from django.urls import include
from django.urls import path
from .views import (AccountCreateAPIView,
                    AccountDetailAPIView, AccountListAPIView, AccountLoginAPIView)
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    #     path("auth/login/", AccountLoginAPIView.as_view(), name='account-login'),
    path("auth/", include('dj_rest_auth.urls')),
    path("account-list/", AccountListAPIView.as_view(), name='account-list'),
    path('account-create/', AccountCreateAPIView.as_view(), name='account-create'),
    path("account/<str:pk>/", AccountDetailAPIView.as_view(), name='account-detail'),
    path('auth/token/obtain/',
         jwt_views.TokenObtainPairView.as_view(), name='token_access'),
    path('auth/token/refresh/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
