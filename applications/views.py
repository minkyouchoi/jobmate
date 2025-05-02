from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from jobs.models import Job
from resumes.models import Resume
from .models import JobApplication

@login_required
def apply_to_job(request, pk):
    from accounts.models import UserProfile  # ✅ 함수 내부에서 import로 순환 참조 방지

    job = get_object_or_404(Job, pk=pk)
    user = request.user

    # ✅ UserProfile 없으면 생성 (한 번만 생성됨)
    user_profile, _ = UserProfile.objects.get_or_create(user=user)

    # ✅ 이미 지원했는지 확인
    if JobApplication.objects.filter(user_profile=user_profile, job=job).exists():
        return redirect('jobs:job_detail', pk=job.pk)

    # ✅ 최신 이력서 1개 선택
    resume = Resume.objects.filter(user=user).order_by('-created_at').first()
    if not resume:
        raise PermissionDenied("등록된 이력서가 없습니다.")

    # ✅ 지원 정보 생성
    JobApplication.objects.create(
        user_profile=user_profile,
        job=job,
        resume=resume
    )

    return redirect('jobs:job_detail', pk=job.pk)

@login_required
def my_applications(request):
    user_profile = request.user.userprofile
    applications = JobApplication.objects.filter(user_profile=user_profile).select_related('job').order_by('-applied_at')
    return render(request, 'applications/my_applications.html', {'applications': applications})

def is_company(user):
    return user.is_authenticated and user.is_company

@user_passes_test(is_company)
def applicants_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk, author=request.user)
    applications = job.applications.select_related('user_profile__user', 'resume').order_by('-applied_at')
    return render(request, 'applications/applicants_for_job.html', {
        'job': job,
        'applications': applications,
    })
    
@user_passes_test(is_company)
def applicants_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk, author=request.user)
    applications = job.applications.select_related('user_profile__user', 'resume').order_by('-applied_at')
    return render(request, 'applications/applicants_for_job.html', {
        'job': job,
        'applications': applications,
    })