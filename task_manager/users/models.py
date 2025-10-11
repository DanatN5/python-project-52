from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    password1 = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "username"


    def __str__(self):
        return self.username