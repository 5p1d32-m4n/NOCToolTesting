from unicodedata import name
from django.urls import path

from users.api.views import Dummy
# from users.api.views import AccountListAPIView, AccountDetailAPIView, AccountCreateAPIView

urlpatterns = [
    # path("user/<int:pk>/", AccountDetailAPIView.as_view(), name="user-detail"),
    # path("user-list/", AccountListAPIView.as_view(), name="user-list"),
    # path("user-create/", AccountCreateAPIView.as_view(), name="user-create"),
    path('dummy', Dummy.as_view(), name='dummy'),
]
