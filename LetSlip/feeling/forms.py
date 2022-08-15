from django import forms
from .models import FeelPost
from dataclasses import field

class FeelPostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.', }))

    class Meta:
        model = FeelPost
        fields = ['body']