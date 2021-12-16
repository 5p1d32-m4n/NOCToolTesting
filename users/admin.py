from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["first_name", "last_name", "employee_number",
                    "username", "email", "is_active", "department", ]
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',                       'first_name', 'last_name', 'employee_number')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
