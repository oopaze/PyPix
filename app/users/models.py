from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField("email", blank=True)
    phone = models.CharField("Telefone", max_length=20)

    REQUIRED_FIELDS = ["phone"]
