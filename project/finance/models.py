from django.db import models

# Create your models here.
from django.db import models

class Farmer(models.Model):
    full_name    = models.CharField(max_length=120)
    age          = models.CharField(max_length=5)
    gender       = models.CharField(max_length=5)
    address      = models.CharField(max_length=5)

    def __str__(self):
        return self.full_name


class Investor(models.Model):
    full_name    = models.CharField(max_length=120)
    age          = models.CharField(max_length=5)
    gender       = models.CharField(max_length=5)
    address      = models.CharField(max_length=5)

    def __str__(self):
        return self.full_name


class Land(models.Model):
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField(max_length=20)
    share_quantity  = models.IntegerField(max_length=20)
    fertility_rate  = models.IntegerField(max_length=20)

    def __str__(self):
        return self.location
