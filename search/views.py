from django.shortcuts import render

from rest_framework.views import APIView,Response,status

from .models import VectoredImage
from .serializers import VectoredImageSerializer
# Create your views here.

class VectoredImage(APIView):
    serializer_class=VectoredImageSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image=serializer.save()
            return Response({'message': f'Successfully uploaded and indexed image with ID {image.pk}'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


