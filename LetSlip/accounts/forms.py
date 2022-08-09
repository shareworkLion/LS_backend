from dataclasses import field
from django import forms
from LetSlip.accounts.models import User
from .models import Profile

 # 유저 정보만 담는 폼
class UserForm(forms.ModelForm):
    nickname = forms.CharField(label='닉네임')
    class Meta:
        model = User
        fields = ['nickname']

# 본인 slip 페이지
class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(label='프로필 사진', required=False)
    gallery_name = forms.CharField(label='갤러리 이름')
    motto = forms.CharField(label='한 줄 모토')
    class Meta:
        model = Profile
        fields = ['profile_photo', 'gallery_name', 'motto']