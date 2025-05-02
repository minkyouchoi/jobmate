from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('jobs/<int:pk>/apply/', views.apply_to_job, name='apply'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('jobs/<int:pk>/applicants/', views.applicants_for_job, name='applicants_for_job'),
]
