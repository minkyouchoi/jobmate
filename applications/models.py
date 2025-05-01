# applications/models.py
from django.db import models
from accounts.models import UserProfile
from jobs.models import Job
from resumes.models import UserResume

# ✅ 채용 지원 모델
class JobApplication(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey(UserResume, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} → {self.job.title}"
