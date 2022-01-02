from abc import abstractmethod
import random
from Display import Display
from Drawable import Drawable

class Food:
    def __init__(self):
        pass

    @abstractmethod
    def place_food(self):
        pass

class Apple(Food, Drawable):
    def __init__(self):
        self.place_food([])

    def place_food(self, out_of_boundary):
        self.x = random.randint(0, (Display.WIDTH - Display.BLOCK_SIZE)//Display.BLOCK_SIZE)*Display.BLOCK_SIZE 
        self.y = random.randint(0, (Display.HEIGHT - Display.BLOCK_SIZE)//Display.BLOCK_SIZE)*Display.BLOCK_SIZE
        self.location = (self.x, self.y)

        if self.location in out_of_boundary:
            self.place_food(out_of_boundary)

    def get_mask(self):
        return [(self.x, self.y, Display.RED)]