from django.urls import path
from . import views

urlpatterns = [
    path("img_to_excel", views, name="img_to_excel")
]