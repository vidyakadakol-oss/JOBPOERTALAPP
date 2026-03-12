from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse("Job Portal Backend Running")


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/', include('users.urls')),
    path('api/', include('jobs.urls')),
    path('api/', include('applications.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]