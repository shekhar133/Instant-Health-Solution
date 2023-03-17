from email.headerregistry import Address
from email.policy import default
from statistics import mode
from django.db import models
from PIL import Image
# Create your models here.

class Gujarat_hospital(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    link = models.CharField(max_length=100,default ="#")
    img = models.ImageField(default = 'default.jpg',upload_to = 'gujarat_hospital')
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.title+f"city: {self.city}"

class Gujarat_Ngo(models.Model):
    title = models.CharField(max_length=100,default ="Ngo")
    content = models.TextField(default ="Ngo")
    address = models.CharField(max_length=100,default ="India")
    phone_number = models.CharField(max_length=20,default ="123")
    link = models.CharField(max_length=100,default ="#")
    img = models.ImageField(default = 'default.jpg',upload_to = 'gujarat_Ngo')
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.title+f"city: {self.city}"

class Appointment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    request = models.TextField(blank = True)
    sent_date = models.DateField(auto_now_add= True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-sent_date']