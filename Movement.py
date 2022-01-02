from abc import abstractmethod


class Movement:
    def __init__(self, model = None):
        pass

    @abstractmethod
    def get_move(self, key_list):
        pass

        