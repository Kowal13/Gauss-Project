from abc import abstractmethod
import random
from game.Display import Display
from Drawable import Drawable

# Food doesn't have definied location (?) - check if that's ok and if not find solution

class Food:
    def __init__(self):
        pass

    @abstractmethod
    def place_food(self):
        pass

    def food_location_from_point(self, point):
        up, right, down, left = 0, 0, 0, 0

        if self.location[0] > point[0]:
            right = 1

        if self.location[0] < point[0]:
            left = 1
        
        if self.location[1] > point[1]:
            down = 1

        if self.location[1] < point[1]:
            up = 1
        return [up, right, down, left]

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
