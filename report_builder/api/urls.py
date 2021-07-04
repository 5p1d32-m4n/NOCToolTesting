"""NOCTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from report_builder.api import views as rv


# router = DefaultRouter()
# router.register(r"reports", rv.ReportViewSet)

urlpatterns = [
    path('report-create/', rv.ReportCreateAPIView.as_view(),
         name='report-create'),
    path('report-detail/<str:pk>/',
         rv.ReportDetailAPIView.as_view(), name='report-detail'),
    path('report-list/', rv.ReportListAPIView.as_view(), name='report-list'),
    path('report-update-list/',
         rv.ReportUpdateListAPIView.as_view(), name='report-update-list'),
    path('report-update/<str:pk>/',
         rv.ReportUpdateAPIView.as_view(), name='report-update')
]
