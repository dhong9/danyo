from portfolio.imgconverter.models import ImgConverter
from rest_framework import serializers


class ImgConverterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgConverter
        fields = '__all__'