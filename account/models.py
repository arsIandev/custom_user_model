from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from . import managers


class User(AbstractUser):
    first_name = last_name = username = None
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = managers.UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self) -> str:
        return self.name
    