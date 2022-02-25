# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.base import TemplateView
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics
# from users.api.serializers import AccountSerializer
# from users.models import Account
# from rest_framework.permissions import IsAuthenticated


# class AccountListAPIView(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


# class AccountDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer


# class AccountCreateAPIView(generics.CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

class Dummy(generics.RetrieveAPIView):
    pass
