from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.Integer(unique=True)
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField(auto_now_add=True)
    birthplace = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=128)
    phone= models.CharField(max_length=13)
    social_number = models.CharField(max_length=20)
    picture = models.ImageField(max_length=100)