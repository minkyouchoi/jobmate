# jobs/views.py
from django.shortcuts import render
from .models import Job
from django.shortcuts import render, get_object_or_404
from .forms import JobForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')  # 최신순 정렬
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    has_applied = False
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
            has_applied = job.applications.filter(user_profile=user_profile).exists()
        except:
            pass  # userprofile 없을 경우는 지원 안 한 걸로 간주

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied
    })

def is_company(user):
    return user.is_authenticated and user.is_company

@login_required
@user_passes_test(is_company, login_url='login')
def job_create(request):
    if not request.user.is_company:
        raise PermissionDenied("기업 계정만 접근할 수 있습니다.")

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)  # ✅ 저장 보류
            job.author = request.user      # ✅ 로그인한 기업 계정을 author로 설정
            job.save()
            return redirect('jobs:job_list')  # ✅ 저장 후 리디렉션
    else:
        form = JobForm()

    return render(request, 'jobs/job_form.html', {'form': form})  # ✅ GET 요청 또는 유효성 오류 시 폼 다시 렌더링


@login_required
@user_passes_test(is_company, login_url='login')
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.author:
        raise PermissionDenied("수정 권한이 없습니다.")

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_detail', pk=job.pk)
        else:
            print("❌ 폼 에러 발생:", form.errors)  # ← 여기서 오류 원인 확인 가능!
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/job_update.html', {'form': form})

@login_required
@user_passes_test(is_company, login_url='login')
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.author:
        raise PermissionDenied("삭제 권한이 없습니다.")
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})


@login_required
@user_passes_test(is_company)
def my_job_list(request):
    jobs = Job.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'jobs/my_job_list.html', {'jobs': jobs})
