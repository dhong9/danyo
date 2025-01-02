from django.shortcuts import render
from django.http import JsonResponse

def img_to_excel(request):
    return JsonResponse({"message": "Hello world!"})