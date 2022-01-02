from abc import abstractmethod


class Drawable:
    def __init__(self):
        pass

    @abstractmethod
    def get_mask(self):
        pass

    def food_eaten(self, drawable1, drawable2):
        if drawable1.get_mask()[0][0] == drawable2.get_mask()[0][0] and drawable1.get_mask()[0][1] == drawable2.get_mask()[0][1]:
            return True
        return False
