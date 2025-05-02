from django.contrib import admin
from .models import UserProfile
from django.contrib.auth import get_user_model

admin.site.register(UserProfile)  # ✅ 관리자에 모델 등록

User = get_user_model()
admin.site.register(User)
