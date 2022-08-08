from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, user_id, picture, gallery_name, nickname, motto, password=None):
        if not user_id:
            raise ValueError('아이디를 입력해 주세요.')

        user = self.model(
            user_id = user_id,
            picture = picture,
            gallery_name = gallery_name,
            nickname = nickname,
            motto = motto,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id
    
    picture = models.CharField()
    gallery_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=8)
    motto = models.CharField(max_length=100)

    def __str__(self):
        return self.picture
    def __str__(self):
        return self.gallery_name
    def __str__(self):
        return self.nickname
    def __str__(self):
        return self.motto