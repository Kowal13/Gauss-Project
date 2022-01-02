import random
from Display import Display

class Food:
    pass

class Apple(Food):
    def __init__(self):
        self.place_apple([])

    def place_apple(self, out_of_boundary):
        self.x = random.randint(0, (Display.WIDTH - Display.BLOCK_SIZE)//Display.BLOCK_SIZE)*Display.BLOCK_SIZE 
        self.y = random.randint(0, (Display.HEIGHT - Display.BLOCK_SIZE)//Display.BLOCK_SIZE)*Display.BLOCK_SIZE
        self.location = (self.x, self.y)

        if self.location in out_of_boundary:
            self.place_apple(out_of_boundary)