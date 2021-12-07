from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form
    # form
    model = CustomUser
    list_display = ["first_name", "last_name", "employee_number",
                    "username", "email", "is_active", "department", ]


admin.site.register(CustomUser, CustomUserAdmin)
