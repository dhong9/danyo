from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image
import numpy as np
import io

def img_to_excel(request):
    return JsonResponse({"message": "Hello world!"})