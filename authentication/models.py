# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    total_skipTraces = models.IntegerField(blank=True)
    total_orders = models.IntegerField(blank=True)
    total_spent = models.FloatField(blank=True)
    pending_skipTraces = models.IntegerField(blank=True)
    available_skipTraces = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.address}, {self.city}, {self.state}'