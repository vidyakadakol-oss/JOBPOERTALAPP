from django.urls import path
from .views import apply_job, view_applications, my_applications

urlpatterns = [
    path('apply/', apply_job),
    path('applications/', view_applications),
    path('my-applications/', my_applications),
]