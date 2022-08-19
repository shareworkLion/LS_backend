from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import re
from django.utils import timezone


category_select = (
    ('취업', '취업'),
    ('직장', '직장'),
    ('공부', '공부'),
    ('학교', '학교'),
    ('시험', '시험'),
    ('알바', '알바'),
    ('일상', '일상'),
    ('관계', '관계'),
    ('웃긴', '웃긴'),
    ('여행', '여행'),
    ('취미', '취미'),
    ('기타', '기타'),
)


class Category(models.Model):
    category_content = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_content

   
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    category = models.CharField(max_length=20, choices=category_select)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.body
         
class Comment(models.Model):
    comment_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
class CommentReply(models.Model):
    comment_reply = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment_reply_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
        

# 오늘 게시된 게시물 
class Count(models.Model):
    counts = models.PositiveIntegerField(verbose_name='오늘 올라온 실수들', null=True)