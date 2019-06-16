from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    GENDERS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Nao-binario')
    ) 
    gender = models.CharField(max_length=2, choices=GENDERS)       
    phone  = models.CharField(max_length=15)
    description  = models.TextField(max_length=500)


