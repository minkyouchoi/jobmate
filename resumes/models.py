# resumes/models.py
from django.db import models
from accounts.models import UserProfile

# ✅ 사용자 이력서 모델
class UserResume(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')  # ✅ 이력서 파일 업로드
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
