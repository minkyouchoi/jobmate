# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ✅ 랜딩 페이지
]
