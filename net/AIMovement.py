from collections import deque
from game.Movement import Movement


class AIMovement(Movement):
    def __init__(self, model):
        super(AIMovement, self).__init__(model)
        self.game_number = 0
        self.epsilon = 0  # randomness
        self.gamma = 0  # discount rate
        self.memory = deque(maxlen=100_000)  # erase memory if over an amount
        self.model = model

    def move(self, key_list, avatar, food):
        avatar.move("right", food)
        return False

    def get_state(self, snake, apple):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_mem(self, state, action, reward, next_state, done):
        pass

    def train_short_mem(self, state, action, reward, next_state, done):
        pass
