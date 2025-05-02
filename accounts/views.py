from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from jobs.models import Job
from resumes.models import Resume
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@login_required
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    user = request.user

    try:
        user_profile = user.userprofile  # ✅ 이제 import 없이 접근 가능
    except:
        raise PermissionDenied("프로필이 없습니다.")  # 혹시라도 진짜 없는 예외 케이스 처리

    # 이미 지원했는지 확인
    if JobApplication.objects.filter(user_profile=user_profile, job=job).exists():
        return redirect('jobs:job_detail', pk=job.pk)

    resume = Resume.objects.filter(user=user).order_by('-created_at').first()
    if not resume:
        raise PermissionDenied("등록된 이력서가 없습니다.")

    JobApplication.objects.create(
        user_profile=user_profile,
        job=job,
        resume=resume
    )
    return redirect('jobs:job_detail', pk=job.pk)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 또는 'home', 원하는 곳
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})