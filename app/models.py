# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, blank=True)
    phone = models.IntegerField()
