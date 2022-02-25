import imp
from rest_framework import generics
from account.api.serializers import AccountSerializer, AccountLoginUserSerializer
from account.models import Accounts
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_auth.views import LoginView as RestLoginView
# from rest_framework.authentication import TokenAuthentication


class AccountLoginAPIView(RestLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = AccountLoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validate_dat['account']
        login(request, account)
        return super().post(request, format=None)


class AccountListAPIView(generics.ListAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class AccountDetailAPIView(generics.RetrieveAPIView):
    queryset = Accounts.objects.all()
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)


class AccountCreateAPIView(generics.CreateAPIView):
    queryset = Accounts.objects.all()
    # authentication_classes = (TokenAuthentication,)
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
