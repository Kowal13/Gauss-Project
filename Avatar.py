from abc import abstractmethod
from Display import Display
import random

class Avatar:
    
    @abstractmethod
    def move(self):
        pass


class Snake(Avatar):
    def __init__(self):
        self.head = (Display.WIDTH/2, Display.HEIGHT/2)
        self.body = [self.head, (self.head[0] - Display.BLOCK_SIZE, self.head[1]), (self.head[0] - 2*Display.BLOCK_SIZE, self.head[1])]
    
    def move(self, direction, was_apple_eaten):
        head_x = self.head[0]
        head_y = self.head[1]

        if direction == "right":
           head_x += Display.BLOCK_SIZE
        elif direction == "left":
            head_x -= Display.BLOCK_SIZE
        elif direction == "down":
            head_y += Display.BLOCK_SIZE
        elif direction == "up":
            head_y -= Display.BLOCK_SIZE

        self.head = (head_x, head_y)
    
            

