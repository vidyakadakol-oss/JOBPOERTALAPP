from django.urls import path
from .views import job_list, create_job

urlpatterns = [
    path('jobs/', job_list),
    path('create-job/', create_job),
]