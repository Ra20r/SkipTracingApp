# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="history")
    order_number = models.IntegerField(blank=True)
    order_type = models.CharField(max_length=100, blank=True)
    total_address = models.IntegerField(blank=True)
    total_hits = models.IntegerField(blank=True)
    hit_percentage = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.order_number}, {self.order_type}, {self.total_address}'