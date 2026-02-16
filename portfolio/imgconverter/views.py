from rest_framework import viewsets
from portfolio.imgconverter.models import ImgConverter
from portfolio.imgconverter.serializers import ImgConverterSerializer

class ImgConverterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = ImgConverter.objects.all()
    serializer_class = ImgConverter