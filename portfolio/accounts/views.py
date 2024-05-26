from portfolio.accounts.serializer import ProfileSerializer
from portfolio.accounts.models import Profile
from rest_framework import viewsets

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer