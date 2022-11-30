from django.core.validators import MinLengthValidator
from django.db import models

class Customer(models.Model):
    user_login = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50, validators=[MinLengthValidator(6)])

    def __repr__(self):
        return f"{self.user_login} has password {self.user_password}"