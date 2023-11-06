from collections.abc import Iterable
from django.db import models
from PIL import Image

from .clip import encode_image
from .index import add_item_to_index,remove_item_with_id
# Create your models here.

class VectoredImage(models.Model):
    image=models.ImageField()
    # id=models.id

    def save(self, **kwargs) -> None:
        encoded_image=encode_image(Image.open(self.image))
        print(encoded_image.shape)
        super().save(**kwargs)
        add_item_to_index(encoded_image,self.pk)
        

    def delete(self,**kwargs) -> tuple[int, dict[str, int]]:
        remove_item_with_id(self.pk)
        return super().delete(**kwargs)