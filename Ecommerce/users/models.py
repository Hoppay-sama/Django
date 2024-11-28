from django.db import models
from django.contrib.auth.hashers import check_password


# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    terms_and_conditions = models.BooleanField(default=False)

    def check_password(self, password):
        return check_password(password, self.password)

# class User(models.Model):