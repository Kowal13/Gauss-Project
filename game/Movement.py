from abc import abstractmethod


class Movement:
    def __init__(self, model=None):
        self.prev_direction = "right"

        self.model = model

        pass

    @abstractmethod
    def move(self, avatar, food, key_list=None):
        pass

        