from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import User

class UserChangeForm(UserChangeForm):
    password = None        
    picture = forms.CharField(label='사진', widget=forms.TextInput(
        attrs={'class': 'form-control',}), 
    )        
    gallery_name = forms.CharField(label='갤러리 이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'50', 'oninput':"maxLengthCheck(this)",}), 
    )        
    nickname = forms.CharField(label='닉네임', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8', 'oninput':"maxLengthCheck(this)",}), 
    )
    motto = forms.CharField( label='한 줄 모토', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'100', 'oninput':"maxLengthCheck(this)",}), 
    )
    
    class Meta:
        model = User
        fields = ['picture', 'gallery_name', 'nickname', 'motto', 'user_id']
