from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from jobs.models import Job
from .models import Application
from .serializers import ApplicationSerializer


# Apply for a job
@api_view(['POST'])
def apply_job(request):
    user_id = request.data.get('user_id')
    job_id = request.data.get('job_id')

    try:
        user = User.objects.get(id=user_id)
        job = Job.objects.get(id=job_id)
    except:
        return Response({"error": "User or Job not found"}, status=404)

    # Check if already applied
    if Application.objects.filter(user=user, job=job).exists():
        return Response({"message": "Already applied for this job"}, status=400)

    application = Application.objects.create(user=user, job=job)

    serializer = ApplicationSerializer(application)

    return Response({
        "message": "Job applied successfully",
        "data": serializer.data
    })


# View all applications (Admin purpose)
@api_view(['GET'])
def view_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


# View applications of a specific user
@api_view(['GET'])
def my_applications(request):
    user_id = request.GET.get('user')

    try:
        user = User.objects.get(id=user_id)
    except:
        return Response({"error": "User not found"}, status=404)

    applications = Application.objects.filter(user=user)
    serializer = ApplicationSerializer(applications, many=True)

    return Response(serializer.data)