from django.db import models



STATUS_CHOICES ={

    ('SINGLE','SINGLE'),
    ('MARRIED','MARRIED'),
} 

class Info(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    date_of_birth = models.CharField(max_length=20 )
    marital_status = models.CharField(choices=STATUS_CHOICES,max_length=10)
    purpose = models.CharField(max_length=50)
    education = models.TextField(max_length=80)
    professional_skills = models.TextField(max_length=80)
    personal_qualities = models.TextField(max_length=80)
    additional_information = models.TextField(max_length=80)
   
    
    def __str__(self):
        return self.name  


# Create your models here.
