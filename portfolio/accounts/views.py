from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from portfolio.accounts.serializer import MyTokenObtainPairSerializer, RegisterSerializer, ProfileSerializer
from portfolio.accounts.models import Profile
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, viewsets

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/update/',
        '/api/delete/',
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulations {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulations your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        text = request.PUT.get('text')
        data = f'Congratulations your API just responded to PUT request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        text = request.DELETE.get('text')
        data = f'Congratulations your API just responded to DELETE request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)