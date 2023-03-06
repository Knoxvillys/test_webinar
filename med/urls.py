"""med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path


from rest_framework.routers import DefaultRouter
from django.urls import path, include

from dvd1.views import VideoViewSet, СourseViewSet

v1_router = DefaultRouter()
v1_router.register('video', VideoViewSet, basename='video')
v1_router.register('course', СourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(v1_router.urls)),
]

