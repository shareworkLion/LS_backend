from django.db import models
from LsApp.models import Post

class FeelPost(models.Model):
    title = Post.title
    body = Post.body