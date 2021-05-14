# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, default="NULL")
    city = models.CharField(max_length=100, blank=True, default="NULL")
    state = models.CharField(max_length=100, blank=True, default="NULL")
    zip_code = models.CharField(max_length=100, blank=True, default="NULL")
    phone = models.CharField(max_length=100, blank=True, default="NULL")
    total_skipTraces = models.IntegerField(blank=True, default=0)
    total_orders = models.IntegerField(blank=True, default=0)
    total_spent = models.FloatField(blank=True, default=0.0)
    pending_skipTraces = models.IntegerField(blank=True, default=0)
    available_skipTraces = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.address}, {self.total_orders}, {self.total_spent}'