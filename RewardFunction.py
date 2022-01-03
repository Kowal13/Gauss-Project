from pygame import init


class RewardFunction:
    pass

class RF(RewardFunction):
    def __init__(self, reward, penalty):
        self.reward = reward 
        self.penalty = penalty
    pass

