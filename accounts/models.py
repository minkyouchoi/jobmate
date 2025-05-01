# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

# ✅ 사용자 추가 정보
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
