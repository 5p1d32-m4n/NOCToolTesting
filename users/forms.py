from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'employee_number',
            'department',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'employee_number',
            'department',
        )
