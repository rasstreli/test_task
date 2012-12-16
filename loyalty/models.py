from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class LoyaltyProfile(models.Model):
    user_id = models.CharField(primary_key=True, unique=True, max_length=16)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)


