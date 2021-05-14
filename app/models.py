# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="history")
    order_number = models.IntegerField(blank=True, default=0)
    order_type = models.CharField(max_length=100, blank=True, default="NULL")
    total_address = models.IntegerField(blank=True, default=0)
    total_hits = models.IntegerField(blank=True, default=0)
    hit_percentage = models.CharField(max_length=100, blank=True, default="0%")
    date = models.CharField(max_length=100, blank=True, default="xx/xx/xxxx")
    status = models.CharField(max_length=100, blank=True, default="NULL")

    def __str__(self):
        return f'{self.order_number}, {self.order_type}, {self.total_address}, {self.hit_percentage}'