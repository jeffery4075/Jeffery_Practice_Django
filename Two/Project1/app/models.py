from django.db import models

class Profile(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=100)
    city  = models.CharField(max_length=100)

