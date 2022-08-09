from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tkinter import CASCADE

# class User(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user

class Profile(models.Model):
    nickname = models.CharField(max_length=10)
    profile_photo = models.ImageField(blank=True)
    gallery_name = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname

    def __str__(self):
        return self.profile_photo

    def __str__(self):
        return self.gallery_name

    def __str__(self):
        return self.motto