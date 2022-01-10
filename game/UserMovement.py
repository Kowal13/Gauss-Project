import pygame
from game.Movement import Movement

class UserMovement(Movement):
    def __init__(self):
        self.prev_direction = "right"

    def move(self, key_list, avatar, food):
        direction = None
        # returns the last correct code from the key list
        for event in key_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_UP:
                    direction = "up"
        
        if direction is not None:
            self.prev_direction = direction

        return avatar.move(self.prev_direction, food)
