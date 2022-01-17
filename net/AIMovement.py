from collections import deque
from game.Movement import Movement


class AIMovement(Movement):
    def __init__(self, model):
        super(AIMovement, self).__init__(model)
        self.model = model
        self.game_number = 0
        self.epsilon = 0  # randomness
        self.gamma = 0  # discount rate
        self.memory = deque(maxlen=100_000)  # erase memory if over an amount
        self.model = model

    def move(self, avatar, food, key_list=None):
        avatar.move("right", food)
        return False

    def get_state(self, snake, apple):
        collision_next_step = snake.check_collision_next_step()
        food_location_from_point = apple.food_location_from_point(snake.head)
        return [self.prev_direction, collision_next_step, food_location_from_point]

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_mem(self, state, action, reward, next_state, done):
        pass

    def train_short_mem(self, state, action, reward, next_state, done):
        pass
