from django.db import models

# Create your models here.
class Client(models.Model):
    Name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=100)
    Location = models.CharField(max_length=100)
