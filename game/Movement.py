from abc import abstractmethod


class Movement:
    def __init__(self, model=None):
        pass

    @abstractmethod
    def move(self, key_list, avatar, food):
        pass

        