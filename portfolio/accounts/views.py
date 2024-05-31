from portfolio.accounts.serializer import ProfileSerializer
from portfolio.accounts.models import Profile
from rest_framework import viewsets
from djoser.views import TokenCreateView

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CustomTokenCreateView(TokenCreateView):
    def _action(self, serializer):
        user = serializer.user
        token = serializer.validated_data.get('auth_token')
        data = {
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'auth_token': token
        }
        return Response(data, status=status.HTTP_200_OK)