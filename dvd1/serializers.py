from rest_framework import serializers

from .models import Video, Сourse


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class СourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сourse
        fields = '__all__'
