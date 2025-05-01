from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)  # ✅ 관리자에 모델 등록
