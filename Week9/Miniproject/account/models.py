from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    ROLE = [(ADMIN,'Admin'),(CUSTOMER,'Customer'),]
    
    profile_photo = models.ImageField(verbose_name = 'photo de profil')
    role = models.CharField(max_length = 30, choices=ROLE, verbose_name='Rôle')
    

