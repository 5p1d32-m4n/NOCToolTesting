from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import generics
from users.api.serializers import CustomUserSerializer
from users.models import CustomUser
from rest_framework.permissions import IsAuthenticated


class CustomUserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
