from django.db import models
from cars.models import Car
from django.contrib.auth.models import User
# Create your models here.

class Own(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, unique=True)