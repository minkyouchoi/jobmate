from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_company')
        labels = {
            'username': '아이디',
            'email': '이메일 주소',
            'is_company': '기업 계정 여부',
        }
        help_texts = {
            'username': '',
            'email': '',
            'is_company': '체크 시 기업 전용 계정으로 등록됩니다.',
        }
