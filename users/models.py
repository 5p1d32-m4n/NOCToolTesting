from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


DEPARTMENTS = (
    ("Indefinido", "Indefinido"),
    ("Tecnico", "Tecnico"),
    ("Servicio al Cliente", "Servicio al Cliente"),
)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=25, default='')
    last_name = models.CharField(max_length=25, default='')
    username = models.CharField(max_length=10, default='', unique=True)
    employee_number = models.PositiveIntegerField(
        primary_key=True, validators=[validators.MaxValueValidator(99999)],
        default=0)
    department = models.CharField(
        max_length=50, choices=DEPARTMENTS, default=DEPARTMENTS[0][0])
