from django.urls import path
from . import views

urlpatterns = [
    path("img_to_excel", views.img_to_excel, name="img_to_excel")
]