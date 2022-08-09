from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.Auth_USER_MODEL)
    nickname = models.CharField(max_length=10)
    profile_photo = models.ImageField(blank=True)
    gallery_name = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)