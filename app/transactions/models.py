from uuid import uuid4
from django.db import models


class Key(models.Model):
    EMAIL = "email"
    PHONE = "phone"
    CPF = "cpf"
    RANDOM = "random"

    TYPES = ((EMAIL, "Email"), (PHONE, "Telefone"), (CPF, "CPF"), (RANDOM, "Aleatória"))

    type = models.CharField("Tipo", max_length=10, choices=TYPES)
    key = models.CharField("Chave", max_length=100, unique=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="keys"
    )


class Transction(models.Model):
    value = models.DecimalField("Valor", max_digits=20, decimal_places=2)
    sender = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        "Key", on_delete=models.CASCADE, related_name="receiver"
    )

    send_at = models.DateField("Enviado em", auto_now_add=True)
