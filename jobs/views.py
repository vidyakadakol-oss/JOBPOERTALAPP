from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer


@api_view(['GET'])
def job_list(request):

    jobs = Job.objects.all()

    search = request.GET.get('search')
    location = request.GET.get('location')

    if search:
        jobs = jobs.filter(title__icontains=search)

    if location:
        jobs = jobs.filter(location__icontains=location)

    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):

    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "Job created successfully",
            "data": serializer.data
        })

    return Response(serializer.errors)