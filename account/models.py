from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

DEPARTMENTS = (
    ("Indefinido", "Indefinido"),
    ("Tecnico", "Tecnico"),
    ("Servicio al Cliente", "Servicio al Cliente"),
)


class Accounts(AbstractUser):

    username = models.CharField(
        max_length=25, blank=True, null=True, unique=True)
    employee_number = models.PositiveIntegerField(
        validators=[validators.MaxValueValidator(99999)],
        default=0)
    email = models.EmailField(_('email address'), unique=True)
    department = models.CharField(
        max_length=50, choices=DEPARTMENTS, default=DEPARTMENTS[0][0])
    first_name = models.CharField(max_length=25, default='')
    last_name = models.CharField(max_length=25, default='')

    EMAIL_FIELD = ['email']
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'employee_number']

    def __str__(self):
        return "{}: {}".format(self.username, self.department)
