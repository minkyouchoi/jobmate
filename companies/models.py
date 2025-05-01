# companies/models.py
from django.db import models

# ✅ 기업 정보 모델
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
