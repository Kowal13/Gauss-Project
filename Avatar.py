from abc import abstractmethod
from Display import Display
import random

from Drawable import Drawable
from Food import Apple

class Avatar:
    
    @abstractmethod
    def move(self, direction, drawable):
        pass

    def food_eaten(self, drawable):
        if self.get_mask()[0][0] == drawable.get_mask()[0][0] and self.get_mask()[0][1] == drawable.get_mask()[0][1]:
            return True
        return False


    def is_collision(self): 
        if self.head in self.body[1:]:
            return True

        return False
    
    def is_out_of_boundary(self):
        if self.head[0] > Display.WIDTH - Display.BLOCK_SIZE:
            return True
        elif self.head[0] < 0:
            return True
        elif self.head[1] > Display.HEIGHT - Display.BLOCK_SIZE:
            return True
        elif self.head[1] < 0:
            return True

        return False

class Snake(Avatar, Drawable):
    def __init__(self):
        self.head = (Display.WIDTH/2, Display.HEIGHT/2)
        self.body = [self.head, (self.head[0] - Display.BLOCK_SIZE, self.head[1]), (self.head[0] - 2*Display.BLOCK_SIZE, self.head[1])]

    def move(self, direction, drawable):
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
        
        if not self.food_eaten(drawable):
             self.body.pop()
             return False
        
        return True

    def get_mask(self,):
        green = self.body[1:]
        dark_green = self.head
        L = [(dark_green[0], dark_green[1], Display.DARK_GREEN)]
        for el in green:
            L.append((el[0], el[1], Display.GREEN))
        
        return L

    def _get_body(self):
        return getattr(self, 'body')

    def _check_collision_next_step(self, direction, drawable):
        # saving the VALUE of the attibute (not the attribute itself) to body_copy
        body_copy = tuple(self.body)
        danger_zone = [0, 0, 0]

        if direction == "right":
            self.move("down", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[2] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]

            self.move("right", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[1] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
            
            self.move("up", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[0] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
        
        if direction == "down":
            self.move("left", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[2] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]

            self.move("down", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[1] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
            
            self.move("right", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[0] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
            
        if direction == "left":
            self.move("up", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[2] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]

            self.move("left", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[1] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
            
            self.move("down", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[0] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]

        if direction == "up":
            self.move("right", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[2] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]

            self.move("up", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[1] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
            
            self.move("left", drawable)
            if self.is_out_of_boundary() or self.is_collision():
                danger_zone[0] = 1
            self.body = list(body_copy)
            self.head = list(body_copy)[0]
        
        return danger_zone


    
            

