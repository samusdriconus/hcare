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


documents_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/documents/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}/documents/'.format(settings.MEDIA_URL),
)


def document_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'exams/{0}'.format(filename)





# Create your models here.
class Patient(models.Model):
    genders = (
        ('f', 'Female'),
        ('m', 'Male'),
    )
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    birthplace = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=genders)
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
    note = models.TextField()
    patient = models.ForeignKey(Patient, related_name='appointements'
        ,on_delete=models.PROTECT,
    )

    def __str__(self):
        return "[" + str(self.date) + "]" + self.patient.name
    




class Disease(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return "[" + self.code + "] " + self.name
    


class MedicalExam(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField(default = datetime.now())
    appointement = models.ForeignKey(Appointement,on_delete=models.CASCADE)
    diagnostic = models.TextField()


    def __str__(self):
        return self.name
    



class Document(models.Model):
    name = models.CharField(max_length=256)
    content = models.FileField(upload_to=document_directory_path,storage=documents_storage)
    exam = models.ForeignKey(MedicalExam, related_name="documents", 
         on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    

    






    












