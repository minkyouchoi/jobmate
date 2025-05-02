# jobs/models.py
from django.db import models
from companies.models import Company
from django.conf import settings

# ✅ 채용 공고 모델
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', '정규직'),
        ('PT', '파트타임'),
        ('CT', '계약직'),
        ('FR', '프리랜서'),
        ('IN', '인턴'),
    ]

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100, default='미입력 회사')
    location = models.CharField(max_length=100, blank=True)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES, default='FT')
    salary = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    skills = models.CharField(max_length=200, blank=True, help_text='예: Python, Django')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
