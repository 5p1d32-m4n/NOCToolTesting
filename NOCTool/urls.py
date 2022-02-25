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
from django.urls import path, include, re_path

# from django_registration.backends.one_step.views import RegistrationView
# from users.forms import (AccountChangeForm,
# AccountCreationForm
#  )

urlpatterns = [
    # django URLs
    path('admin/', admin.site.urls),
    # API and rest related URLs
    path('api/', include('report_builder.api.urls')),
    path('api/', include('account.api.urls')),

]
