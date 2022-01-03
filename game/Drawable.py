from abc import abstractmethod


class Drawable:
    def __init__(self):
        pass

    @abstractmethod
    def get_mask(self):
        pass


