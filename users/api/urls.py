from django.urls import path
from users.api.views import CustomUserListAPIView, CustomUserDetailAPIView, CustomUserCreateAPIView

urlpatterns = [
    path("user/<int:pk>/", CustomUserDetailAPIView.as_view(), name="user-detail"),
    path("user-list/", CustomUserListAPIView.as_view(), name="user-list"),
    path("user-create/", CustomUserCreateAPIView.as_view(), name="user-create"),
]
