from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('profiles/<pk>', views.ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='profiles'),
    path('auth/token/login', views.CustomTokenCreateView.as_view(), name='login'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]