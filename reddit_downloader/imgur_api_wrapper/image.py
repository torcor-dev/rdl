from .base import ImgurModel


class Image(ImgurModel):
    def __init__(self, *args, **kwargs):
        self.type = "image"
        super().__init__(*args, **kwargs)
