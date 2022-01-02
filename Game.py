import pygame
from Avatar import Snake
from Display import Display
from Food import Apple

class Game:
    FPS = 10
    
    def __init__(self, display, snake, apple, movement, keyboard):
        self.keyboard = keyboard
        self.clock = pygame.time.Clock()
        self.score = 0
        self.iteration = 0
        self.snake = snake 
        self.apple = apple
        self.display = display
        self.movement = movement
        self.plot_score = []
        self.plot_mean_score = []
        self.eating_sound = pygame.mixer.Sound("Assets/eating_sound.wav")

    def reset(self):
        self.score = 0
        self.iteration = 0
        self.snake = Snake()
        self.apple = Apple()
        self.display = Display() 

    def run(self):
        is_game_over = False
        while not is_game_over:
            is_game_over = self.play_step()

        print("Score:", self.score)
        pygame.quit()            
 
    def should_quit(self, key_list):
        for ev in key_list:
            if ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return True

    def play_step(self):
        key_list = self.keyboard.get_event_list()
        if self.should_quit(key_list):
            return True

        was_apple_eaten = self.snake.move(self.movement.get_move(key_list), self.snake, self.apple)
        is_game_over = self.is_game_over()
        if is_game_over:
            return True
        if was_apple_eaten:
            self.score += 1
            self.apple.place_food(self.snake.body)
            self.eating_sound.play()
        self.display.update([self.snake, self.apple], self.score)
        self.clock.tick(self.FPS)

        return is_game_over


    def is_game_over(self):
        if self._is_collision() or self._is_out_of_boundary():
            return True

        return False

    def _is_collision(self): 
        if self.snake.head in self.snake.body[1:]:
            return True

        return False
    
    def _is_out_of_boundary(self):
        if self.snake.head[0] > Display.WIDTH - Display.BLOCK_SIZE:
            return True
        elif self.snake.head[0] < 0:
            return True
        elif self.snake.head[1] > Display.HEIGHT - Display.BLOCK_SIZE:
            return True
        elif self.snake.head[1] < 0:
            return True

        return False