# jobs/views.py
from django.shortcuts import render
from .models import Job
from django.shortcuts import render, get_object_or_404

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')  # 최신순 정렬
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):  # ✅ 상세 페이지 뷰
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
