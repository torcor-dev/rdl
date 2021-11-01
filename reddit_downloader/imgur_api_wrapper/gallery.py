from .base import ImgurModel
from .image import Image


class Gallery(ImgurModel):
    def __init__(self, *args, **kwargs):
        self.type = "gallery"
        self.images = []
        super().__init__(*args, **kwargs)
        self.images = [Image(img) for img in self.images]
