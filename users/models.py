from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db.models.expressions import F


DEPARTMENTS = (
    ("Indefinido", "Indefinido"),
    ("Tecnico", "Tecnico"),
    ("Servicio al Cliente", "Servicio al Cliente"),
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager
    """

    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field is required !'))
        if not username:
            raise ValueError(_("The Username field is required !"))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=25, default='')
    last_name = models.CharField(max_length=25, default='')
    username = models.CharField(max_length=10, default='', unique=True)
    employee_number = models.PositiveIntegerField(
        primary_key=True, validators=[validators.MaxValueValidator(99999)],
        default=0)
    department = models.CharField(
        max_length=50, choices=DEPARTMENTS, default=DEPARTMENTS[0][0])
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username 
