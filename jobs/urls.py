# jobs/urls.py
from django.urls import path
from . import views
from applications.views import applicants_for_job

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),  # ✅ 상세 페이지 URL 추가
    path('create/', views.job_create, name='job_create'),
    path('<int:pk>/edit/', views.job_update, name='job_edit'),
    path('<int:pk>/delete/', views.job_delete, name='job_delete'),
    path('<int:pk>/applicants/', applicants_for_job, name='applicants_for_job'),
    path('mine/', views.my_job_list, name='my_job_list'),  # ✅ 추가!

]
