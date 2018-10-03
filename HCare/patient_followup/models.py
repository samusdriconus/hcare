from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/images/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/images/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'patient/{0}'.format(filename)


# Create your models here.
class Patient(models.Model):
    sex_types = (
        ('f', 'Female'),
        ('m', 'Male'),
    )
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    birthplace = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=sex_types)
    address = models.CharField(max_length=128)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=254,default="")
    social_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=image_directory_path,storage=image_storage)
    comment = models.TextField()

    def __str__(self):
        return "[" + self.social_number +"]" + self.name
    

class Appointement(models.Model):
    date = models.DateTimeField(default=datetime.now())
    duration = models.IntegerField(default="15")
    comment = models.TextField()
    patient = models.ForeignKey(Patient, related_name='appointements'
        ,on_delete=models.CASCADE,
    )







