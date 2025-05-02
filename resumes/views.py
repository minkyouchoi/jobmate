# resumes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm
from django.contrib.auth.decorators import login_required, user_passes_test

# 일반 사용자만 접근 허용
def is_user(user):
    return user.is_authenticated and not user.is_company

@login_required
@user_passes_test(is_user)
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

@login_required
@user_passes_test(is_user)
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resumes:resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_form.html', {'form': form})

from django.core.exceptions import PermissionDenied

@login_required
@user_passes_test(is_user)
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resumes/resume_detail.html', {'resume': resume})


@login_required
@user_passes_test(is_user)
def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk)

    if resume.user != request.user:
        raise PermissionDenied("수정 권한이 없습니다.")

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resumes:resume_detail', pk=resume.pk)
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'resumes/resume_form.html', {'form': form})


@login_required
@user_passes_test(is_user)
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)

    if resume.user != request.user:
        raise PermissionDenied("삭제 권한이 없습니다.")

    if request.method == 'POST':
        resume.delete()
        return redirect('resumes:resume_list')

    return render(request, 'resumes/resume_confirm_delete.html', {'resume': resume})

