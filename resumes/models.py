# resumes/models.py
from django.db import models
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ 작성자
    name = models.CharField(max_length=100, default='이름없음')                    # ✅ 공백 불가
    phone = models.CharField(max_length=20, default='010-0000-0000')              # ✅ 공백 불가
    email = models.EmailField(default='temp@example.com')                         # ✅ 공백 불가

    education = models.TextField(blank=True)   # ⭕ 선택 가능
    show_education = models.BooleanField(default=True)  # ✅ 학력 공개 여부

    experience = models.TextField(blank=True)  # ⭕ 선택 가능

    CAREER_CHOICES = [
        ('신입', '신입'),
        ('1-2년차', '1-2년차'),
        ('3-5년차', '3-5년차'),
        ('5-10년차', '5-10년차'),
        ('10년 이상', '10년 이상'),
    ]
    career_level = models.CharField(max_length=20, choices=CAREER_CHOICES, default='신입')  # ✅ 경력 그레이드

    preferred_location = models.CharField(max_length=50, blank=True)  # ✅ 희망 근무지역

    EMPLOYMENT_CHOICES = [
        ('정규직', '정규직'),
        ('계약직', '계약직'),
        ('프리랜서', '프리랜서'),
        ('인턴', '인턴'),
        ('기타', '기타'),
    ]
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, default='정규직')  # ✅ 근무 형태

    skills = models.CharField(
        max_length=200,
        blank=True,
        help_text='쉼표로 구분하여 입력 (예: Python, Django, HTML)'
    )
    skills_detail = models.TextField(blank=True)  # ✅ 기술 상세 설명

    bio = models.TextField(blank=True)            # ⭕ 선택 가능 (자기소개)

    portfolio = models.FileField(
        upload_to='resumes/portfolios/',
        blank=True,
        null=True
    )  # ✅ 첨부파일

    portfolio_link = models.URLField(blank=True, null=True)  # ✅ 외부 포트폴리오 링크

    created_at = models.DateTimeField(auto_now_add=True)  # 생성일 자동 저장

    def __str__(self):
        return f"{self.name} - {self.user.username}"
