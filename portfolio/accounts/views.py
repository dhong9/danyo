from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from portfolio.accounts.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def update(self, request, *args, **kwargs):
        data_to_change = {
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'password': request.data.get('password')
        }
        # Partial update of the data
        serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

        return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/update/'
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'PUT'])
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
    return Response({}, status.HTTP_400_BAD_REQUEST)