from rest_framework import serializers

from .models import Video, –°ourse


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class –°ourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = –°ourse
        fields = '__all__'
