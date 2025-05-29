from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)
    username = models.CharField(_('Usuário'), max_length=150, unique=True)

    #USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
