from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    TYPE_CHOICES = {
        'Personal':'personal',
        'Organization':'organization',
    }
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Personal')
    company_name = models.CharField(max_length=120 , null=True , blank=True)
