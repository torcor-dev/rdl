from .base import ImgurModel
from .image import Image


class Album(ImgurModel):
    def __init__(self, *args, **kwargs):
        self.type = "album"
        self.images = []
        super().__init__(*args, **kwargs)
        self.images = [Image(img) for img in self.images]
