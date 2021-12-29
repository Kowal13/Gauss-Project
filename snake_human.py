from typing import Text
import pygame
import os
import random

pygame.init()
pygame.mixer.init()

# RGB colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)

FPS = 10
BLOCK_SIZE = 20

EATING_SOUND = pygame.mixer.Sound("Assets/eating_sound.wav")


font = pygame.font.SysFont('comicsans', 40)

WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

class SnakeGame:
    def __init__(self):
        # def width and height of the display window
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        # caption name
        pygame.display.set_caption("Snake")

        self.clock = pygame.time.Clock()
        self.direction = "right"
        # x axis - index 0, y axis - index 1
        self.head = (WIDTH/2, HEIGHT/2)
        self.snake = [self.head, (self.head[0] - BLOCK_SIZE, self.head[1]), (self.head[0] - 2*BLOCK_SIZE, self.head[1])]
        self.score = 0
        self.food = None
        self.place_food()

    def place_food(self):
        x_cord = random.randint(0, (WIDTH - BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE 
        y_cord = random.randint(0, (HEIGHT - BLOCK_SIZE)//BLOCK_SIZE )*BLOCK_SIZE
        self.food = (x_cord, y_cord)
        if self.food in self.snake:
            self.place_food()
    
    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction = "right"
                elif event.key == pygame.K_LEFT:
                    self.direction = "left"
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"
                elif event.key == pygame.K_UP:
                    self.direction = "up"

    def move_head(self):
        head_x = self.head[0]
        head_y = self.head[1]

        if self.direction == "right":
            head_x += BLOCK_SIZE
        elif self.direction == "left":
            head_x -= BLOCK_SIZE
        elif self.direction == "down":
            head_y += BLOCK_SIZE
        elif self.direction == "up":
            head_y -= BLOCK_SIZE
        
        self.head = (head_x, head_y)

    def is_game_over(self):
        if self.head[0] > WIDTH - BLOCK_SIZE:
            return True
        elif self.head[0] < 0:
            return True
        elif self.head[1] > HEIGHT - BLOCK_SIZE:
            return True
        elif self.head[1] < 0:
            return True
        elif self.head in self.snake[1:]:
            return True
        return False

    def ui_update(self):
        self.display.fill(BLACK)
        for chunk in self.snake:
            pygame.draw.rect(self.display, BLUE, pygame.Rect(chunk[0], chunk[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

        txt = font.render("Score:" + str(self.score), True, WHITE)
        self.display.blit(txt, [0, 0])
        pygame.display.flip()
        self.clock.tick(FPS)

    def play_step(self):
        # get user input
        self.user_input()

        # move the snake accordingly (the end of the tail will be cut off if the snake doesn't eat an apple)
        self.move_head()
        self.snake.insert(0, self.head)
        # check if game is over and return score
        if self.is_game_over():
            return self.is_game_over(), self.score
        # place food 
        if self.head == self.food:
            EATING_SOUND.play()
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()
        
        # update to the display
        self.ui_update()

        return self.is_game_over(), self.score


def main():
    game_over = False
    game = SnakeGame()
    while not game_over:
        game_over, score = game.play_step()
        print(game_over, score)
    
    print("Score:", score)
    pygame.quit()

# run file if opened directly (i.e. not imported)
if __name__ == "__main__":
    main()

