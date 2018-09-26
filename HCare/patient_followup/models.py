from django.db import models

# Create your models here.
class Patient(models.Model):
    sex_types = (
        ('f', 'Female'),
        ('m', 'Male'),
    )
    id = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField(auto_now_add=True)
    birthplace = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=sex_types)
    address = models.CharField(max_length=128)
    phone= models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    social_number = models.CharField(max_length=20)
    picture = models.ImageField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return "[" + self.social_number +"]" + self.name
    




