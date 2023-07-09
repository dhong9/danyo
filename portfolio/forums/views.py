from rest_framework import viewsets
from portfolio.forums.models import Category
from portfolio.forums.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer