"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# Views
from portfolio.threadly import views as threadly_views
from portfolio.forums import views as forums_views
from portfolio.imgconverter import views as imgconverter_views

router = routers.DefaultRouter()
router.register(r'users', threadly_views.UserViewSet)
router.register(r'groups', threadly_views.GroupViewSet)
router.register(r'projects', threadly_views.ProjectViewSet)
router.register(r'contacts', threadly_views.ContactViewSet)
router.register(r'categories', forums_views.CategoryViewSet)
router.register(r'imgconverter', imgconverter_views.ImgConverterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('portfolio.accounts.urls')),
    path('imgconverter/', include('portfolio.imgconverter.urls')),
    path('comments', threadly_views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comments-list'),
    path('comments/<pk>', threadly_views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comments-detail'),
    path('posts', forums_views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='posts-list'),
    path('posts/<pk>', forums_views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='posts-detail'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
