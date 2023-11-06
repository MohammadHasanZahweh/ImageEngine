from django.urls import path

from .views import VectoredImage
urlpatterns = [
    path("vectored-image",VectoredImage.as_view())
]