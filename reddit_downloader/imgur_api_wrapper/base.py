class ImgurModel:
    def __init__(self, *args, **kwargs):
        for arg in args:
            for k, v in arg.items():
                if isinstance(v, dict):
                    for ik, iv in v.items():
                        setattr(self, ik, iv)
                setattr(self, k, v)
        for k, v in kwargs.items():
            setattr(self, k, v)
