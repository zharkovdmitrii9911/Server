from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField('Номер телефона', max_length=20)


