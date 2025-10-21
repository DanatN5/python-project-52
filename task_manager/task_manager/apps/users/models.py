from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username