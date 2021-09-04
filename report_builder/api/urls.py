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


urlpatterns = [
    path('report-create/', rv.ReportCreateAPIView.as_view(),
         name='report-create'),
    path('report-detail/<str:pk>/',
         rv.ReportDetailAPIView.as_view(), name='report-detail'),
    path('report-list/', rv.ReportListAPIView.as_view(), name='report-list'),
    path('report-update-list/',
         rv.ReportUpdateListAPIView.as_view(), name='report-update-list'),
    path('report-update/<str:pk>/',
         rv.ReportUpdateAPIView.as_view(), name='report-update'),
    path('services-create/', rv.ServicesCreateAPIView.as_view(),
         name='services-create'),
    path('services-detail/<str:pk>/',
         rv.ServicesDetailAPIView.as_view(), name='services-detail'),
    path('services-list/', rv.ServicesListAPIView.as_view(), name='services-list'),
    path('services-update-list/',
         rv.ServicesUpdateListAPIView.as_view(), name='services-update-list'),
    path('services-update/<str:pk>/',
         rv.ServicesUpdateAPIView.as_view(), name='services-update'),
    path('clients-create/', rv.ClientsCreateAPIView.as_view(),
         name='clients-create'),
    path('clients-detail/<str:pk>/',
         rv.ClientsDetailAPIView.as_view(), name='clients-detail'),
    path('clients-list/', rv.ClientsListAPIView.as_view(), name='clients-list'),
    path('clients-update-list/',
         rv.ClientsUpdateListAPIView.as_view(), name='clients-update-list'),
    path('clients-update/<str:pk>/',
         rv.ClientsUpdateAPIView.as_view(), name='clients-update'),
    path('outage_type-create/', rv.OutageTypeCreateAPIView.as_view(),
         name='outage_type-create'),
    path('outage_type-detail/<str:pk>/',
         rv.OutageTypeDetailAPIView.as_view(), name='outage_type-detail'),
    path('outage_type-list/', rv.OutageTypeListAPIView.as_view(),
         name='outage_type-list'),
    path('outage_type-update-list/',
         rv.OutageTypeUpdateListAPIView.as_view(), name='outage_type-update-list'),
    path('outage_type-update/<str:pk>/',
         rv.OutageTypeUpdateAPIView.as_view(), name='outage_type-update'),
    path('cause-create/', rv.CauseCreateAPIView.as_view(),
         name='cause-create'),
    path('cause-detail/<str:pk>/',
         rv.CauseDetailAPIView.as_view(), name='cause-detail'),
    path('cause-list/', rv.CauseListAPIView.as_view(), name='cause-list'),
    path('cause-update-list/',
         rv.CauseUpdateListAPIView.as_view(), name='cause-update-list'),
    path('cause-update/<str:pk>/',
         rv.CauseUpdateAPIView.as_view(), name='cause-update'),
]
