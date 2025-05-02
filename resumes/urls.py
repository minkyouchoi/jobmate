from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.resume_create, name='resume_create'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),  # 상세보기
    path('<int:pk>/edit/', views.resume_update, name='resume_edit'),
    path('<int:pk>/delete/', views.resume_delete, name='resume_delete'),
]
