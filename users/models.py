from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('Você não informou um endereço de e-mail'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('O superusuário deve ser atribuído com is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('O superusuário deve ser atribuído com is_superuser=True')

        return self.create_user(email, username, first_name, password, **other_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    username = models.CharField(_('Usuário'), max_length=150, unique=True)
    first_name = models.CharField(_('Primeiro nome'), max_length=150, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('Sobre'), max_length=500, blank=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_active = models.BooleanField(_('Ativo'), default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email
