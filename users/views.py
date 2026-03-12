from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# User Registration API
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if username already exists
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    # Create user
    user = User.objects.create_user(username=username, password=password)

    # Generate token
    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "message": "User created successfully",
        "token": token.key
    })


# User Login API
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successful",
            "token": token.key
        })

    return Response({"error": "Invalid username or password"}, status=400)