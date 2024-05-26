from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('update/<pk>/', views.UpdateView.as_view(), name='auth_update'),
    path('delete/<pk>/', views.UpdateView.as_view(), name='auth_delete'),
    path('test/', views.testEndPoint, name='test'),
    path('profiles/<pk>', views.ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='profiles'),
    path('', views.getRoutes),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]