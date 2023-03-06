from rest_framework.viewsets import ModelViewSet

from .models import Video, Сourse
from .serializers import (
    VideoSerializer,
    СourseSerializer
)


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class СourseViewSet(ModelViewSet):
    queryset = Сourse.objects.all()
    serializer_class = СourseSerializer
