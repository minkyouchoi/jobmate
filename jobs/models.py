# jobs/models.py
from django.db import models
from companies.models import Company

# ✅ 채용 공고 모델
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='job_files/', blank=True, null=True)  # ✅ 공고 첨부파일

    def __str__(self):
        return self.title
