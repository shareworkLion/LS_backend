from django.db import models
from django.contrib.auth.models import AbstractUser

# # 타유저 팔로우 위한 모델
# class FollowUser(AbstractUser):
#     followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

#     class Meta(AbstractUser.Meta):
#         swappable = 'AUTH_USER_MODEL'