from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars/')

class Chat(models.Model):
    email = models.EmailField(blank=False)
    text = models.TextField(blank=False, max_length=99)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
