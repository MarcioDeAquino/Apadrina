from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    GENDERS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB', 'Nao-binário')
    ) 
    gender = models.CharField(max_length=2, choices=GENDERS)       
    phone  = models.CharField(max_length=15)


