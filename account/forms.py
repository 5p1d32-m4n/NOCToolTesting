from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Accounts


class AccountCreationForm(UserCreationForm):

    class Meta():
        model = Accounts
        fields = '__all__'


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Accounts
        fields = '__all__'
