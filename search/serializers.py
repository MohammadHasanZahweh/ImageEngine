from rest_framework import serializers

from .models import VectoredImage

class VectoredImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VectoredImage
        fields = "__all__"