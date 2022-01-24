from django.db import models




class Info(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    image =models.ImageField(upload_to='images/')
    date_of_birth = models.CharField(max_length=20)
    purpose = models.CharField(max_length=50)
    education = models.CharField(max_length=80)
    professional_skills = models.TextField(max_length=80)
    personal_qualities = models.CharField(max_length=80)
    additional_information = models.CharField(max_length=80)
   
    
    def __str__(self):
        return self.name  


# Create your models here.
