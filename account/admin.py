from tabnanny import verbose
import django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from account.models import Accounts
from django.contrib.auth.forms import UserChangeForm
from .forms import AccountChangeForm
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {
         'fields': ('employee_number', 'department')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'department', 'email', 'first_name', 'last_name',
                    'is_staff',  "employee_number"]
    search_fields = ('email', 'first_name', 'last_name',
                     'employee_number', 'username')
    ordering = ('email', )


admin.site.register(Accounts, AccountAdmin)
