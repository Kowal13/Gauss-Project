from abc import abstractmethod
from Display import Display
import random

from Drawable import Drawable

class Avatar:
    
    @abstractmethod
    def move(self, direction, drawable1, drawable2):
        pass


class Snake(Avatar, Drawable):
    def __init__(self):
        self.head = (Display.WIDTH/2, Display.HEIGHT/2)
        self.body = [self.head, (self.head[0] - Display.BLOCK_SIZE, self.head[1]), (self.head[0] - 2*Display.BLOCK_SIZE, self.head[1])]
    
    def move(self, direction, drawable1, drawable2):
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

        self.body.insert(0, self.head)
        if not self.food_eaten(drawable1, drawable2):
            self.body.pop()
            return False
        
        return True

    def get_mask(self):
        green = self.body[1:]
        dark_green = self.head
        L = [(dark_green[0], dark_green[1], Display.DARK_GREEN)]
        for el in green:
            L.append((el[0], el[1], Display.GREEN))
        
        return L

    
            

